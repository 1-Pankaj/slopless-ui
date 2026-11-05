#!/usr/bin/env node
/**
 * finish.mjs: the browser finishing pass.
 *
 * Opens a page in a real browser, screenshots it at desktop and phone widths,
 * collects console errors, page errors, and failed requests, and fails on
 * horizontal overflow. Optional but strongly recommended by SKILL.md; every
 * environment that cannot run it should substitute any other way to look at
 * the rendered page (see references/verification.md).
 *
 * Requirements: Node 18+. Playwright is resolved from the current working
 * project directory (not from this skill's installation folder):
 *     npm i -D playwright && npx playwright install chromium
 *
 * Usage:
 *     node finish.mjs <url-or-file> [--widths 1440,390] [--out verify-out] [--full] [--strict-network]
 */

import { existsSync, mkdirSync } from "node:fs";
import { createRequire } from "node:module";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";

const DEFAULT_WIDTHS = [1440, 390];

function parseArgs(argv) {
  const args = { widths: DEFAULT_WIDTHS, out: "verify-out", full: false, strictNetwork: false, target: null };
  const rest = argv.slice(2);
  for (let i = 0; i < rest.length; i++) {
    const arg = rest[i];
    if (arg === "--widths") {
      if (!rest[i + 1] || rest[i + 1].startsWith("--")) {
        console.error("--widths needs a comma-separated list, for example 1440,390.");
        process.exit(2);
      }
      args.widths = rest[++i].split(",").map((n) => parseInt(n, 10)).filter((n) => Number.isFinite(n) && n > 0);
    } else if (arg === "--out") {
      if (!rest[i + 1] || rest[i + 1].startsWith("--")) {
        console.error("--out needs a directory path.");
        process.exit(2);
      }
      args.out = rest[++i];
    } else if (arg === "--full") {
      args.full = true;
    } else if (arg === "--strict-network") {
      args.strictNetwork = true;
    } else if (arg === "-h" || arg === "--help") {
      console.log("Usage: node finish.mjs <url-or-file> [--widths 1440,390] [--out verify-out] [--full] [--strict-network]");
      process.exit(0);
    } else {
      args.target = arg;
    }
  }
  if (!args.target || args.widths.length === 0) {
    console.error("Give a URL or a file path, and at least one width.");
    process.exit(2);
  }
  return args;
}

async function loadPlaywright() {
  const fromProject = createRequire(resolve(process.cwd(), "__slopless_ui_resolver__.cjs"));
  try {
    return fromProject("playwright");
  } catch {
    try {
      return fromProject("playwright-core");
    } catch {
      console.error(
        [
          "Playwright is not installed, so this script cannot open a browser.",
          "",
          "Install it in the project directory from which you are running this command:",
          "    npm i -D playwright && npx playwright install chromium",
          "",
          "Global playwright-cli commands are not importable Playwright packages.",
          "Or skip this script and verify with any other browser tool available",
          "in your environment (agent browser, headless CLI, dev server plus",
          "screenshots). The point is looking at the rendered page; this file",
          "is only one way to do that.",
        ].join("\n")
      );
      process.exit(3);
    }
  }
}

async function main() {
  const args = parseArgs(process.argv);
  const { chromium } = await loadPlaywright();

  let url = args.target;
  if (!/^https?:\/\//i.test(url)) {
    const filePath = resolve(url);
    if (!existsSync(filePath)) {
      console.error("File not found: " + filePath);
      process.exit(2);
    }
    url = pathToFileURL(filePath).href;
  }

  mkdirSync(args.out, { recursive: true });

  const browser = await chromium.launch();
  const problems = [];
  const summary = [];
  const networkWarnings = [];

  for (const width of args.widths) {
    const height = width < 600 ? 844 : 900;
    const context = await browser.newContext({
      viewport: { width, height },
      deviceScaleFactor: 1,
      reducedMotion: "reduce",
    });
    const page = await context.newPage();

    const consoleErrors = [];
    const pageErrors = [];
    const failedRequests = [];
    const documentErrors = [];
    page.on("console", (message) => {
      if (message.type() === "error") {
        const text = message.text();
        // Chromium reports many failed assets as console errors too. Keep those
        // in the network warning list instead of failing the page twice.
        if (!/^Failed to load resource:/i.test(text) && !/\bnet::ERR_[A-Z_]+\b/.test(text)) {
          consoleErrors.push(text);
        }
      }
    });
    page.on("pageerror", (error) => pageErrors.push(String(error)));
    page.on("requestfailed", (request) => {
      failedRequests.push(request.url() + " (" + (request.failure()?.errorText || "failed") + ")");
    });
    page.on("response", (response) => {
      if (response.status() < 400) return;
      const request = response.request();
      const detail = response.url() + " (HTTP " + response.status() + ")";
      if (request.resourceType() === "document") documentErrors.push(detail);
      else failedRequests.push(detail);
    });

    await page.goto(url, { waitUntil: "load", timeout: 30000 });
    await page.evaluate(() => document.fonts.ready).catch(() => {});
    await page.waitForTimeout(350);

    const overflow = await page.evaluate(
      () => document.documentElement.scrollWidth - document.documentElement.clientWidth
    );
    if (overflow > 1) {
      problems.push(width + "px: horizontal overflow of " + overflow + "px");
    }

    const shot = resolve(args.out, "page-" + width + ".png");
    await page.screenshot({ path: shot, fullPage: args.full });

    summary.push(
      width + "px: screenshot " + shot +
      (consoleErrors.length ? ", console errors " + consoleErrors.length : "") +
      (pageErrors.length ? ", page errors " + pageErrors.length : "") +
      (documentErrors.length ? ", document errors " + documentErrors.length : "") +
      (failedRequests.length ? ", failed requests " + failedRequests.length : "")
    );

    for (const text of consoleErrors) problems.push(width + "px console error: " + text);
    for (const text of pageErrors) problems.push(width + "px page error: " + text);
    for (const text of documentErrors) problems.push(width + "px document response: " + text);
    for (const text of failedRequests) networkWarnings.push(width + "px failed request: " + text);
    if (args.strictNetwork) {
      for (const text of failedRequests) problems.push(width + "px failed request: " + text);
    }

    await context.close();
  }

  await browser.close();

  console.log("Checked: " + url);
  for (const line of summary) console.log("  " + line);
  const hasNetworkWarnings = summary.some((line) => /failed requests [1-9]\d*/.test(line));
  if (!args.strictNetwork && hasNetworkWarnings) {
    console.log("Network requests that failed are review warnings by default; use --strict-network to fail on them.");
    for (const warning of networkWarnings) console.log("  warning: " + warning);
  }
  if (problems.length) {
    console.log("\nProblems (" + problems.length + "):");
    for (const line of problems) console.log("  " + line);
    console.log("\nFail. Fix and re-run, then look at the screenshots yourself.");
    process.exit(1);
  }
  if (hasNetworkWarnings) {
    console.log("\nNo blocking console/page errors or horizontal overflow. Review the failed-request warnings above.");
    console.log("Still open the screenshots and run the squint test (references/verification.md).");
    return;
  }
  console.log("\nNo console errors, no failed requests, no horizontal overflow.");
  console.log("Still open the screenshots and run the squint test (references/verification.md).");
}

main().catch((error) => {
  console.error("finish.mjs failed: " + error.message);
  process.exit(1);
});

# Copy

Text is part of the design. A beautiful screen with bloated copy reads as slop in the first two seconds. Open this whenever you write or edit user-facing text: headlines, body, buttons, errors, empty states, tooltips, release notes.

## The em dash rule

Never use an em dash in user-facing text. Not in headlines, not in body copy, not in tooltips, not in commit-style asides. This is the single most reliable tell of machine-written text, and it is also just lazy punctuation.

Replace by meaning:

| Instead of | Use |
|---|---|
| A quick aside, like this one, mid-sentence | A comma, or parentheses for a true aside |
| A break that lands | A period. Then a short sentence. |
| An introduction to a list | A colon |
| Ranges like 2019-2024 | A plain hyphen |

The same discipline applies to this skill's own documentation. A rule you do not follow yourself convinces nobody.

## Plain language

Aim for text a busy person understands on one pass:

- Short sentences. If one breath is not enough, make two.
- Concrete nouns. "Report", "invoice", "yesterday's failures", not "solutions", "content", "assets".
- Active voice. "The export failed" beats "An error was encountered during export."
- Explain a term the first time it appears, or pick a plainer term.
- Reading level: if a sentence needs a second read, rewrite it. Complex products need plain words more than anyone.

## Cadence: the rhythm of a person writing

Banned words are the loud tells. The quieter tell is rhythm. Machine text has an even pulse; human text breathes. This is what makes text read as written rather than generated, and no word list can catch it:

- **Vary sentence length on purpose.** Follow a long sentence with a short one. Three sentences of the same length in a row read as generated even when every word is fine.
- **Paragraphs breathe unevenly.** One idea per paragraph, and paragraphs of different lengths. Four paragraphs of exactly three sentences each were not written by a person in a hurry to say something.
- **Use the contractions a person would use.** "We're", "doesn't", "you'll". Stiff formality reads as a mask; forced chirpiness reads worse.
- **Specifics beat adjectives.** "Ships in 3 working days" is a fact. "Ships quickly" is filler dressed as information.
- **Puncture the pattern once in a while.** A two-word answer where a paragraph was expected. A fragment that lands. A number where an adjective was queued. Uniformity is the tell, so break it deliberately.
- **Headings do not have to match.** "What you get", "Why the presses are old", and "Open Tuesday to Friday" can all live on one page. Grammatically parallel heading sets read as a form.

## The humanizer pass

Cadence rules are the theory. The humanizer pass is the practice: run it over every finished screen before delivery, in this order.

1. **Read it aloud, once.** Anywhere you stumble, the reader stumbles. Anywhere you hear a presentation voice, rewrite it.
2. **Delete the first sentence.** Most drafts warm up before they say anything. "Oscilla is proud to introduce" carries nothing; start at the second sentence and check nothing was lost.
3. **Name the user's world.** The sentence should contain at least one noun the user recognizes from their own work: invoices, room levels, the gate, p99. Abstract nouns ("teams", "workflows", "experiences") mean the sentence has not started yet.
4. **Trade adjectives for units.** "Fast" becomes "31 ms". "Reliable" becomes "99.99% uptime, trailing 90 days". "Huge lineup" becomes "forty artists". A number with its unit is a claim a reader can check; an adjective is a mood.
5. **Break the rhythm on purpose.** Follow the longest sentence on the screen with the shortest. Let one line be a fragment that lands: "Small studio. Loud work." Uniform rhythm is the machine tell no word list catches.
6. **Let the product be specific.** Buttons name objects ("Create a free key", not "Get Started"). Empty states name the thing that belongs there. Errors say what happened in the world ("The connection dropped"), not in the code ("Error 502").
7. **Keep one human aside per page.** A footnote that admits something ("measured hourly, published even when a number slips"), a stat with personality ("2 office dogs"), a line that talks to one person ("we reply within two working days, usually with questions"). One is voice; three is a gimmick.
8. **Check the sample data too.** Names, streets, and numbers in mockups are copy. "John Doe" is a fingerprint of nobody; "Vera Mold" or "Annika Dorn" is a person who could exist.

If the page passes all eight, it will still fail the read-aloud test sometimes. That is the test working. Fix it and read again.

## Banned words and patterns

These words and constructions are reliable slop markers. When one shows up, the sentence around it is usually hiding a real point. Find the point and write that instead.

- Hollow superlatives: seamless, effortless, revolutionary, game-changing, cutting-edge, next-generation, best-in-class, world-class, state-of-the-art, robust, powerful, stunning, beautiful (about the product itself), elevate, unleash, unlock, supercharge, empower, transform, streamline, optimize (about abstract things), leverage (as a verb), synergy, ecosystem, holistic, delve, tapestry, landscape (metaphorical), journey (for anything but actual trips), realm, robust.
- Framing devices: "In today's fast-paced world", "Welcome to", "Meet X" as a universal opener, "It's not just X, it's Y", "Whether you're A or B", rhetorical questions as hooks, "Look no further", "At X, we believe".
- Empty pluralisms: "features", "benefits", "solutions" with no noun attached, "a wide range of", "various", "everything you need".
- Punctuation noise: exclamation marks in UI text, ALL CAPS sentences, multiple punctuation marks ("Now available!"), and em dashes (see above).

None of these are banned because the words are bad. They are banned because they appear instead of information.

## Microcopy by surface

**Buttons** start with a verb and name the object: "Save changes", "Create invoice", "Invite people". Never "Submit", "OK", "Yes", or "Learn more" when "Read the pricing guide" fits.

**Errors** say what happened, say why when known, and say what to do:

> We could not save your changes. The connection dropped while uploading. Your edits are still open; try again.

Rules: no raw error objects, no "Oops", no blaming the user ("You entered an invalid date" becomes "Enter a date like 24 Mar 2026"), and network errors are worded differently from validation errors.

**Empty states** say what belongs here and give the first action:

> No invoices yet. Create your first invoice to see payment status here.

**Labels and hints** sit above fields and are visible. Placeholder text is an example of the content ("Acme Ltd"), never the label.

**Confirmation for destructive actions** names the thing: "Delete 3 invoices? This cannot be undone." Prefer reversible undo over confirmation when possible.

**Numbers and dates** in the user's format, no invented precision: "About 3 minutes left", not "ETA 00:03:12", unless the app is a timer.

## Voice in one test

Read the copy aloud. If it sounds like a person explaining something to another person, ship it. If it sounds like a slide deck, a banner ad, or a language model being helpful, rewrite it shorter. When unsure, delete the first sentence and see if anything was lost. Usually nothing was.

## Sample data

Sample content is copy too. Use realistic, varied values: long names, short names, a zero, a missing value, a large number. "John Doe", "123 Main Street", and "Test User" hide layout bugs and make every demo look the same. Never present invented metrics, testimonials, or customer logos as real; label them or leave them out.

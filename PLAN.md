# NOLAP GIFTS: Plan

Make a gift feel like a little film and a real app at once. Pick an occasion, add your photos, videos, words and a song, and send one private link.

## Working agreement

- Plan each big feature together first, then build it.
- UI and animation first, shipped in small slices that are tested live.
- The product name is always written **NOLAP GIFTS** in caps.
- Commit messages are plain, with no tool attribution.
- Nothing goes to `main` until the look has been previewed and approved.

## Principles

- Words stay on screen long enough to read: 2.6 s plus 0.56 s per word, never under 4.4 s.
- Every gift opens like a phone app (status bar, app bar, docked sheet, tab bar).
- Private by default: unguessable link, `noindex`, optional password and expiry.
- One tap to open on any phone. Works in WhatsApp's in-app browser.

## Slice 1 (done): Toria's 8 month page

A hand-built gift that proves the format.

## Slice 2: Make the page data-driven

Turn the hard-coded page into a template that reads one gift config: names, start date, scene list, messages, photos, video, song, palette. No new look, only the engine behind it.

## Slice 3: Occasion templates

Anniversary, birthday, Valentine's, apology, proposal, mother's day, graduation, new baby. Each has its own scenes and wording, with one shared engine.

## Slice 4: Gift builder

A short guided form: names, date, upload photos and videos (cropped for faces), write or choose messages, pick a song, preview, publish. Output is one link and a QR code.

## Slice 5: Payments and delivery

Mobile money and card (Paystack). Gifts are paid before the link goes live. Share to WhatsApp in one tap. Optional password and expiry.

## Slice 6: Music

Licensed or royalty-free library inside the builder. Customers cannot upload commercial songs. This is a legal requirement for a public product.

## Open questions

- Pricing: per gift, or bundles?
- Does a gift live forever, or for a set time (for example 1 year)?
- Do we offer a downloadable video version as an add-on?
- Which occasion templates ship first?

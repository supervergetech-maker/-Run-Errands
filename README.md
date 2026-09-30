# Run Errands — website notes (v2)

**Deliverable:** `index.html` — a single, self-contained one-page website (fonts, logo, QR and
imagery are all embedded, so you can email it, WhatsApp it or upload it anywhere as one file).

## What was already in the client's flyers (used as-is)

| Item | Value |
|---|---|
| Business name | Run Errands |
| Tagline | "Got an Errand? We'll handle it" |
| Positioning line | "From shopping to pickups, deliveries and everyday tasks. We get it done for you." |
| Trust line | Reliable · Fast · Convenient |
| Services | Grocery & Personal Shopping · Parcel Pickup & Delivery · Pharmacy Pickup · Laundry Pickup & Drop-off · Document Pickup & Delivery · Personal Errands & Purchase |
| WhatsApp / phone | +234 906 807 2310 (0906 807 2310) |
| Email | runerrands@gmail.com |
| Base | Alaba, Lagos, Nigeria |
| Brand colours | Green `#0D8E4D`, Lime `#A8DB3C`, Navy `#0A1E33`, Orange `#F5881F` (sampled from the client's files) |
| Logo | Extracted from the client's logo file and re-tiled for the header/favicon |

## The client's QR code — decoded

The QR printed on their flyers resolves to:

```
https://wa.link/kp78yr
   → https://api.whatsapp.com/send?phone=2349068072310
        &text=Hi RUN ERRANDS — I have an errand I'd like you to handle.
```

The site reuses **that exact same code**, so the QR on the website, on their flyers and on any
printed material all open the same chat. Clean copies: `assets/wa-qr.png` and `assets/wa-qr.svg`.

## Rule applied in v2: nothing on the page that the client didn't confirm

v1 contained a "Join the team / run errands and earn" recruitment section and a few unconfirmed
claims. **All of it has been removed.** Nothing about recruiting, hiring, coverage, opening hours,
payment terms or turnaround times is asserted on the site any more. The site now only states what
the flyers state, plus neutral phrasing like *"send us your location and we'll confirm before taking
the job on."*

Ask the client before adding anything like that back.

## What was upgraded in v2

1. **Each service opens its own WhatsApp template.** Tapping "Request this" on Grocery Shopping
   opens WhatsApp with *"I'd like help with grocery & personal shopping — What I need / My location /
   When I need it:"* — the customer only fills in blanks instead of writing from scratch. Six
   templates + the generic greeting = 7 distinct links, all verified.
2. **New "Four things to include" section** — tells a first-time customer exactly what to send
   (what you need / where you are / when / anything we should know). This is the single biggest
   cause of back-and-forth in this kind of business, and it needs no business facts.
3. **Search + share data added** — LocalBusiness JSON-LD schema (services, phone, email, address)
   and Open Graph / Twitter card tags, so the link shows a proper branded preview card when shared
   on WhatsApp, Facebook, X or LinkedIn.
4. **Share image generated** — `assets/og-cover.png` (1200×630) is the preview card, plus
   `assets/status-1080x1920.png` and `assets/poster-1080x1350.png` for WhatsApp status / Instagram.
   Regenerate with `python3 og.py` after editing `og-card.html`.
5. **Accessibility** — skip link, visible focus rings, semantic headings, alt text, reduced-motion
   support.
6. Copy tightened to remove over-claims (e.g. no more "we run errands across Lagos", no more
   "same day" promises).

### Open items for the client

| # | Question | Why it matters |
|---|---|---|
| 1 | Which areas do you actually cover? | The site is deliberately vague. Naming areas converts much better. |
| 2 | What are your opening hours? | Not stated anywhere on the site. |
| 3 | How do you want to be paid? | FAQ currently says "we confirm the cost and how you'd like to pay before the job starts". |
| 4 | Any dispatch fee, minimum order or service fee? | Nothing about pricing is on the site. |
| 5 | Can you confirm the "we keep you updated along the way" promise in How it works, step 3? | It is the one service promise still written as a fact. |
| 6 | Is a runner/partner recruitment programme actually happening? | v1 assumed yes; it was removed. If it is real, the section can go back in. |
| 7 | Are the new service photos approved? | They are AI-generated illustrations, not photos of Run Errands staff or completed jobs; replace with real approved images if available. |

## What was upgraded in v3

1. **Working request form.** The "Four things to include" section became a real form: pick a service,
   type the details, add location and timing, and it composes a clean message and opens WhatsApp with
   it — or copies it to the clipboard. No backend, nothing stored anywhere, and the customer still has
   to press send in WhatsApp. Biggest single conversion win on the page.
2. **Installable on phones** (`manifest.json` + generated app icons). Customers can add it to their
   home screen from the browser, so it behaves like an app and stays one tap from the chat.
3. **Smaller and faster** — hero photo re-compressed (70 KB → 42 KB), page weight 212 KB → 175 KB.
4. **Tappable QR** — the QR now opens the WhatsApp chat when tapped, not just when scanned.
5. **More fold headroom on small phones** — the "Make a request" button now clears the fold on every
   screen tested (360×640 up to 430×932).
6. **`whatsapp-templates.md`** — greeting, away message, 11 quick replies, catalogue copy, profile and
   labels, ready to paste into WhatsApp Business.

## Motion design

Motion here is a **system with a job**, not decoration. Two things drive it: one easing curve per
role, and one arrival pattern that every block on the page shares — so scrolling down feels like
one continuous hand moving down a page, not six unrelated effects.

### The vocabulary

| Token | Curve | Role |
|---|---|---|
| `--ease-expo` | `cubic-bezier(.16,1,.3,1)` | Entrances — fast out, long quiet settle |
| `--ease-quart` | `cubic-bezier(.25,1,.5,1)` | On-screen moves: hover and FAQ |
| `--ease-inout` | `cubic-bezier(.83,0,.17,1)` | Loops and anything reversible — drift, float |
| `--ease-spring` | `cubic-bezier(.34,1.46,.64,1)` | Small playful elements only: chips, buttons, the tray |
| `--d1 / d2 / d3 / d4` | 170 / 280 / 620 / 940 ms | Micro / quick / standard arrival / cinematic headline |

### Scroll as a timeline

This version takes its direction from the supplied motion demo: **scroll is the timeline**. The
motion continuously follows your position instead of only firing once when a section enters view.

- **Hero zoom:** the green backdrop scales up as you leave the opening scene; copy lifts and softens,
  while the trolley artwork moves on a slower parallax rate.
- **Pinned services journey:** “What we handle” stays in place while the six service cards—with
  illustrative service photos—travel left-to-right under vertical scrolling. Short viewports and
  reduced-motion users see the responsive grid instead.
- **Image-style reveal:** the contact QR panel opens from the centre, using a rounded clip reveal.
- **A quiet closing wave:** letters in the final CTA move by a few pixels as that line crosses the
  viewport; its accessible label remains the original full sentence.
- The changing-width strip beneath the navbar and its moving nav underline are removed. The how-it-
  works rail, independent section parallax and hero route-line draw remain.

The rest of the page keeps the shared arrival language: headings rise behind a mask, request fields
assemble in order, and FAQ/contact blocks cascade in. The reference’s dramatic black/gold look was
not copied; the motion is translated into the Run Errands green/lime brand and kept restrained.

### Robust by construction

The default state of every element is **visible**. Motion is added on `.in` when an element is
observed, so if JavaScript never runs, the page is still complete — verified in a no-JS context.
This is also why arrivals use *animations* on class-in rather than transitions: they can never fight
the hover transition on the same element.

Under `prefers-reduced-motion: reduce`, the pinned horizontal journey becomes the normal responsive
service grid, and the scroll zoom, text wave and clip reveal stop. Entrance motion, rail and parallax
are also switched off; content remains visible and usable. Verified in an emulated reduced-motion
context.

### Verified, not assumed

Zero console errors · 15/15 observed blocks revealed · all 6 services traverse the pinned rail
end-to-end (1,150px desktop / 1,686px at 390px) · hero scale measured from 1.00 to 1.09 during
scroll · no mobile horizontal overflow · reduced-motion and no-JS layouts fall
back to the visible grid · form still composes and hands off to WhatsApp · mobile CTA clears the fold
on four device sizes.

## How the site is built

- Mobile-first, responsive, no frameworks, no build step, no internet needed to view it.
- Every WhatsApp/call/email button is live and tap-to-action; sticky Call + WhatsApp bar on phones,
  floating WhatsApp button on desktop.
- Structure: Hero → 6-service pinned scroll rail (normal grid without motion) → Send a request (form) → How it works (3 steps) → Why us →
  Contact + QR → FAQ → final call to action → footer.

### Files

```
runerrands/
├── index.html        ← the finished website (open in any browser)
├── template.html     ← source with {{placeholders}} if you want to edit text
├── build.py          ← re-embeds assets into index.html after you edit the template
├── og-card.html      ← source of the social/share images
├── og.py             ← regenerates the share image + status + poster PNGs
├── manifest.json     ← install-to-home-screen config
├── whatsapp-templates.md ← greeting, away message & quick replies to paste into WhatsApp Business
└── assets/           ← logo marks, cart photo, fonts, WhatsApp QR, social images
```

### Editing

- **Quick text change:** open `index.html` in any text editor and edit the words directly.
- **Proper way:** edit `template.html`, then run `python3 build.py` to regenerate `index.html`.
- **Change the WhatsApp number:** update `PHONE` at the top of `build.py` (the QR is generated there
  from the short link `https://wa.link/kp78yr`).
- **Change what a service message says:** the `MESSAGES` dictionary in `build.py`.
- Requires `segno` (`pip install segno`) only if you regenerate the QR.

### Publishing note

`og:image` is a relative path (`assets/og-cover.png`). When you host the site, upload the `assets`
folder alongside `index.html`. Note that WhatsApp/Google only show the preview image when the link
has a public `https://` address — sending the HTML file directly won't show it.

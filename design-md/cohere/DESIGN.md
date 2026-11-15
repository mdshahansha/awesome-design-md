---
version: alpha
name: Cohere-design-analysis
description: Cohere's 2026 web system is a controlled enterprise AI interface built from stark white editorial space, deep green-black product bands, soft mineral surfaces, rounded media cards, and a distinctive type split between monospaced-feeling display headlines and precise Unica77 UI text.

colors:
  primary: "#17171c"
  cohere-black: "#000000"
  ink: "#212121"
  deep-green: "#003c33"
  dark-navy: "#071829"
  canvas: "#ffffff"
  soft-stone: "#eeece7"
  pale-green: "#edfce9"
  pale-blue: "#f1f5ff"
  hairline: "#d9d9dd"
  hairline-strong: "#75758a"
  border-light: "#e5e7eb"
  card-border: "#f2f2f2"
  muted: "#93939f"
  slate: "#75758a"
  body-muted: "#616161"
  action-blue: "#1863dc"
  focus-blue: "#4c6ee6"
  focus-on-dark: "#ffad9b"
  coral: "#ff7759"
  coral-soft: "#ffad9b"
  form-focus: "#9b60aa"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#b30000"

typography:
  hero-display:
    fontFamily: CohereText
    fontSize: 96px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -1.92px
  product-display:
    fontFamily: CohereText
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -1.44px
  section-display:
    fontFamily: Unica77 Cohere Web
    fontSize: 60px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -1.2px
  section-heading:
    fontFamily: Unica77 Cohere Web
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.48px
  card-heading:
    fontFamily: Unica77 Cohere Web
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.32px
  feature-heading:
    fontFamily: Unica77 Cohere Web
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body-large:
    fontFamily: Unica77 Cohere Web
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body:
    fontFamily: Unica77 Cohere Web
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button:
    fontFamily: Unica77 Cohere Web
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.71
    letterSpacing: 0
  caption:
    fontFamily: Unica77 Cohere Web
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono-label:
    fontFamily: CohereMono
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.28px
  micro:
    fontFamily: Unica77 Cohere Web
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 22px
  xl: 30px
  pill: 32px
  full: 9999px

spacing:
  xxs: 2px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  section: 80px

motion:
  duration-instant: 60ms
  duration-fast: 100ms
  duration-base: 150ms
  duration-slow: 220ms
  duration-emphasis: 300ms
  ease-standard: cubic-bezier(0.2, 0, 0.2, 1)
  ease-enter: cubic-bezier(0, 0, 0.2, 1)
  ease-exit: cubic-bezier(0.4, 0, 1, 1)
  stagger-step: 20ms
  duration-reduced: 100ms

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 8px 0
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.xl}"
    padding: 6px 12px
  announcement-bar:
    backgroundColor: "{colors.cohere-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.micro}"
    height: 36px
  hero-photo-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
  agent-console-card:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    padding: 24px
  trust-logo-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  capability-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 24px
  dark-feature-band:
    backgroundColor: "{colors.deep-green}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: 80px
  product-card:
    backgroundColor: "{colors.soft-stone}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 32px
  blog-filter-chip:
    backgroundColor: transparent
    textColor: "{colors.coral}"
    typography: "{typography.card-heading}"
    rounded: "{rounded.sm}"
    padding: 8px 14px
  research-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-large}"
  contact-form-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 32px
  footer-newsletter:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.micro}"
---

## Overview

Cohere's current web presence feels like a sober enterprise AI command center with editorial restraint. The home page opens on a huge typographic declaration over a white canvas, then uses photography, dark product mockups, trust logos, and generous empty space to make AI infrastructure feel controlled rather than speculative. Product pages invert the tone into deep green-black or dark navy bands, while blog and research pages move toward publishing-system clarity: large filters, thin rules, dense lists, and pale technical backgrounds.

What makes the system distinctive is the mix of austere black-and-white UI with bursts of tactile brand imagery. The site avoids decorative chrome in the normal interface; color arrives through photography, abstract 3D media, coral blog taxonomy chips, blue research links, and dark product environments. Cards are rounded but not cute. Type is large, tight, and almost monospaced in spirit, creating a research-lab cadence across marketing, product, and editorial surfaces.

**Key Characteristics:**
- Monumental display headlines with very tight line height and negative tracking.
- White editorial canvases interrupted by deep green, dark navy, and image-led CTA bands.
- Rounded media cards and product cards, usually 8px to 22px.
- Pill CTAs in near-black or white, with most secondary actions rendered as underlined text links.
- Trust-logo strips with monochrome partner marks and very wide vertical spacing.
- Agent-console mockups using dark panels, small status chips, and product integration badges.
- Blog and research surfaces with prominent taxonomy chips, long rule-separated lists, and search fields.

## Colors

### Brand & Accent

- **Cohere Black** (`#000000`): Announcement bar, highest-contrast text, and the global brand anchor.
- **Near-Black Primary** (`#17171c`): Primary CTA buttons, dark footer, and deep UI cards.
- **Deep Enterprise Green** (`#003c33`): Product hero bands for North and Command-style dark sections.
- **Dark Navy** (`#071829`): Financial-services and security-oriented solution bands.
- **Action Blue** (`#1863dc`): Editorial links, pagination, and secondary action emphasis.
- **Coral** (`#ff7759`): Blog category chips, taxonomy outlines, and warm product markers.
- **Soft Coral** (`#ffad9b`): Pale chip borders and segmented article-label details.

### Surface & Background

- **Canvas White** (`#ffffff`): Dominant page background and form/card surface.
- **Soft Stone** (`#eeece7`): Product cards, testimonial placeholders, and warm neutral surface blocks.
- **Pale Green Wash** (`#edfce9`): North page section backdrop behind stacked dark capability panels.
- **Pale Blue Wash** (`#f1f5ff`): Blog CTA surface behind abstract 3D imagery.
- **Card Border** (`#f2f2f2`): Softest card containment line.

### Text & Rules

- **Ink** (`#212121`): Default body text and most link text on light backgrounds.
- **Muted Slate** (`#93939f`): Decorative and large-label use only — dates, de-emphasized labels and footer microcopy at 18px+. It measures 3.04:1 on `{colors.canvas}` and 2.71:1 on `{colors.card-border}`, so it is below AA for 16px body copy. Use `{colors.body-muted}` (6.19:1 on canvas) for any secondary text at body size.
- **Slate** (`#75758a`): Research separators and tertiary text.
- **Hairline** (`#d9d9dd`): Decorative rules only — list separators and section dividers inside otherwise high-contrast layouts. At 1.41:1 on `{colors.canvas}` it is not a usable component boundary.
- **Hairline Strong** (`#75758a`): *Prescribed, not extracted.* Parallel accessible boundary at the Slate value, for any border that is the only thing defining a control: text inputs, select fields, outlined pills and table cells. Measures 4.50:1 on `{colors.canvas}`.
- **Border Light** (`#e5e7eb`): Secondary divider and utility rule, decorative only (1.24:1 on canvas).

### Semantic

- **Focus Blue** (`#4c6ee6`): Keyboard focus ring on every light surface this file defines — `{colors.canvas}`, `{colors.card-border}`, `{colors.soft-stone}`, `{colors.pale-green}`, `{colors.pale-blue}`.
- **Focus On Dark** (`#ffad9b`): *Prescribed, not extracted.* Focus ring drawn on the dark product bands, where Focus Blue falls to 2.76:1 on `{colors.deep-green}`. Taken from the brand's existing Soft Coral so the ring stays Cohere's, not a generic white outline.
- **Form Focus Violet** (`#9b60aa`): Focus border for text inputs, used together with the ring rather than instead of it.
- **Error Red** (`#b30000`): Extracted ring/shadow color associated with validation-like states.

### Gradient System

Cohere does not use gradients as a generic UI fill. Gradients and color fields are media-led: abstract 3D hero imagery, deep blue open-science particle fields, red-orange product video posters, and dark green-to-black product environments. Keep UI surfaces flat; reserve gradient richness for large media panels and CTA image bands.

## Typography

### Font Family

- **Display**: `CohereText`, falling back to `Space Grotesk`, `Inter`, `ui-sans-serif`, and `system-ui`.
- **Body/UI**: `Unica77 Cohere Web`, falling back to `Inter`, `Arial`, `ui-sans-serif`, and `system-ui`.
- **Technical labels**: `CohereMono`, falling back to `Arial`, `ui-sans-serif`, and `system-ui`.
- **Icons**: Cohere uses custom icon fonts and thin-line geometric illustrations.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|---|---|---:|---:|---:|---:|---|
| Hero Display | CohereText | 96px | 400 | 1.00 | -1.92px | Home page declaration scale. |
| Product Display | CohereText | 72px | 400 | 1.00 | -1.44px | Product and research hero headlines. |
| Section Display | Unica77 | 60px | 400 | 1.00 | -1.2px | Large product-page headings. |
| Section Heading | Unica77 | 48px | 400 | 1.20 | -0.48px | Split hero and CTA headings. |
| Card Heading | Unica77 | 32px | 400 | 1.20 | -0.32px | Feature card and list section titles. |
| Feature Heading | Unica77 | 24px | 400 | 1.30 | 0 | Cards, filters, and article titles. |
| Body Large | Unica77 | 18px | 400 | 1.40 | 0 | Lead text and larger paragraphs. |
| Body | Unica77 | 16px | 400 | 1.50 | 0 | Default copy and link text. |
| Button | Unica77 | 14px | 500 | 1.71 | 0 | Compact CTA labels. |
| Caption | Unica77 | 14px | 400 | 1.40 | 0 | Metadata and small explanatory text. |
| Mono Label | CohereMono | 14px | 400 | 1.40 | 0.28px | Uppercase technical labels. |
| Micro | Unica77 | 12px | 400 | 1.40 | 0 | Footer, nav microcopy, and small links. |

### Principles

- Use massive type sparingly; Cohere pages often have one oversized headline and then settle into restrained 16px-24px UI copy.
- Keep display type tight. Hero copy should feel compact and carved, not airy.
- Avoid heavy bold weights. Size, spacing, and surface contrast do most of the hierarchy work.
- Use uppercase mono labels for category and system markers, especially on product and research pages.
- Editorial pages can use coral chips and blue links, but the base typography remains black and measured.

## Layout

### Spacing System

The system uses an 8px base with many one-off alignment values: `2px`, `6px`, `8px`, `10px`, `12px`, `16px`, `20px`, `22px`, `24px`, `28px`, `32px`, `36px`, `40px`, `56px`, `60px`, `64px`, and `80px`.

Large sections rely on dramatic vertical breathing room. The home page places a trust-logo strip far below the hero media. Product pages often hold dark panels inside fields of empty white space, then transition to dense forms or footers only near the end.

### Grid & Container

- Global nav uses a three-zone layout: logo left, menu centered, sign-in/CTA right.
- Home hero is centered text above a two-card media composition: a wide product mockup card beside a narrower photography card.
- Feature sections commonly use 3-column cards on desktop.
- Product pages alternate centered hero blocks, trust-logo strips, large single-feature bands, and 2- or 3-column card grids.
- Research pages use full-width lists with date and chip columns instead of decorative cards.
- Forms use two-column input rows inside a rounded white card on dark or stone section backgrounds.

### Whitespace Philosophy

Cohere uses whitespace as a trust signal. Large empty intervals separate the brand claim, customer proof, product proof, and CTA. Dense content appears only where it serves the information architecture: research paper rows, blog card grids, and contact form fields.

## Elevation & Depth

Cohere is mostly flat. Depth comes from surface alternation, media contrast, rounded corners, and thin borders rather than drop shadows. Elevation is expressed one way throughout — a 1px border plus a surface change — and never as a shadow, so there is no `shadow:` token group in this file.

The light layers are deliberately close together: `{colors.card-border}` sits at 1.12:1 against `{colors.canvas}` and `{colors.soft-stone}` at 1.18:1. Layer separation therefore comes from the border, not from the fill, which is why a card that must read as a container uses `{colors.hairline-strong}` rather than `{colors.card-border}` alone.

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, white or dark field | Hero copy, research lists, editorial surfaces |
| Bordered | 1px `{colors.hairline}` or `{colors.border-light}` for decorative rules; 1px `{colors.hairline-strong}` wherever the border is the control's only boundary | Research rows, forms, pale cards, footer inputs |
| Media Lift | Rounded image or video over contrasting section color | Hero photo cards, product videos, CTA imagery |
| Dark Product Field | Deep green or navy full-width band | Command, North, financial services, security sections |

## Shapes

### Radius Scale

| Token | Value | Role |
|---|---:|---|
| `xs` | 4px | Small images, search fields, article thumbnails, utility elements |
| `sm` | 8px | Blog chips, cards, small media, dialogs |
| `md` | 16px | Medium product cards and grouped blocks |
| `lg` | 22px | Signature media-card and soft placeholder radius |
| `xl` | 30px | Research/topic filter pills |
| `pill` | 32px | Primary CTA buttons |
| `full` | 9999px | Round status elements and fully pill-shaped controls |

### Image Treatment

Images are not decorative backdrops for text except in CTA bands. Most imagery sits as rounded cards with visible corners: product videos, enterprise photography, article thumbnails, and abstract 3D renders. The dominant radii are 8px and 22px.

## Components

### **`button-primary`**

Near-black or white pill CTA, depending on surface contrast. Uses 14px-16px Unica77, 12px 24px padding, and a 32px pill radius. This is the primary action style for "Request a demo", "Submit", and hero CTAs.
- **States:** default, hover (`{colors.ink}` fill), focus-visible (2px `{colors.focus-blue}` ring with a 2px canvas offset; `{colors.focus-on-dark}` when the button sits on a dark band), active/pressed, disabled (fill drops to `{colors.hairline}` with `{colors.muted}` label), loading (label replaced by an in-place spinner, button footprint unchanged). No selected or error state.

### **`button-secondary`**

Text-only action link, usually underlined or rule-aligned, with no filled background. Used for "Explore products", "Try the Playground", newsletter signup, and secondary hero actions.
- **States:** default, hover (underline thickens), focus-visible (`{colors.focus-blue}` ring around the text box), active/pressed, disabled (`{colors.muted}` label, underline removed). No loading, selected or error state.

### **`button-pill-outline`**

Outlined pill control with transparent fill, 1px dark border, and 30px radius. Used for research filters, topic tags, and lightweight taxonomy controls.
- **States:** default, hover (border moves to `{colors.hairline-strong}`), focus-visible, active/pressed, selected (inverts to `{colors.primary}` fill with `{colors.on-primary}` label), disabled. No loading or error state.

### **`announcement-bar`**

Full-width black strip above the nav, 36px tall, centered microcopy with an underlined "Learn more" link and a close control at the far right.
- **States:** two only — default and dismissed. The inline link and the close control each carry hover, focus-visible (`{colors.focus-on-dark}` ring) and active/pressed.

### **`hero-photo-card`**

Rounded media card used in the home hero and solution pages. It combines photography or abstract imagery with an overlaid dark agent-console module. Radius is usually 22px on large cards and 8px on smaller thumbnails.
- **States:** default only when the card is static media. Where it wraps a link it adds hover and focus-visible; there is no disabled, selected, loading or error state.

### **`agent-console-card`**

Dark product mockup panel showing agent names, status chips, integration badges, prompt fields, and generated response cards. Background is near-black, text is white or muted, and small accent chips use product colors.
- **States:** default and loading (skeleton rows in place of generated response cards). This is a product mockup, not an interactive control, so it has no hover, focus-visible, active/pressed, disabled, selected or error state of its own.

### **`trust-logo-strip`**

Centered copy above a row of monochrome customer logos. It is intentionally quiet: no cards, no borders, just large horizontal spacing and black or white logos depending on the background.
- **States:** default only. Non-interactive; the logos are not links in the documented layout.

### **`capability-card`**

Content block with thin-line geometric illustration, 24px heading, body copy, and a text link. On light backgrounds, cards often have only a top rule or a subtle image/card relationship rather than full boxing.
- **States:** default, hover (text link underline appears), focus-visible on the link rather than the card. No active/pressed, disabled, loading, selected or error state.

### **`dark-feature-band`**

Deep green or navy full-width section used for product capabilities, security claims, and feature breakdowns. Text turns white; cards use darker translucent surfaces, pale borders, and abstract line illustrations.
- **States:** default only — a layout band, not a control. Controls placed inside it inherit `{colors.focus-on-dark}` for focus-visible.

### **`product-card`**

Warm stone card used for product/model summaries. Typically 3-column on desktop, with 8px radius, generous padding, a small pill button, a divider line, and checkmark bullet rows.
- **States:** default and hover (border moves to `{colors.hairline-strong}`). Its pill button carries the full `button-primary` state set, including focus-visible, active/pressed, disabled and loading; the card itself has no selected or error state.

### **`blog-filter-chip`**

Large coral taxonomy chip used on the blog index. Active chips invert to coral fill with dark text; inactive chips use coral outline and pale fill. Typography is oversized relative to typical filters, making the taxonomy a hero-level control.
- **States:** default (coral outline, pale fill), hover, focus-visible, active/pressed, selected (coral fill with dark text), disabled (`{colors.coral-soft}` outline, `{colors.muted}` label). No loading or error state.

### **`research-table`**

Rule-separated publication list with title left, topic pills centered, and date right. Rows are tall, white, and border-driven; filters above use many compact outlined pills.
- **States:** row default, hover (row tint), focus-visible on the row link, and loading (rule-separated skeleton rows). Rows have no active/pressed, disabled, selected or error state; the filter pills above use `button-pill-outline` states, selected included.

### **`contact-form-card`**

Rounded white form panel set against dark green or warm stone sections. Inputs are rectangular with thin gray borders, 12px-16px padding, and compact labels/placeholders. Submit uses the same near-black pill style as primary CTAs.
- **States:** per input — default (1px `{colors.hairline-strong}` boundary), hover, focus-visible (`{colors.form-focus}` border plus the `{colors.focus-blue}` ring), disabled, and error (`{colors.error}` border with a message in `{colors.error}`, never colour alone). Submit carries the `button-primary` set including active/pressed and loading. No selected state.

### **`footer-newsletter`**

Dark footer subscription block with coral "AI moves fast" label, white headline, muted legal microcopy, a single-line email field, and arrow submit marker. Footer columns use white section labels and muted links.
- **States:** email field default, hover, focus-visible (`{colors.focus-on-dark}` ring on the dark footer), error (`{colors.error}` message under the field) and disabled; the arrow submit adds active/pressed and loading. No selected state.

## Motion & Animation

**This motion system is prescribed to match the brand's visual identity and was not measured from the live site.** No timing function, duration or curve below was extracted from Cohere's pages; they are derived from the **Crisp** profile, chosen because this is an enterprise AI tool interface whose own description is "sober", whose display weight is 400, and whose UI shell is deliberately free of decorative chrome. State change should read as instant; there is no entrance choreography.

All values reference the `motion:` token group. Only `transform` and `opacity` are animated. `width`, `height`, `top`, `left` and `margin` are never animated. Every exit is shorter than its matching entrance.

| Interaction | Duration | Easing | Property | Reduced-motion behaviour |
|---|---|---|---|---|
| Hover (buttons, chips, rows, links) | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity`; `transform: scale(1.01)` on pill CTAs only | Colour and opacity change at `{motion.duration-reduced}`; no scale |
| Press / active | `{motion.duration-instant}` | `{motion.ease-standard}` | `transform: scale(0.98)` | No transform; opacity step at `{motion.duration-reduced}` |
| Focus-visible ring | `{motion.duration-instant}` | `{motion.ease-standard}` | `opacity` on the ring layer | Ring appears at `{motion.duration-reduced}`, never instantly suppressed |
| Page / route transition | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` in, `{motion.ease-exit}` out | `opacity` only; no travel, so the hero declaration is never delayed | Cross-fade at `{motion.duration-reduced}` |
| Modal / drawer | `{motion.duration-base}` in, `{motion.duration-fast}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` plus `transform: translateY(8px)` in, scrim `opacity` | Opacity only at `{motion.duration-reduced}`; no translate |
| Dropdown (nav menu, filter menu) | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` plus `transform: translateY(4px)` | Opacity only at `{motion.duration-reduced}` |
| Toast | `{motion.duration-fast}` in, `{motion.duration-instant}` out | `{motion.ease-enter}` / `{motion.ease-exit}` | `opacity` plus `transform: translateY(6px)` | Opacity only at `{motion.duration-reduced}`; auto-dismiss timing unchanged |
| List enter (research rows, blog cards) | `{motion.duration-fast}` per item, `{motion.stagger-step}` between items | `{motion.ease-enter}` | `opacity` only — no stagger-driven travel, per the Crisp signature | Stagger dropped; one fade at `{motion.duration-reduced}` for the whole list |
| List exit (filter change) | `{motion.duration-instant}` | `{motion.ease-exit}` | `opacity` | Fade at `{motion.duration-reduced}`, no stagger |
| Loading (skeletons, button spinner) | `{motion.duration-emphasis}` loop | `{motion.ease-standard}` | `opacity` pulse on skeletons; `transform: rotate()` on the spinner | Spinner rotation frozen; skeletons hold a static mid-opacity fill and progress is announced in text |

Cohere has no brand ambience loop in this system. The only infinite animations permitted are the loaders above.

```css
@media (prefers-reduced-motion: reduce) {
  /* Removed: all travel and scale — translateY on modal, drawer, dropdown and
     toast; scale on hover and press; the list-enter stagger; spinner rotation. */
  /* Kept: opacity fades, capped at {motion.duration-reduced} (100ms), so focus
     rings, toasts and validation messages still announce themselves. */
  /* Frozen: skeleton pulses hold a static fill; loading progress is conveyed in text. */
}
```

## Accessibility

### Measured contrast

Every ratio here is computed with WCAG 2.1 relative luminance from the hexes in this file's own frontmatter.

| Foreground / Background | Ratio | Required | Result |
|---|---:|---:|---|
| `{colors.ink}` on `{colors.canvas}` | 16.10:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.card-border}` | 14.38:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.soft-stone}` | 13.64:1 | 4.5:1 | Pass |
| `{colors.body-muted}` on `{colors.canvas}` | 6.19:1 | 4.5:1 | Pass |
| `{colors.on-primary}` on `{colors.primary}` | 17.86:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.deep-green}` | 12.40:1 | 4.5:1 | Pass |
| `{colors.on-dark}` on `{colors.dark-navy}` | 17.92:1 | 4.5:1 | Pass |
| `{colors.action-blue}` on `{colors.canvas}` | 5.44:1 | 4.5:1 | Pass |
| `{colors.ink}` on `{colors.coral}` | 6.16:1 | 4.5:1 | Pass |
| `{colors.hairline-strong}` on `{colors.canvas}` | 4.50:1 | 3.0:1 | Pass |
| **`{colors.muted}` on `{colors.canvas}`** | **3.04:1** | 4.5:1 | **Fail — real brand value, disclosed below** |
| **`{colors.muted}` on `{colors.card-border}`** | **2.71:1** | 4.5:1 | **Fail — real brand value, disclosed below** |
| **`{colors.hairline}` on `{colors.canvas}`** | **1.41:1** | 3.0:1 | **Fail — real brand value, disclosed below** |
| `{colors.border-light}` on `{colors.canvas}` | 1.24:1 | 3.0:1 | Fail — decorative rule only |
| `{colors.coral}` on `{colors.canvas}` | 2.61:1 | 3.0:1 | Fail — chip fill and outline, never text |

### Where the real brand fails AA

These are extracted values and have not been altered; the honest statement is more useful than a falsified hex.

- **`{colors.muted}` (`#93939f`) fails AA for body text.** 3.04:1 on `{colors.canvas}` and 2.71:1 on `{colors.card-border}`, against 4.5:1. It is defensible only at 18px+ regular or 14px+ bold, where the 3:1 large-text threshold applies — and even then it fails on `{colors.card-border}` and `{colors.soft-stone}` (2.57:1). Use `{colors.body-muted}` for secondary text at body size.
- **`{colors.hairline}` (`#d9d9dd`) fails the 3:1 boundary threshold.** 1.41:1 on `{colors.canvas}`. It is a decorative separator between high-contrast content, not a control boundary. Where a border is the only thing defining a control, use `{colors.hairline-strong}`.
- **`{colors.coral}` (`#ff7759`) fails 3:1 against white** at 2.61:1, so a 1px coral outline is not a sufficient boundary on its own; `blog-filter-chip` pairs it with a pale fill and a text label, and the selected state inverts to a coral fill with `{colors.ink}` text at 6.16:1.
- `{colors.border-light}` (`#e5e7eb`, 1.24:1) is a utility rule only, by the same rule as `{colors.hairline}`.

### Focus ring visibility on every surface this file defines

Two rings, because one cannot serve both polarities: `{colors.focus-blue}` at 2.76:1 on `{colors.deep-green}` would be invisible on the product bands.

| Surface | Ring token | Ratio | Required |
|---|---|---:|---:|
| `{colors.canvas}` | `{colors.focus-blue}` | 4.49:1 | 3.0:1 |
| `{colors.card-border}` | `{colors.focus-blue}` | 4.01:1 | 3.0:1 |
| `{colors.pale-green}` | `{colors.focus-blue}` | 4.21:1 | 3.0:1 |
| `{colors.pale-blue}` | `{colors.focus-blue}` | 4.11:1 | 3.0:1 |
| `{colors.soft-stone}` | `{colors.focus-blue}` | 3.80:1 | 3.0:1 |
| `{colors.deep-green}` | `{colors.focus-on-dark}` | 6.91:1 | 3.0:1 |
| `{colors.primary}` | `{colors.focus-on-dark}` | 9.95:1 | 3.0:1 |
| `{colors.dark-navy}` | `{colors.focus-on-dark}` | 9.99:1 | 3.0:1 |
| `{colors.cohere-black}` | `{colors.focus-on-dark}` | 11.70:1 | 3.0:1 |

The ring is 2px with a 2px offset in the surface colour, drawn outside the control so the pill radius stays readable. Over the full-bleed hero and CTA photography, which has no measurable colour, the ring is drawn two-tone: `{colors.focus-on-dark}` with a 1px outer edge in `{colors.primary}`.

### Tap targets

Documented padding and type give `button-primary` a 12px + 24px box around a 14px/1.71 label, which computes to a 48px height, and the oversized `blog-filter-chip` and `button-pill-outline` filters clear the 44x44px minimum by design. The 36px `announcement-bar` close control does **not**: it needs its hit area extended to 44px without changing the visible 36px bar. Rendered tap-target size cannot be verified from a document, so this is a specification, not a measurement.

### Reduced motion

See the `@media (prefers-reduced-motion: reduce)` block above. All travel, scale, stagger and spinner rotation are removed; opacity fades remain, capped at `{motion.duration-reduced}` (100ms); skeleton pulses are frozen and loading progress is given in text.

### Other requirements

- Colour is never the only carrier of meaning: form errors pair `{colors.error}` with a text message, and `blog-filter-chip` selection inverts fill as well as colour.
- Display roles at 96px/72px with 1.00 line height and negative tracking must still reflow rather than clip at 200% zoom; this cannot be verified from a document.

## Do's and Don'ts

### Do

- Use white canvas as the default surface; introduce dark green or navy as full-width product bands.
- Keep primary CTAs pill-shaped and near-black on light surfaces.
- Use 22px radius on major media cards and placeholders.
- Use coral for editorial taxonomy and small warm accents, not as the main CTA system.
- Use monochrome trust logos with wide spacing.
- Use thin-line geometric illustrations for research and capability icons.
- Let photography and product mockups carry color, while the UI shell stays restrained.

### Don't

- Do not turn coral or blue into broad decorative surface colors.
- Do not add heavy drop shadows to cards.
- Do not make every section card-based; Cohere often uses unframed rows, rules, and open space.
- Do not use rounded cards below 8px for major media.
- Do not replace the display/body type split with one generic sans-serif voice.
- Do not render undocumented interaction variants in documentation or previews.
- Do not use saturated gradients as normal UI backgrounds; keep gradients media-led.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---:|---|
| Small Mobile | <425px | Single-column cards, compact nav, reduced hero headline scale |
| Mobile | 425-640px | Hero media stacks, card grids become one column, form rows stack |
| Large Mobile | 640-768px | Wider one-column layouts with larger media cards |
| Tablet | 768-1024px | Two-column cards begin, nav spacing tightens |
| Desktop | 1024-1440px | Full nav, 3-column card grids, split hero compositions |
| Large Desktop | 1440-2560px | Wide containers and large empty vertical intervals |

### Touch Targets

Primary CTAs and pills meet comfortable touch sizing through 12px-24px padding and pill radii. Research filter chips and blog category chips are larger than standard tags, making dense taxonomy surfaces usable on touch devices.

### Collapsing Strategy

- Nav collapses from full horizontal links to a compact mobile menu.
- Hero media moves from split cards to stacked cards.
- Product and capability grids collapse from 3 columns to 2 and then 1.
- Form fields collapse from paired rows to a single column.
- Research rows preserve their rule-separated structure but stack metadata below titles on smaller widths.

## Iteration Guide

1. Start from a white canvas or a full-width dark green/navy band; avoid mid-tone page backgrounds unless the screenshot shows a specific CTA/form section.
2. Use `button-primary` for the single highest-priority action and `button-secondary` for the companion action.
3. Use `hero-photo-card` or `agent-console-card` when a page needs visual energy; avoid invented dashboard data.
4. For editorial pages, combine `blog-filter-chip`, `button-pill-outline`, and `research-table` instead of generic marketing cards.
5. Keep component examples structurally honest: placeholder product frames are better than invented product content.

## Known Gaps

- Exact proprietary font files are not bundled; use the documented fallbacks when implementing externally.
- Mobile screenshots were not regenerated in this public update, so mobile behavior is documented from the desktop system and existing responsive patterns.
- Some live pages lazy-load content blocks late; blank testimonial placeholders are documented as placeholder skeleton surfaces rather than filled testimonial cards.
- The whole Motion & Animation section is prescribed from the Crisp profile, not extracted. No duration, easing curve or stagger in this file was measured from Cohere's live pages.
- Component states are specified rather than observed. The screenshots behind this file show default states only, so hover, focus-visible, active/pressed, disabled, loading, selected and error behaviour is a specification for implementers, not a record of the live site.
- `{colors.hairline-strong}` and `{colors.focus-on-dark}` are prescribed accessible tokens added alongside the extracted palette. Cohere's live pages were not observed using a visible focus ring, so the ring geometry, offset and the two-tone treatment over photography are specified, not measured.
- `{spacing.xs}` is 6px, off the documented 8px base; it is kept because the live system uses many one-off alignment values, listed under Layout. The radius ladder likewise carries 22px, 30px and 32px as three near-neighbours because all three are extracted, not because the scale is even.
- Tap-target size, overlap, clipping, frame rate and layout shift cannot be verified from a document. Every claim about them here is a specification.

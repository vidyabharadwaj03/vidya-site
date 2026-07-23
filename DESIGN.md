# Design

<!-- impeccable:design-schema 1 -->

## Direction (2026-07-23 redesign)

THESIS: An editorial index, not a scrapbook — the page reads like a well-set portfolio dossier, refusing the pastel/hand-drawn "cute personal site" default the previous version shipped.

OWN-WORLD: Warm off-white ground, near-ink text, a single confident clay/terracotta accent used sparingly (links, active states, one rule per row). Fraunces (serif) carries display type — name, section titles, entry titles. IBM Plex Sans carries everything else — nav, body copy, meta, labels — set with a touch of tracking on small caps labels. No hand-lettered script, no rotated photo frames, no bouncy easing, no colored card shadows.

STORY: A visitor scans a short, confident intro, then moves through numbered sections (echoing the ordered nav) rendered as flat, hairline-divided rows — projects, timeline entries, media mentions — each expandable for detail. Nothing is boxed in a shadowed card; hierarchy comes from type scale, weight, and spacing alone.

FIRST VIEWPORT: Sticky top nav with wordmark left, numbered section links right. Hero: large serif name, one plain-sans lede sentence, a single small "currently" line — no illustration, no floating decoration.

FORM: Reference-pinned by the user (ayushenagpal.com, varungangadharan.com) — restrained-neutrals-plus-one-accent color strategy, editorial numbered-index composition. Not a concept-tournament pick; brief pins the world.

## Palette

- `--bg` warm off-white (`#FAF7F3` light / `#1C1A18` dark)
- `--text` near-ink (`#211E1B` light / `#F3EFE9` dark) — 15.5:1 / 15.2:1 contrast
- `--text-muted` warm gray for secondary copy (`#6B6459` / `#A79E90`) — 5.5:1 / 6.6:1
- `--text-faint` warm gray for small meta (dates, tags, footer) (`#78716A` / `#94897A`) — held at ≥4.5:1 even at small sizes
- `--border` hairline warm gray, 1px only — no card shadows, no colored left-borders
- `--accent` single clay/terracotta (`#B5562F` light / `#E08256` dark, ≥4.5:1 both) — used for links, active nav state, numbered labels, hover. Nothing else carries color.

## Type

- Display: Fraunces 500/600, italic 500 for occasional emphasis — name, section titles, entry titles.
- Body/UI: native system sans stack (`-apple-system, "Segoe UI", Roboto, sans-serif`) — paragraphs, nav labels, buttons. Zero extra bytes, renders crisp and native rather than as one more custom webfont flourish; matches how both reference sites read.
- Meta/mono: IBM Plex Mono 400/500 — small tracked-out labels, numbered indices (`01`, `002`), dates, tags. Deliberate technical/editorial register, not a "technical" costume — used exactly where the reference sites use tracked mono meta text.
- No script/handwritten face. No gradient text. Emphasis via weight/size only.
- Dropped from the previous system (unused in the rebuild, removed from `build.py`'s font mapping): Nunito (all weights), Caveat (all weights), Source Serif 4 (`ssf*`). This also cuts the inlined font payload from ~545KB to ~177KB base64.

## Components

- **Numbered section system**: nav links and section headers share the same ordinal (`01 Projects`, `02 Education`, …) — a deliberate wayfinding device carrying real page-order information, not decoration.
- **Flat index rows**: projects, timeline, media render as `<details>` rows with a 1px top border, no radius, no shadow, no background fill. Expand affordance is a plain `+`/`−` or rotating hairline chevron, not a filled circle button.
- **Tags/meta**: plain small-caps Plex text, not pill-shaped chips with hover bounce.
- **Photos**: flat rectangular frames, thin 1px border, no rotation, no drop shadow.
- **Contact**: plain labeled text rows (`email` / `linkedin` / `github`), not colored pill buttons.

## Motion

- One entrance moment: fade + 12px translateY on scroll into view, `ease-out`, no bounce/overshoot easing anywhere.
- Hover states are color/underline only — no translateY bounce, no rotation.
- `prefers-reduced-motion` fully respected (already wired; keep it).

## Constraints carried over (unchanged)

- Single self-contained HTML file; `build.py` inlines fonts from `fonts/*.b64` into `index.template.html` → `index.html`. Edit the template, then rebuild.
- No external requests — fonts stay inlined as data URIs.
- Content stays data-driven from JS arrays; this redesign changes rendering/CSS only, not the underlying data shape or copy.
- `TIMELINE` placeholder entries stay unfilled — do not invent facts.

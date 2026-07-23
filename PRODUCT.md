# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

No single primary audience by design — this is a personal hub for whoever finds it: recruiters/employers as Vidya relocates to the Bay Area, potential Soraa collaborators or investors, policy/education contacts, press, and general network connections. The site is not optimized around one conversion funnel.

## Product Purpose

Vidya Bharadwaj's personal site: a single-page portfolio introducing her as a software engineer, founder (Soraa), technology-policy advocate, educator, and Bharatanatyam dancer. It exists to give any visitor an honest, complete picture of her work and interests in one place.

## Positioning

Deliberately no forced throughline. The user confirmed she does not want a compressed "builder who also does policy" narrative — the range of engineering projects, activism, education work, and dance should be presented on its own terms and let the work speak for itself.

## Operating Context

Single static HTML page (`index.template.html`) with these sections, in order: hero intro, "currently building" (Soraa spotlight), previous projects, education (UIUC), activism timeline, media mentions, hobbies/passions ("beyond"), contact links.

## Capabilities and Constraints

- Ships as one self-contained HTML file. `build.py` inlines base64-encoded font data from `fonts/` into `index.template.html` to produce `index.html`; edits belong in the template, and `index.html` must be regenerated (`python3 build.py`) after any change.
- Per `build.py`'s own comment, `index.html` is republished as a Claude Artifact — no external asset/font requests, no separate build pipeline beyond the font-inlining script.
- Content (projects, timeline, media, hobbies, social links) is data-driven from JS arrays (`SORAA`, `PREVIOUS_PROJECTS`, `DLAB_PROJECTS`, `TIMELINE`, `MEDIA`, `PASSIONS`, `SOCIAL_LINKS`, etc.) rendered client-side rather than hardcoded markup.
- Several `TIMELINE` entries carry an explicit `placeholder` string (e.g. Brooklyn Tech HS talk, Museum of Science Boston talk, Encode India Program, Project Puthri workshops) marking facts the user hasn't supplied yet (exact dates, institutions, counts, photos). These are known, deliberate gaps — never fabricate details to fill them.
- Visual style (palette, hand-drawn doodles, floating decorative words, motion) is **not** locked — the user confirmed she's open to changing it, so "cleaner" work may revise the visual world, not just tidy the existing one.

## Brand Commitments

Name: Vidya Bharadwaj. Contact: findvidyaonline@gmail.com, linkedin.com/in/vidyab03, github.com/vidyabharadwaj03. No other identity constraints confirmed as binding.

## Evidence on Hand

Real, already-authored content exists for: Soraa (current company, joinsoraa.com); five previous projects (MealMatch, BeMeal, Kode With Klossy, Northwestern research, IEEE PES Power Challenge) plus two D-Lab projects; UIUC coursework and academic work; a 15-entry activism timeline (GirlCon, Encode Justice, Reuters feature, Plan International USA, TeachAI, Code.org CSEdCon, RepuWhiz, Project Puthri, etc.) with real external links (Reuters, LinkedIn posts, podcast, press); 5 media mentions; 3 hobbies (Bharatanatyam, home café, running). Treat this as authoritative source content — do not invent testimonials, metrics, or events beyond what's written, and preserve the explicit `placeholder` markers noted above rather than inventing values for them.

## Product Principles

- Present breadth honestly rather than compressing into a single pitch or persona — no forced narrative arc across engineering, policy, and dance.
- Serve a general, undefined audience — don't over-optimize the page for one visitor type (e.g. purely recruiter-facing) at the expense of others.
- Preserve technical delivery constraints (single self-contained file, font-inlining build step, Artifact-publishable) through any redesign.
- Treat existing project/timeline/media content as real evidence to preserve and reorganize, not to rewrite or fabricate around — respect placeholders as open gaps, not omissions to invent.
- Visual identity is explicitly open for revision in service of "cleaner" — simplification can touch palette, decoration, and layout, not just spacing/polish.

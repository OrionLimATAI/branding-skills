---
name: dyna-presentation-design
description: Create or review Dyna.Ai PPT decks and slide visual systems using the official template.
---

# Dyna.Ai Presentation Design

Use this skill for Dyna.Ai PowerPoint, presentation, deck, slide, sales deck, pitch deck, company profile, webinar deck, and executive presentation work.

This skill is maintained by brand designers so non-design teammates can generate stronger slide visuals and deck structures with AI while still extending the official Dyna.Ai template.

Use `dyna-brand-foundation` for core brand rules. Use the existing `ppt-template-master` skill as the detailed template source when creating or rendering slides from the official Dyna.Ai 2026 Company Profile PPT template. Use `dyna-brand-reviewer` before external sharing or executive delivery.

## When to Use

Use for slide structure, deck outlines, slide specs, PPT visual direction, template extension, deck QA, sales decks, company profiles, executive presentations, webinar decks, and slide-by-slide rewrite or review.

## Required Inputs

- Deck objective, audience, slide count, content outline, source proof, CTA or next step, output format, whether the official Dyna.Ai PPT template must be extended, whether the user needs slide visuals or a document-like outline, and any legal or approval constraints
- If proof, metrics, client names, quotes, or financial claims are missing approval, mark them as placeholders rather than inventing content

## Output Contract

Use `dyna-brand-foundation/references/output-contracts.md`: return a Presentation / Deck Spec or slide visual direction with objective, audience, template source, slide structure, layout mapping, brand tokens, chart/table handling, image-generation-ready prompt structure when useful, claim risk, export notes, and review checklist.

## Template Source

Official presentation source: Dyna.Ai 2026 Company Profile PPT template.

When actual slide creation, PPTX editing, rendering, or visual QA is requested, load `ppt-template-master` and follow its layout mapping, typography, color, chart, icon, and slide rhythm rules.

Core template behavior:

- Canvas: `13.333 x 7.5 in`, equivalent to `1280 x 720`
- Typeface: `Poppins`
- Brand color: `#006CEE`
- Slide rhythm: cover, chapter dividers, white/light content pages, dark/gradient emphasis pages, ending slide
- Layout mindset: template extension, not redesign
- Geometry: use the approved template patterns; keep tables and dense content clean and readable
- Icons: one outline-based family when needed, used for scanning support rather than decoration

## Visual-First Deck Output

For slide visual work, prioritize:

- slide rhythm and page role
- template layout mapping
- visual hierarchy
- chart, table, or product module treatment
- proof and CTA placement
- image-generation-ready prompt structure when creating slide visuals or cover directions
- export readability for presentation and PDF use

Text outlines are useful only when they help a non-design teammate build or generate stronger slides.

## Collaboration Role

Use this skill as the primary skill for decks and slide systems. Bring in supporting skills when needed:

- `dyna-sales-enablement-design` for sales story, proof discipline, and buyer value
- `dyna-dashboard-design-guideline` for KPI slides, workflow diagrams, product console visuals, and data views
- `dyna-campaign-design` for campaign launch decks or KV-to-deck continuity
- `dyna-event-design-guideline` for webinar and event decks
- `dyna-brand-reviewer` before executive sharing or external distribution

## Slide Structure Rules

- Start with the story: audience, business problem, Dyna.Ai role, proof, and next step
- Map content to the closest official template layout before inventing a new slide structure
- Use chapter dividers for narrative transitions, not for dense content
- Use content pages for frameworks, tables, KPI views, product modules, and proof
- Use dark or gradient pages for executive statements, section summaries, or closing emphasis
- Keep each slide focused on one job

## Brand Language Rules

- Slide headlines should be short, specific, and provable
- Supporting copy should explain the business problem, product capability, or proof cue
- Avoid unsupported ROI, efficiency, compliance, risk-reduction, and deployment claims
- Do not invent customer names, quotes, metrics, logos, or endorsements
- Use clear CTAs such as request demo, contact sales, register, or discuss next steps

## Chart And Table Rules

- Use `#006CEE` as the lead series or key emphasis
- Use turquoise or light blue for supporting series
- Use yellow only for a sparse signal such as threshold, anomaly, or selected marker
- Right-align numeric columns and keep decimal precision consistent
- Keep chart labels readable in presentation view and PDF export

## Common Failures

- Treating the deck like a campaign poster instead of a presentation system
- Creating new slide styles when an official template layout fits
- Overloading slides with paragraphs
- Using unapproved metrics, quotes, customer names, or partner proof
- Making every page a card grid with the same rhythm
- Letting yellow or decorative gradients dominate the deck
- Returning only a text outline when the user needs slide visual direction

## Reviewer Handoff

Use `dyna-brand-reviewer` for final deck QA. Review:

- Dyna.Ai naming, `#006CEE`, `Poppins`, logo usage, and `0.5b` clear space
- Whether the deck extends the official PPT template
- Slide hierarchy, page rhythm, chart/table readability, and export readiness
- Claim boundary, proof level, customer approval, and CTA clarity

## Quality Check

Before finalizing:

1. The deck has a clear audience and business purpose
2. Slide structure follows the official template rhythm
3. Visual choices feel like Dyna.Ai, not a generic SaaS deck
4. Claims and proof are verified or clearly marked as placeholders
5. Charts, tables, and dense slides remain readable
6. Output is ready for PPT, PDF, or stakeholder review
7. A non-design teammate can use the output to create or generate slides without inventing layout decisions

---
name: dyna-social-digital-design
description: Create or review Dyna.Ai social and digital marketing visuals.
---

# Dyna.Ai Social And Digital Design

Use this skill for social and digital marketing assets where readability, channel fit, and fast brand recognition matter.

This skill is maintained by brand designers so non-design teammates can create stronger feed images, carousels, banners, EDM headers, and digital visuals with AI. For visual requests, the output should be ready to drive image generation or design execution.

Use `dyna-brand-foundation` for core brand rules when exact colors, type, logo, image style, or tone need to be checked.

Official source of truth: `Dyna.Ai socialmedia Guidelines.pdf`.

## When to Use

Use for LinkedIn posts, LinkedIn carousels, EDM headers, web banners, digital ads, webinar promos, thumbnails, YouTube/X covers, and partner social lockups.

## Required Inputs

- Platform, size, campaign or event name, audience, headline, CTA, logo/partner context, proof source, export target, and whether the result is for image generation or design handoff
- If platform size or crop behavior is unknown, state the assumption and preserve safe margins

## Output Contract

Use `dyna-brand-foundation/references/output-contracts.md`: return a visual direction or Design Spec with canvas, layout, logo clear space, typography, color tokens, copy hierarchy, proof level, CTA, metadata, export requirements, image-generation-ready prompt structure when needed, and handoff notes.

## Common Failures

- Text too small for feed viewing
- Partner lockup overpowering Dyna.Ai
- Yellow used as a theme instead of a signal
- EDM or cover graphics missing crop-safe spacing
- Returning a text-only post idea when the user needs a visual asset

## Reviewer Handoff

Use `dyna-brand-reviewer` for partner co-marketing, executive posts, campaign launches, paid ads, and any asset going outside the company.

## Supported Assets

- LinkedIn feed images
- LinkedIn document carousels
- Email and EDM headers
- Website promo banners
- Webinar promo images and recording covers
- Paid social or display ad statics
- Blog and insight thumbnails

## Design Goal

Digital assets should be:

- readable in a feed
- visibly Dyna.Ai at small sizes
- concise in message
- consistent across a campaign family
- polished enough for enterprise audiences
- structured enough that non-design teammates can generate or adapt them safely

## Visual-First Output

For social and digital visuals, prioritize:

- canvas size and safe area
- focal point and crop behavior
- headline size and line breaks
- logo and partner lockup placement
- proof cue and CTA position
- mobile feed readability
- export target and variant notes

Text guidance is useful only when it supports the asset's visual hierarchy and channel fit.

## Collaboration Role

Use this skill as the primary skill for channel-specific social and digital visuals. Bring in supporting skills when needed:

- `dyna-campaign-design` for master KV and campaign family consistency
- `dyna-event-design-guideline` for webinar and event promo structure
- `dyna-website-landing-design` for banner-to-landing continuity
- `dyna-sales-enablement-design` for sales-support social visuals
- `dyna-brand-reviewer` before paid, partner, or executive distribution

## Channel Defaults

Use official Dyna social templates when available. Use these formats unless the user provides a newer platform spec:

- LinkedIn square post: `1200 x 1200`
- Blog or insight cover: `1902 x 1066`
- EDM normal header: `1450 x 557`, usually no logo
- EDM special / large header: `1920 x 1080`, usually no logo
- Webinar cover: `1920 x 1080`
- LinkedIn, X, and YouTube covers: use the official socialmedia PDF templates and platform crop previews

Always preserve safe margins because platform crops vary.

## Social Color System

- Brand color: `#006CEE`
- Turquoise: `#00EDFF`
- Purple: `#A533FF`
- Yellow: `#FFE500`
- Light: `#E5F0FF`
- Black: `#000000`
- White: `#FFFFFF`

For general social backgrounds, use about `95%` blue family and `5%` secondary color, except special festivals and events. Do not let secondary colors become the dominant background.

Approved social gradients:

- `#006CEE -> #A1CCFF`
- `#006CEE -> #6FB5FF`
- `#6CEFEF -> #712FFF`
- `#00164E -> #006CEE`
- `#2A0087 -> #005CCC`
- `#1A2B6B -> #6F8BEF`
- `#1FA2FF -> #CCFCFF`
- `#ABCEFF -> #EEFEFF`
- `#CBE1FF -> #F7F1FF`

## Hierarchy Rules

Default hierarchy:

- Dyna.Ai logo or brand identifier
- headline
- supporting phrase or proof point
- CTA or event detail when needed
- speaker, date, partner, or product metadata when relevant

Limit the headline to a feed-readable length. Split long titles across lines rather than shrinking everything.

## Copy Rules

- Write for quick feed scanning: short headline, one clear proof cue, one next step.
- Prefer specific product, event, report, or business problem language over broad AI claims.
- Keep CTA copy concrete and visible.
- Do not invent urgency, metrics, customer proof, or partner endorsement.
- Reduce jargon unless the audience is technical and the term is necessary.

## Layout Patterns

Use one of these patterns:

- **Headline-led**: large statement, small proof, restrained brand graphic
- **Insight-led**: data point or quote as the focal point
- **Event-led**: title, date, speaker, CTA, and a simple visual field
- **Product-led**: cropped UI, workflow card, or product visual with headline
- **Carousel-led**: cover, section pages, proof pages, CTA close

Avoid placing all information at equal weight.

## Visual Rules

- Use Dyna.Ai brand color as the main CTA or active structure
- Keep backgrounds clean, light, dark, or template-derived
- Use turquoise for secondary emphasis
- Use yellow only for one attention marker
- Use icons sparingly and from one family
- Keep text contrast high on mobile screens
- Do not use tiny footnotes, dense paragraphs, or low-contrast metadata on feed images
- Do not use buzzword-heavy copy that requires explanation before the value is clear

## Logo And Lockup Rules

- Follow the `0.5b` clear-space rule from the brand guideline
- LinkedIn square and co-marketing template logo sizing should follow the socialmedia PDF's `1/4` logo reference
- Blog cover logo sizing should follow the socialmedia PDF's `1/6` logo reference
- Do not place the logo where profile crops, platform UI, or post overlays will cover it
- Social headers should be updated for major campaigns and product releases when relevant

For partner lockups:

- If the partner logo is a font logo, match or keep it within the Dyna.Ai logo's optical height according to the template type
- If the partner logo is a graphic logo, optically balance it and keep it from overpowering the Dyna.Ai mark
- Use the co-marketing template for partner social posts instead of inventing spacing

## Carousel Rules

For LinkedIn or document carousel-style assets:

- Page 1 should work as a standalone hook
- Each page should make one point
- Use repeated placement for logo, page number, and section title
- Use diagrams, charts, or short lists instead of paragraph blocks
- End with a clear CTA or takeaway

## Export Checks

Before finalizing:

1. Headline is readable at mobile feed size
2. Logo survives platform cropping
3. CTA and date details are not near unsafe edges
4. Text contrast passes visual inspection
5. Campaign variants share the same visual system
6. File naming clearly identifies platform, size, and version
7. A non-design teammate can use the output to generate the asset without guessing layout, crop, or hierarchy

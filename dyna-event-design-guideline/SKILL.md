---
name: dyna-event-design-guideline
description: Create or review Dyna.Ai event KVs, booth visuals, and vendor-ready event systems.
---

# Dyna.Ai Event Design Guideline

This skill helps create and review Dyna.Ai event branding materials. Use it for event-facing design systems, not for generic presentation styling. The goal is to keep event outputs consistent across KV design, billboard formats, booth materials, and vendor execution.

This skill is maintained by brand designers so non-design teammates can generate stronger event visuals and production-ready directions with AI. Text specs should support visual output and vendor execution, not replace the event visual system.

Use `dyna-brand-foundation` for core Dyna.Ai brand rules when exact color, typography, logo, image, or tone guidance is needed.

Official source of truth: `Dyna.Ai Event Guideline.pdf`.

## When to Use

Use for event guidelines, webinar covers, event KVs, billboards, booths, Dyna Day systems, customer visit materials, vendor specs, and production reviews.

## Required Inputs

- Event type, venue or platform, audience, format, canvas or booth size, required copy, CTA, production medium, output format, deadline, and vendor constraints
- Clarify whether the user needs a visual direction, AI image prompt, event guideline, or vendor checklist
- If vendor dimensions are unknown, state required confirmation before production

## Output Contract

Use `dyna-brand-foundation/references/output-contracts.md`: return a visual direction, Design Spec, or Vendor Checklist with dimensions, hierarchy, logo clear space, typography, color tokens, material or export notes, image-generation-ready prompt structure when useful, and proofing checks.

## Common Failures

- Title too small for viewing distance
- Missing Info or CTA in event KV
- Booth graphics designed without material, screen, or installation constraints
- Vendor files lacking ratio, resolution, or color mode
- Event request answered only as a text checklist when the user needs a KV, booth screen, or visual system

## Reviewer Handoff

Use `dyna-brand-reviewer` before vendor production. Treat production blockers as P0 and major readability issues as P1 using `review-rubric.md`.

## Use This Skill For

- Event design guidelines and brand manuals
- Exhibition and booth visual specs
- Dyna Day visual systems
- Customer visit and webinar branding
- Key visual and billboard structure rules
- Vendor checklists, file output standards, and production reviews

## Visual-First Event Output

For event visuals, prioritize:

- KV composition
- viewing-distance hierarchy
- logo / title / KV / info / CTA placement
- screen, billboard, or booth ratio
- physical material constraints
- lighting, crop, and installation risk
- image-generation-ready prompt structure when AI visuals are part of the workflow

Vendor specs are essential, but they should serve a clear event visual direction.

## Collaboration Role

Use this skill as the primary skill for event systems, booth visuals, webinar covers, and production-facing event assets. Bring in supporting skills when needed:

- `dyna-campaign-design` for campaign-led event themes and launch consistency
- `dyna-social-digital-design` for event promo posts, EDM headers, and webinar social assets
- `dyna-presentation-design` for event decks and speaker slides
- `dyna-office-environment-design` for customer visit or showroom-like physical environments
- `dyna-brand-reviewer` before vendor proofing or public release

## Core Brand Rules

- Brand name must be written as `Dyna.Ai`
- Overall style: modern, clean, tech-forward, minimal
- Prioritize whitespace, structure, and clear hierarchy
- Avoid clutter, decorative graphics, and trend-driven effects

## Color System

- Primary palette: Dyna.Ai brand color `#006CEE`, Black `#000000`, White `#FFFFFF`
- Secondary palette: Light Blue `#9ABCFF`, Event Yellow `#FFC62D`, Gray `#D0D1CE`
- Secondary colors are for small-scale highlights, functional emphasis, or information hierarchy only
- Recommended ratio: `70 / 20 / 10`
- Avoid uncontrolled multi-color compositions

## Typography

- Brand typeface: `Poppins`
- Use `Poppins` consistently across event branding and communication materials
- Do not introduce decorative or substitute brand fonts without approval
- Keep typography clean, readable, and consistent across materials

## Graphic Language

### Brand Symbol

- Use only approved brand symbol artwork
- Do not stretch, rotate, recolor, or alter its structure
- Maintain clear space around the symbol
- Use it as a structured brand element, not casual decoration

### Auxiliary Graphics

- Auxiliary graphics must derive from the brand symbol and brand language
- Use grids, lines, geometric blocks, and subtle tech-inspired patterns
- Keep them minimal and supportive
- Do not use unrelated decorative textures or abstract effects

## Key Visual Structure

The event KV system has two standard formats:

1. `Standard KV Layout Structure`
2. `Billboard Structure`

### Standard KV Layout Structure

- Default ratio: `16:9`
- Recommended size: `1920 x 1080 px`
- Recommended grid: `16 columns x 8 rows`
- Layout logic: `left content zone + right visual zone`

Every KV should include these five core elements:

- `Logo` - Brand identifier, positioned consistently
- `Title` - Event name or main message
- `KV` - Primary visual element or hero image
- `Info` - Essential event details such as date, time, and location
- `CTA` - Registration link or next step

Execution rules:

- Title is the primary message
- Info and CTA sit below the title in a clear vertical flow
- KV occupies the main visual field without reducing readability

### Billboard Structure

- Default common ratio: `3.4:1`
- Use `2:1` only when the venue, vendor, or media spec requires it
- Used for booth headers, fascia panels, long banners, and ultra-wide formats
- Follow the same brand hierarchy as the standard KV
- Simplify content for distance viewing
- Reduce `Info` and `CTA` when the format requires it

## Event Applications

### Exhibitions

- Large booth `36sqm+`: multi-layer architectural structure, large LED focal screen, dedicated demo zones, meeting areas, phone booths with soundproofing, storage room, and optional overhead suspended feature
- Standard booth `18-36sqm`: single main background wall, product demo area, reception counter, and phone booths with soundproofing when space allows
- Small booth `9sqm`: one strong KV display, minimal setup, essential branding only

Typical materials:

- Organize booth materials by type first: visual output, physical structure graphics, interactive and digital assets, and print materials
- Within each type, use `Purpose`, `Typical materials`, and `Size adaptation`
- Under `Size adaptation`, explain how the category scales across `Large Booth`, `Standard Booth`, and `Small Booth`
- Use formal guideline prose rather than tables when drafting manuals
- Keep small booth materials minimal: one strong KV, reception graphics, QR code, and only essential handouts
- For visual output materials, include concrete scale guidance: main KV screen is LED / 4K horizontal format; large booth background wall is typically `5-8m` wide; standard booth background wall is typically `3-5m` wide; small booth uses a single KV display; side wall visuals are for large booths only; theme slogan applies across all booth sizes

Material standards:

- Use premium materials such as lightbox fabric, UV printing, acrylic, and metal-based structures or finishes
- Reject cheap boards, low-resolution output, poor finishing quality, visibly low-grade materials, or materials that distort brand color under lighting

### Dyna Day

Typical zones:

- Registration zone
- Main hall
- Demo zone
- Media zone
- Atmosphere materials

Keep all zones visually linked through one KV system, one hierarchy, and one material language.

### Customer Visit

- Use a more restrained, hospitality-led visual tone
- Prioritize welcome screens, agenda graphics, guide signage, and gift packaging

### Webinar

- Keep digital assets readable across desktop and mobile
- Typical assets: webinar banner, EDM header, cover image, slides, countdown, recording end screen, social promo visuals

## File Output

- Print: `CMYK`
- Screen: `RGB`
- Print-ready files: `300 dpi`
- Large screens: confirm `4K` or `1080p` output requirements before delivery

## Vendor Review Checklist

Check the following before production:

- Logo is correct and undistorted
- Brand colors are accurate
- Fonts are consistent
- Title and KV are not cropped incorrectly
- Resolution and color mode match the output type
- Bleed is complete for print files
- Materials and dimensions match the approved order

## Writing Guidance

When drafting guidelines or specs with this skill:

1. Write in a professional, direct, corporate tone
2. Prefer short sections and high-signal bullets
3. Keep rules actionable for designers and vendors
4. Separate visual rules from production rules
5. Adapt structure to the event type, but keep brand logic consistent
6. Keep event copy specific to the event, audience, time, location, CTA, or proof; avoid broad AI claims on large-format assets

## Quality Check

Before finalizing, verify:

- `Dyna.Ai` naming is correct
- KV structure matches the intended format
- Typography follows `Poppins` rules
- Graphic language stays derived from the brand symbol
- The design feels structured and premium, not decorative
- A non-design teammate can understand what visual to generate or hand to a vendor before reading production details

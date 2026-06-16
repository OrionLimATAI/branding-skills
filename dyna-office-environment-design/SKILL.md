---
name: dyna-office-environment-design
description: Create or review Dyna.Ai office, showroom, and environment brand visuals.
---

# Dyna.Ai Office Environment Design

Use this skill for Dyna.Ai workplace and environmental brand applications: reception, showroom, office signage, meeting-room graphics, screen content, office supplies, ID cards, lanyards, bags, apparel, and branded workplace materials.

This skill is maintained by brand designers so non-design teammates can generate stronger office and showroom visuals with AI while still respecting material, installation, and vendor constraints.

Use `dyna-brand-foundation` for core brand rules.

Official source of truth: `Dyna.Ai Brand Guideline - Office.pdf`.

## When to Use

Use for reception, showroom, office signage, meeting-room graphics, screen content, office supplies, ID cards, lanyards, bags, apparel, and workplace brand materials.

## Required Inputs

- Site or item type, dimensions, material, viewing distance, production method, logo placement, editable fields, output format, and vendor or installer constraints
- Clarify whether the user needs a visual direction, screen asset prompt, vendor checklist, or production review
- If site measurements are unknown, request confirmation before final production specs

## Output Contract

Use `dyna-brand-foundation/references/output-contracts.md`: return a visual direction, Design Spec, or Vendor Checklist with purpose, dimensions, material, logo clear space, typography, color checks, file format, image-generation-ready prompt structure when useful, and installation risks.

## Common Failures

- Logo too small, distorted, or too close to edges
- Office item treated like a campaign graphic
- Missing material, installation, or durability notes
- ID, lanyard, or apparel files missing editable field guidance
- Screen or showroom request answered only as text when the user needs a visual direction

## Reviewer Handoff

Use `dyna-brand-reviewer` before vendor proofing, production, installation, or office rollout.

## Supported Applications

- corporate reception
- showroom and demo area graphics
- horizontal and vertical display screens
- roll-up and promotional materials
- entrance guidance and wayfinding
- meeting room door stickers
- meeting room wall stickers
- anti-collision stickers
- office slogans
- notebooks, pens, letterheads, envelopes, and business cards
- office ID cards and lanyards
- paper bags and canvas bags
- polo shirts and T-shirts

## Core Principles

- Dimensions are site-specific and must be adapted to the actual office environment
- Preserve Dyna.Ai logo clarity and premium material quality
- Use primary brand colors for large brand presence
- Use auxiliary colors decoratively, not as large-area replacements for the primary palette
- Keep physical applications clean, durable, and easy to maintain
- Keep workplace copy short, specific, and appropriate for physical viewing distance

## Visual-First Environment Output

For office and showroom visuals, prioritize:

- the physical context and viewing distance
- logo scale and placement
- screen or material dimensions
- surface color and finish
- content density for the viewing moment
- vendor feasibility
- image-generation-ready prompt structure when the output is a screen KV, showroom visual, or environmental mockup

Text specs should help non-design teammates generate or brief an environment visual without guessing the physical constraints.

## Collaboration Role

Use this skill as the primary skill for office, showroom, signage, and workplace material visuals. Bring in supporting skills when needed:

- `dyna-event-design-guideline` for customer visits, temporary exhibition-like zones, and large-format viewing rules
- `dyna-social-digital-design` for screen assets adapted from campaign or social visuals
- `dyna-presentation-design` for showroom screens that extend the official presentation system
- `dyna-brand-reviewer` before vendor production or office rollout

## Reception

- Reception logo represents Dyna.Ai and should be treated as a primary brand moment
- Recommended fabrication: solid acrylic and backlit logo
- Minimum installation floor clearance: `1700mm`
- Confirm wall material, lighting, viewing distance, and installation constraints before production

## Showroom Screens

Default screen specs from the Office guideline:

- `75in` horizontal screen: `3840 x 2160px`
- conference room projection standby screen: `3840 x 2160px`
- `32in` or `43in` vertical screen: `1080 x 1920px`
- vertical product display: `1080 x 1920px`
- vertical standby or business-card image: `1080 x 1920px`

Theme activity KVs and product displays must be adapted to the local theme, product, colleague, or region rather than reused blindly.

## Promotional Materials

- Roll-up size: `80 x 200cm`
- Keep roll-up hierarchy simple: logo, headline, proof or visual, and CTA/contact when needed
- Avoid dense paragraphs, tiny QR codes, or low-resolution product imagery

## Signage

Use signage for:

- elevator-door entrance guidance
- office entrance direction guidance
- wooden-door meeting room stickers
- glass-door meeting room stickers
- glass-wall meeting room graphics
- anti-collision stickers

Wayfinding can be adjusted according to actual site conditions, but the logo, color, and typography rules should not be improvised.

## Office Supplies And Apparel

- ID card and lanyard templates should allow editable photo, name, and title
- Install and use `Poppins` before editing office ID or lanyard files
- Keep apparel and bag designs simple, brand-led, and production-friendly
- For paper bags, canvas bags, polos, and T-shirts, prioritize logo clarity, material color, print method, and durability

## Review Checklist

Before finalizing:

1. Dimensions match the real site, screen, or product spec
2. Logo is correct, clear, and not distorted
3. Primary colors dominate large applications
4. Auxiliary colors are decorative and controlled
5. Screen assets match required pixel dimensions
6. Print and fabrication methods support premium quality
7. Editable fields such as name, title, photo, and local contact details are clearly identified
8. Final files are ready for vendor execution or local office adaptation
9. A non-design teammate can understand the intended visual result before sending files to a vendor

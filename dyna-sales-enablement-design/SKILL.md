---
name: dyna-sales-enablement-design
description: Create or review Dyna.Ai sales visuals, onepages, and sales enablement materials.
---

# Dyna.Ai Sales Enablement Design

Use this skill for Dyna.Ai sales-facing visuals and sales enablement materials that help commercial teams explain, prove, and sell solutions.

This skill is maintained by brand designers so non-design teammates can create stronger sales visuals, onepage images, and structured sales assets with AI. For visual requests, do not stop at a document-style brief when the real need is an image, onepage, hero visual, or page-ready composition.

Use `dyna-brand-foundation` for core brand rules. Use `dyna-presentation-design` when the output is a PowerPoint deck, sales deck, pitch deck, webinar deck, company profile, or slide-based business document based on the official PPT template.

Use `Dyna.Ai Brand Visual Identity Guidelines .pdf` for print color, logo, typography, and brand symbol rules. Use `dyna-office-environment-design` when the asset is an office, showroom, giveaway, apparel, ID, lanyard, bag, or environmental item rather than a sales asset.

## When to Use

Use for sales visuals, onepage PNGs, solution visuals, product-story images, proposal visual pages, one-pagers, solution briefs, datasheets, brochures, case studies, whitepapers, partner briefs, and sales leave-behind PDFs.

## Design Intent

This skill should help non-design teammates produce sales-facing assets that feel:

- commercially persuasive
- visually structured
- proof-led and credible
- consistent with Dyna.Ai
- ready to drive image generation or page generation when the final deliverable is visual

Text is support. Visual quality is the goal when the request is image-first or page-first.

## Delivery Tracks

Choose one of two tracks before structuring the output.

### Visual Track

Use when the final deliverable is:

- onepage PNG
- `9:16` onepage visual
- solution visual
- product-story image
- sales support static visual
- page-ready sales visual for web generation

For this track, prioritize:

- visual direction
- image-generation-ready prompt structure
- content hierarchy
- proof placement
- CTA placement
- layout modules
- readability and claim guardrails

### Document Track

Use when the final deliverable is:

- one-pager PDF
- solution brief
- datasheet
- brochure
- whitepaper
- leave-behind document

For this track, prioritize:

- scan-friendly structure
- section logic
- proof handling
- compliance and claim safety
- handoff clarity for design, sales, or vendor reuse

## Required Inputs

- Buyer, industry, solution, pain point, proof source, CTA, distribution context, output format, and legal or approval constraints
- Clarify whether the deliverable is visual-first or document-first
- If customer proof is not approved, anonymize and mark placeholders for client confirmation

## Output Contract

Use `dyna-brand-foundation/references/output-contracts.md`, but adapt the output to the track:

- **Visual Track**: return visual direction, image-generation-ready prompt structure, hierarchy, modules, proof handling, CTA, and readability guardrails
- **Document Track**: return a Brand Brief or Design Spec with buyer problem, solution, capabilities, outcomes, proof handling, claim risk, CTA, and export requirements

## Common Failures

- Invented metrics, client names, quotes, or case details
- Visual request answered with a document-like page instead of a high-quality visual
- Visual that lacks buyer logic, proof, or CTA
- Document that looks like a poster instead of a sales tool
- Capability list without buyer outcome
- Missing CTA or next sales step

## Reviewer Handoff

Use `dyna-brand-reviewer` before sales distribution, partner sharing, client meetings, external PDF export, or image/page release.

## Supported Materials

- sales onepage PNG
- `9:16` onepage visual
- solution visual
- product-story image
- sales support static visual
- one-pager
- solution brief
- product datasheet
- brochure
- case study
- whitepaper
- partner brief
- proposal visual pages
- sales leave-behind PDF
- executive summary document

## Design Goal

Sales assets should be:

- fast to scan
- specific to buyer needs
- proof-led and commercially credible
- visually aligned with Dyna.Ai
- easy for non-design teammates to generate with stronger structure
- easy for sales teams to reuse without redesign

## Collaboration Roles

When a sales visual needs more than commercial structure, call supporting scene skills deliberately.

- `dyna-sales-enablement-design`
  - buyer value
  - business story
  - proof discipline
  - CTA direction
  - claim safety
- `dyna-dashboard-design-guideline`
  - product credibility
  - KPI / workflow / status semantics
  - operational module patterns
  - product-console structure
- `dyna-website-landing-design`
  - hero composition
  - first-screen hierarchy
  - CTA rhythm
  - proof-above-the-fold logic

If the output must feel like a real product-driven sales visual, do not rely on this skill alone. Route through this skill as the primary commercial layer, then bring in dashboard and landing logic as supporting structure.

## Visual Track Structure

For onepage visuals and sales images:

- brand band or top context
- hero headline with one clear value proposition
- short supporting copy tied to buyer pain
- proof strip with up to 3 strong proof points
- 2 to 4 compact modules for capability, workflow, governance, or product evidence
- one clear CTA zone
- supporting labels only where they improve meaning and credibility

For `9:16` onepage compositions, compress aggressively. Do not try to fit an entire PDF page into a portrait canvas.

## Document Track Structure

For one-pagers and solution briefs:

- title and short value proposition
- audience or industry fit
- problem / market pressure
- Dyna.Ai solution summary
- key capabilities
- business outcomes
- proof points, metrics, or case evidence
- implementation or integration cues
- CTA and contact block

For case studies:

- client context or anonymized segment
- challenge
- Dyna.Ai approach
- solution modules
- measurable outcomes
- quote or executive takeaway when available
- reusable CTA

For datasheets:

- product or module name
- what it does
- core capabilities
- integrations or architecture notes
- security, compliance, or deployment cues
- use cases
- CTA

## Onepage PNG Case Rule

Use this as a routing lesson.

If the goal is a high-quality onepage PNG and the visual needs:

- commercial persuasiveness
- product credibility
- first-screen marketing rhythm

then do not use document-only sales logic.

Route as:

1. `dyna-sales-enablement-design` as the primary skill for buyer value, proof, and CTA
2. `dyna-dashboard-design-guideline` for KPI/workflow/status/product surface
3. `dyna-website-landing-design` for hero, proof rhythm, and CTA hierarchy

This case exists because an older document-first version of this skill could lead non-design teammates toward outputs that looked more like sales briefs than premium visuals.

## Layout Rules

- Use clear hierarchy and strong section labels
- For Visual Track, optimize for composition first and document logic second
- For Document Track, keep pages document-like rather than poster-like
- Use tables for technical comparisons and feature matrices only when they improve clarity
- Use small diagrams for workflows, architecture, and before/after journeys when they clarify the sales argument
- Use Dyna.Ai brand color for structure and CTA, turquoise for support, yellow for sparse callouts
- Keep body copy concise and grouped into scan-friendly blocks
- Do not overfill visual assets with paragraph-heavy explanation

## Copy Rules

- Lead with business value, then capabilities
- Translate AI features into buyer outcomes
- Use concrete language: reduce manual review, accelerate onboarding, improve risk detection, scale operations
- Avoid unsupported superlatives and vague transformation claims
- Do not invent ROI, efficiency percentages, client results, client names, or quotes
- Mark unapproved claims as placeholders that need business, legal, or customer confirmation
- Keep partner, integration, and customer relationship language precise and verifiable
- Keep each section useful even when read out of order

## Proof Presentation

Prefer proof in this order:

1. verified metrics
2. named or approved client proof
3. anonymized industry evidence
4. operational workflow examples
5. credible qualitative benefits

Do not invent metrics. If evidence is missing, write placeholders that clearly need client confirmation.

Claim quality order:

1. Approved customer metric or quote
2. Verified internal product metric
3. Qualitative benefit tied to a concrete workflow
4. Placeholder requiring confirmation

## Export And Handoff

- Visual Track outputs should be usable for image generation or page generation without major reinterpretation
- PDF should be readable at 100 percent zoom
- Long-form pages should preserve margins and footer clarity
- Charts and tables should remain legible when printed
- Use file names that include asset type, market, version, and date when appropriate

## Quality Check

Before finalizing:

1. The asset can be understood in under one minute
2. Buyer value is visible before feature detail
3. Proof points are credible and not invented
4. Typography and color follow Dyna.Ai rules
5. The output matches the chosen track
6. A non-design teammate could use the result without guessing the core visual structure
7. Sales teams can reuse the asset without design intervention

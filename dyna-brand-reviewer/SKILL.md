---
name: dyna-brand-reviewer
description: Review Dyna.Ai branded assets for visual quality, compliance, and release readiness.
---

# Dyna.Ai Brand Reviewer

Use this skill to review Dyna.Ai branded work and provide actionable feedback. It is for critique, QA, preflight, visual quality control, and brand compliance rather than initial concept generation.

This skill is maintained by brand designers so non-design teammates can understand whether an AI-generated or team-generated visual is strong enough to use, revise, hand off, or release.

Use `dyna-brand-foundation` for core brand standards. Use the relevant scene skill when reviewing a campaign, event, social asset, website page, sales document, presentation, or dashboard. Use `dyna-presentation-design` for PPT, deck, slide, company profile, sales deck, webinar deck, and executive presentation review.

## When to Use

Use before external release, partner co-marketing, vendor production, event production, sales distribution, website launch, dashboard handoff, or whenever a draft feels off-brand.

## Required Inputs

- Asset type, channel, intended audience, current draft or description, source files if available, release or production context, and whether the target is a visual, page, deck, document, or vendor asset
- If the draft is not visible, audit the provided brief and call out assumptions

## Output Contract

Use `dyna-brand-foundation/references/output-contracts.md` and `dyna-brand-foundation/references/review-rubric.md`. Return Overall assessment, Source of truth used, Visual quality assessment, Priority issues, Suggested fixes, Production risks, and Approval status.

## Common Failures

- Feedback without severity
- Vague taste comments instead of fixable issues
- Missing source traceability
- Rewriting the whole asset when the user asked for audit
- Passing an asset that is compliant but visually too weak, generic, or unreadable for release

## Reviewer Handoff

Use P0/P1/P2/P3 severity from `review-rubric.md`. Approval status must be approved, approved with edits, or revise and resubmit.

## Source Priority

Use the most specific official PDF first:

- Visual identity: `Dyna.Ai Brand Visual Identity Guidelines .pdf`
- Social and digital: `Dyna.Ai socialmedia Guidelines.pdf`
- Events and booths: `Dyna.Ai Event Guideline.pdf`
- Office, showroom, signage, supplies, apparel: `Dyna.Ai Brand Guideline - Office.pdf`
- Decks: the approved Dyna.Ai PPT template and `dyna-presentation-design`

## Review Stance

Be direct, specific, and constructive. Prioritize issues that affect brand recognition, business clarity, readability, production quality, or market credibility.

## Visual-First Review Stance

For image, page, KV, dashboard, deck, event, social, or environment work, review more than rule compliance. Check whether the asset is visually strong enough for a non-design teammate to use.

Assess:

- visual hierarchy
- readability at the actual size or viewing distance
- brand recognizability
- proof and CTA clarity
- image-generation artifacts or generic AI styling
- whether the output feels ready to revise, hand off, or release

If the asset follows rules but still feels weak, mark it as approved with edits or revise and resubmit, and explain the concrete design change needed.

## Collaboration Review

When an asset crosses scenes, name the scene skills that should have informed the work:

- campaign, social, event, office, presentation, sales, website, or dashboard
- source of truth PDF or template
- whether a reviewer pass should happen again after edits

## Review Order

1. Brand identity
2. Message clarity
3. Layout and hierarchy
4. Color and typography
5. Imagery and graphics
6. Data, charts, and proof
7. Channel or format fit
8. Production and export readiness

## Brand Checks

- Brand name is exactly `Dyna.Ai`
- Logo is approved, undistorted, and placed with enough clear space
- Logo clear space is at least `0.5b`
- Logo minimum size is respected: `10mm` high for print, `28px` high for mobile/online, `1in` high for TV/video
- Dyna.Ai brand color `#006CEE` is used for Dyna.Ai brand work
- Black `#000000`, white `#FFFFFF`, light blue `#9ABCFF`, and channel-specific accents are used according to role
- Typography follows the intended medium
- The overall style feels modern, clean, premium, and enterprise-ready
- The asset does not look like a disconnected template or generic AI brand

## Channel Checks

- Social backgrounds generally follow the `95%` blue family / `5%` secondary color rule unless it is a special festival or event asset
- Social gradients use only approved gradient pairs from the socialmedia guideline
- Social partner lockups follow the font-logo and graphic-logo sizing rules from the socialmedia guideline
- Event KVs use the standard hierarchy: Logo, Title, KV, Info, CTA
- Event standard KVs use `16:9`, recommended `1920 x 1080`, with a unified grid and margin system
- Event billboards use `3.4:1` as the default common ratio unless venue specs require otherwise
- Event materials use premium production methods such as lightbox fabric, UV printing, acrylic, or metal where appropriate
- Office applications follow site-specific dimensions, screen specs, signage location, and material guidance from the Office guideline

## Message Checks

- Main message is immediately understandable
- Headline is not trying to carry too many ideas
- Supporting copy is concrete, credible, and concise
- CTA is visible and specific
- Claims are not exaggerated or unsupported
- Audience, industry, or use case is clear when needed
- Copy uses specific business, workflow, or product language rather than vague AI magic
- Proof level is clear: verified, sourced, approved, or placeholder
- Partner, customer, and platform relationships are not overstated
- CTA matches the user's next step and does not rely on passive language

## Visual Checks

- Layout has clear hierarchy and spacing
- Alignment and grid are consistent
- No important text sits on low-contrast or busy backgrounds
- Icons, shapes, and patterns support meaning rather than decoration
- Image choice feels credible for enterprise AI and fintech
- Mobile or small-size readability is considered for digital assets
- AI-generated visuals avoid generic SaaS cliches, unreadable fake UI, distorted logo use, and text-like artifacts

## Data And Proof Checks

- Metrics are labeled and sourced when required
- Tables are readable and numeric columns are aligned
- Charts use brand colors semantically
- Yellow marks attention, threshold, or anomaly only
- Red and green are reserved for conventional negative and positive semantics
- No invented metrics or unsourced client proof

## Production Checks

- Asset size and ratio match the target channel
- Safe margins and cropping risks are handled
- Print assets use correct resolution and color mode
- Screen assets are exported at the required pixel size
- File naming and versioning are clear
- Vendor-facing files include enough execution instructions

## Feedback Format

When reviewing, return:

- Overall assessment: on-brand, mostly on-brand, needs revision, or off-brand
- Source of truth used: name the governing VI, social, event, office, or scene rule
- Visual quality assessment: explain whether the asset is strong enough for the intended channel and audience
- Priority issues: use P0/P1/P2/P3 labels from `review-rubric.md`, highest impact first
- Brand language / claim quality: identify hype, vague AI language, unsupported claims, proof gaps, and CTA weakness
- Suggested fixes: concrete changes, not vague reactions
- Production risks: export, vendor, crop, legibility, proof, or approval blockers
- Approval status: approved, approved with edits, or revise and resubmit

Keep feedback useful for designers, marketers, and non-design teammates. Do not rewrite the whole asset unless the user asks.

---
name: dyna-website-landing-design
description: Create or review Dyna.Ai websites and landing pages.
---

# Dyna.Ai Website And Landing Design

Use this skill for Dyna.Ai market-facing web pages, landing pages, solution pages, industry pages, product pages, thought-leadership pages, and campaign destinations.

This skill is also a supporting skill for collaborative visual tasks when a non-design teammate needs a onepage, image, or page section with stronger hero hierarchy, proof rhythm, and CTA structure.

Use `dyna-brand-foundation` for core brand rules. Use dashboard-specific guidance only when the page is an authenticated product console or operational dashboard.

## When to Use

Use for marketing websites, landing pages, product pages, solution pages, industry pages, webinar registration pages, and campaign destinations.

Use as a supporting skill when another asset needs:

- a stronger first viewport
- a clearer hero promise
- more disciplined CTA hierarchy
- proof placement near the top
- a landing-style narrative shell around another scene's content

## Required Inputs

- Page goal, audience, offer, proof, primary CTA, conversion path, required sections, form needs, and responsive constraints
- If product proof is missing, use placeholders and identify what needs approval

## Output Contract

Use `dyna-brand-foundation/references/output-contracts.md`: return a Page Structure, Design Spec, or reusable first-screen module with first viewport, section order, proof modules, claim risk, CTA flow, responsive behavior, and brand checks.

## Common Failures

- Generic SaaS hero composition
- Weak proof below the first viewport
- Too many CTAs with equal emphasis
- Landing page rules applied to product dashboards
- Landing guidance used as the whole answer for a product-heavy visual that also needs dashboard or sales logic

## Reviewer Handoff

Use `dyna-brand-reviewer` before design handoff, development handoff, campaign launch, or paid media traffic.

## Page Goal

A Dyna.Ai marketing page should:

- communicate the offer immediately
- show real product, outcome, or industry relevance
- build trust through proof and specificity
- guide users toward one primary CTA
- feel premium, structured, and enterprise-ready

## Collaboration Role

In cross-skill work, this skill contributes the marketing-facing shell.

It should supply:

- hero promise
- first-screen hierarchy
- CTA rhythm
- proof-above-the-fold logic
- section ordering that helps a non-design teammate avoid generic page composition

It should not try to replace:

- dashboard product structure
- sales proof discipline
- operational semantics

When the request is a onepage image or a product-story visual, use this skill to shape the top-level narrative and first screen, then combine it with supporting skills as needed.

## Default Page Structure

Use this structure unless the content suggests a better one:

- navigation with clear brand presence
- hero with product, solution, or campaign name as the first-viewport signal
- concise value proposition and primary CTA
- proof row: metrics, client categories, use cases, or trust signals
- problem / market context
- Dyna.Ai solution modules
- product or workflow visual
- industry or persona benefits
- case study, quote, or outcome proof
- resources or next-step module
- footer CTA

The first viewport must show what the page is about without relying only on nav text.

For collaborative onepage visuals, the hero plus proof strip is often the most important contribution from this skill.

## Hero Rules

- The H1 should be the product, solution, campaign, or literal offer
- Put explanation in supporting copy, not in an overlong headline
- Supporting copy should connect the offer to a specific business problem and proof cue
- Use a real product visual, workflow, relevant image, or strong brand-led composition
- Do not make the hero look like a generic SaaS template
- Leave a hint of the next section visible on common desktop and mobile viewports
- Keep primary CTA visible without crowding the hero

## Brand Language Rules

- H1 should be concrete enough to stand alone in a browser tab, share preview, or sales conversation.
- Supporting copy should say what Dyna.Ai helps users do, for whom, and with what proof level.
- Proof sections should separate verified proof from placeholders awaiting approval.
- CTA copy should match intent: request demo, register, download report, contact sales, or explore solution.
- Avoid claims that promise outcomes without evidence or imply deployment guarantees.

## Section Design

- Use full-width sections with constrained inner content
- Avoid stacking cards inside cards
- Use cards only for repeated items, proof modules, resource lists, or framed product snippets
- Use a clear section title, short explanation, and scannable modules
- Alternate density: do not make every section a three-card row
- Show proof through data, workflows, screenshots, client categories, or concrete examples

## Default Landing Wireframe

When the user does not provide a stronger structure, use this wireframe:

- **Navigation**
  - logo, product/solution links, resource link, primary CTA

- **Hero**
  - H1 as product, solution, campaign, or literal offer
  - one short value proposition
  - primary CTA and quieter secondary CTA
  - product, workflow, or proof-led visual
  - hint of proof section visible below first viewport

- **Proof Strip**
  - 3-4 metrics, client categories, regions, use cases, or validated claims
  - use placeholders only when proof still needs approval

- **Problem / Market Context**
  - concise framing of buyer pain
  - avoid long manifesto copy

- **Solution Modules**
  - 3-5 capability modules with clear outcome labels
  - use screenshots, workflow diagrams, or icons only when they clarify the offer

- **Workflow / Product Evidence**
  - show how Dyna.Ai executes, verifies, escalates, or reports work

- **Use Cases / Industries**
  - organize by banking, insurance, payments, lending, collections, risk, or customer operations when relevant

- **Governance / Trust**
  - security, auditability, compliance, human review, deployment control

- **Final CTA**
  - repeat the primary conversion path after proof, not after every section

## Web UI Brand Rules

- Use Dyna.Ai brand color `#006CEE` for primary buttons, active states, and key links
- Use black `#000000` and white `#FFFFFF` for strong contrast
- Use `#E5F0FF` or light blue fields for soft section backgrounds
- Use turquoise `#00EDFF` sparingly for secondary highlights and data visuals
- Use yellow only for alerts, selected markers, or high-attention labels
- Use `Poppins` for brand-led marketing UI
- Keep body text highly readable and avoid dense centered paragraphs

## Conversion Rules

- One primary CTA per page section is enough
- Secondary CTAs should be visually quieter
- CTA copy should be concrete: request demo, download report, register, contact sales, explore solution
- Repeat the CTA after proof sections, not after every paragraph
- Forms should ask for only necessary fields and keep labels direct

## Avoid

- abstract hero visuals that do not identify Dyna.Ai or the offer
- decorative gradients unrelated to the brand system
- generic AI stock imagery without business context
- long text blocks in the hero
- broad AI transformation claims without proof
- oversized marketing cards that reduce information density
- web sections that explain features without showing proof or workflow

## Quality Check

Before finalizing:

1. The first viewport clearly identifies the offer
2. The page has one primary conversion path
3. Product, industry, or proof content appears early
4. Brand palette and typography are consistent
5. Mobile layout preserves hierarchy and CTA clarity
6. The page feels like Dyna.Ai, not a generic AI landing page
7. If used as a supporting skill, the result gives a non-design teammate a clearer hero and CTA system without flattening the product story

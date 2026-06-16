---
name: dyna-brand-foundation
description: Route Dyna.Ai brand work to the right source of truth and the right visual collaboration path.
---

# Dyna.Ai Brand Foundation

This is the Dyna.Ai brand source router. Use it first when a request is broad, cross-channel, or unclear, then load the most specific scene skill and reference file needed for the task.

This skill system is maintained by brand designers so non-design teammates can safely produce stronger Dyna.Ai visuals, pages, and branded assets with AI. For visual work, the goal is not to stop at a text brief. The goal is to reach a high-quality visual direction that can directly drive image generation, page generation, review, and handoff.

## Core Truth

- Brand name: `Dyna.Ai`
- Brand color: `#006CEE`
- Brand typeface: `Poppins`
- Logo clear space: at least `0.5b`, where `b` is logo height
- Design goal: premium clarity for enterprise AI and fintech audiences
- Language standard: specific over vague, proof over hype, capability over magic, clear role over implied endorsement, business outcome over abstract transformation
- Visual-first rule: for image, page, KV, onepage, or UI-facing requests, final delivery should prioritize visual quality; text is a support layer, not the default end state

Do not introduce alternate, decorative, novelty, or unrelated default product fonts into Dyna.Ai brand work. Do not describe `#006CEE` as temporary, channel-only, or tied only to a new material type.

## Source Of Truth

Use the most specific official source for the asset:

- VI: `Dyna.Ai Brand Visual Identity Guidelines .pdf` for logo, brand color, typography, brand symbol, naming, and core don'ts
- Social: `Dyna.Ai socialmedia Guidelines.pdf` for LinkedIn, email/EDM, web banners, digital ads, webinar assets, social gradients, platform sizes, and partner lockups
- Event: `Dyna.Ai Event Guideline.pdf` for exhibitions, Dyna Day, customer visits, webinars, event KV, booth materials, billboards, and vendor checks
- Office: `Dyna.Ai Brand Guideline - Office.pdf` for reception, showroom, signage, office supplies, apparel, and workplace applications
- Presentation: official Dyna.Ai 2026 Company Profile PPT template for PPT, decks, slides, company profiles, sales decks, webinar decks, and executive presentations

When a channel PDF gives a more specific rule than this foundation, follow the channel PDF for that channel.

## Who This System Serves

- **Maintainers**: brand designers who encode Dyna.Ai visual standards, quality bars, and scene-specific rules into the skill set
- **Users**: teammates who are not designers or are less design-confident, including marketing, sales, product, operations, and cross-functional teams

Write guidance so a non-design teammate can still produce a stronger visual result without inventing structure, colors, proof, or hierarchy.

## Skill Routing

| User intent | Use |
|---|---|
| Core brand rule, source choice, cross-channel task | `dyna-brand-foundation` |
| Campaign idea, launch KV, integrated visual system | `dyna-campaign-design` |
| LinkedIn, email/EDM, web banner, digital ad, webinar visual, partner social | `dyna-social-digital-design` |
| Website page, landing page, webinar registration page, hero-led first screen | `dyna-website-landing-design` |
| Sales visual, onepage PNG, solution onepage, product-story image, one-pager, datasheet, case study, whitepaper, sales PDF | `dyna-sales-enablement-design` |
| PPT, deck, slides, slide visual system, company profile, sales deck, webinar deck, executive presentation | `dyna-presentation-design` |
| Dashboard, AI console, KPI view, product UI direction, operational product surface | `dyna-dashboard-design-guideline` |
| Event KV, booth visual, webinar cover, billboard, vendor event spec | `dyna-event-design-guideline` |
| Reception, showroom screen, signage, ID, lanyard, bag, apparel | `dyna-office-environment-design` |
| Audit, QA, visual quality check, off-brand critique, pre-release approval | `dyna-brand-reviewer` |

## References

Load only the reference needed for the task:

- `references/tokens.md` for exact colors, typography, logo, data, and forbidden patterns
- `references/channel-rules.md` for source priority and skill routing
- `references/output-contracts.md` for brief, spec, audit, vendor checklist, and page structure formats
- `references/review-rubric.md` for P0/P1/P2/P3 severity and approval format
- `references/smoke-tests.yaml` for regression prompts used by the validation script

## Default Workflow

1. Identify asset type, audience, channel, output format, and whether the final deliverable is visual-first or document-first.
2. Choose the primary scene skill from `references/channel-rules.md`.
3. If the task needs multiple strengths, name the supporting scene skills as well.
4. Apply Dyna.Ai tokens from `references/tokens.md`.
5. Use the relevant output contract from `references/output-contracts.md`, but adapt it toward visual direction when the final deliverable is an image or page.
6. For external, partner, sales, presentation, event, office, dashboard, or vendor-facing work, run a second pass with `dyna-brand-reviewer`.

## Collaboration Rules

For complex visual tasks, do not force one skill to do everything. Combine scene skills deliberately:

- Use `dyna-sales-enablement-design` for buyer-facing value, proof discipline, CTA, and claim safety
- Use `dyna-dashboard-design-guideline` for product credibility, KPI logic, workflow/status semantics, and operational surface
- Use `dyna-website-landing-design` for hero structure, first-screen hierarchy, and CTA rhythm
- Use `dyna-campaign-design` for master KV direction and campaign family coherence
- Use `dyna-social-digital-design` for feed, carousel, EDM, banner, and paid media readability
- Use `dyna-event-design-guideline` for event KV, booth, webinar, billboard, and vendor-facing production logic
- Use `dyna-office-environment-design` for showroom, screen, signage, and physical environment constraints
- Use `dyna-presentation-design` for slide rhythm, template mapping, and deck visual systems
- Use `dyna-brand-reviewer` for final brand QA when the result will be shared externally or handed to design, vendors, or development

When a request crosses scenes, always name:

- primary skill
- supporting skills
- reviewer step

## Output Expectations

- If creating a visual task: return visual direction, image-generation-ready prompt structure, layout hierarchy, content modules, CTA placement, proof handling, and brand/readability guardrails.
- If creating a document-heavy task: return a brand brief, design spec, presentation / deck spec, page structure, or vendor checklist.
- If reviewing: return an audit using severity labels and approval status.
- If evidence is missing: use explicit placeholders and name what needs confirmation.
- If the request crosses channels: name the primary skill, supporting skill, and reviewer step.
- For market-facing copy: state the proof level, claim risk, and concrete CTA.

## Quality Bar

Before finalizing any Dyna.Ai branded work, check:

1. `Dyna.Ai` naming is exact
2. `#006CEE` is treated as the Dyna.Ai brand color
3. `Poppins` is the brand typeface
4. Logo artwork, minimum size, and `0.5b` clear space are respected
5. Source of truth matches the channel
6. Copy is concrete, credible, and enterprise-ready
7. Visual direction feels specific to Dyna.Ai, not generic AI or SaaS styling
8. Claims, metrics, quotes, and case studies are verified or clearly marked as placeholders
9. Headlines, CTAs, and proof points are precise, restrained, and commercially believable
10. The output can help a non-design teammate reach a stronger visual result without guessing core brand decisions

## Validation

Use the bundled scripts after updating the Dyna skill package:

```bash
python3 .codex/skills/dyna-brand-foundation/scripts/validate_dyna_brand.py
python3 .codex/skills/dyna-brand-foundation/scripts/run_dyna_skill_checks.py
```

## Maintenance And Feedback

When a brand rule changes:

1. Update `references/tokens.md` or the relevant channel reference first.
2. Update affected scene skills only if their behavior changes.
3. Add or revise at least one case in `references/smoke-tests.yaml`.
4. Run both validation scripts before sharing the skill package.

When a marketer reports a bad output, capture:

- Original prompt
- Asset type and channel
- Whether the final goal was visual-first or document-first
- Source of truth that should have applied
- What the output did wrong
- Correct expected behavior

If the issue can recur, convert it into a smoke case.

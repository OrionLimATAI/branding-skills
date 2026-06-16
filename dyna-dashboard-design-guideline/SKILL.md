---
name: dyna-dashboard-design-guideline
description: Create or review Dyna.Ai dashboards and product consoles.
---

# Dyna.Ai Dashboard Design Guideline

Use this skill for Dyna.Ai dashboards, AI product consoles, KPI screens, analytics views, operational workspaces, and executive overview screens.

This skill is also a supporting skill for collaborative visual tasks when a non-design teammate needs a sales visual, onepage, or page section to feel like a real Dyna.Ai product surface rather than a generic marketing mockup.

Use `dyna-brand-foundation` for core brand rules. If the implementation uses shadcn/ui, describe component structure, state semantics, and interaction requirements inside this dashboard guidance rather than routing to a separate skill.

## When to Use

Use for dashboards, AI product consoles, KPI screens, analytics views, operational workspaces, workflow monitors, and executive overview screens.

Use as a supporting skill when another visual asset needs:

- product credibility
- KPI logic
- workflow status
- operational structure
- real software surface cues

## Required Inputs

- User role, workflow, data domain, KPIs, status semantics, priority semantics, actions, device constraints, and implementation stack if known
- If data is sample-only, label it as placeholder content

## Output Contract

Use `dyna-brand-foundation/references/output-contracts.md`: return a Design Spec or reusable product-UI skeleton with first viewport, KPI structure, chart semantics, status system, table behavior, action panel, and brand checks.

## Common Failures

- Dashboard treated like a campaign poster
- Supporting role used to overtake the whole composition instead of supplying product structure
- Status and priority represented with the same visual logic
- Color-only status communication
- Dense table before users see context or next action

## Reviewer Handoff

Use `dyna-brand-reviewer` for brand QA. When the output must become shadcn/ui implementation guidance, keep the guidance inside this skill and specify the component mapping clearly.

## Dashboard Goal

A Dyna.Ai dashboard should feel:

- operationally useful
- enterprise-grade
- data-rich but readable
- brand-controlled without becoming decorative
- credible for fintech and AI workflows

## Collaboration Role

In cross-skill work, this skill contributes the product-facing layer.

It should supply reusable visual bones such as:

- KPI strip
- status system
- workflow modules
- queue or operational card patterns
- product-console hierarchy

It should not try to define the whole commercial story, sales CTA, or landing-page narrative by itself.

When helping non-design teammates, be explicit about what to keep:

- keep the smallest set of modules that proves the product is real, active, and governable
- do not carry full desktop dashboard density into a onepage image or marketing page

## Recommended Structures

Choose based on task:

- **Ops Console**: sidebar, filter bar, KPI row, primary chart, workflow status, operational table
- **Executive Overview**: summary hero, larger KPIs, trend chart, regional or segment comparison, action summary
- **Analytics Workspace**: tabs, filters, chart-led analysis, breakdown cards, detailed table
- **AI Workflow Monitor**: model/job status, queue, confidence or quality metrics, exceptions, audit log

Default to Ops Console unless the user asks for a boardroom-style overview.

## First Viewport

Include at least:

- clear product or workspace identity
- current context such as region, time range, model, workflow, or portfolio
- 3 to 4 key KPIs
- one primary analytical module
- one operational next-action or status module

Do not start with a dense table unless the user asks for a table-first admin view.

For collaborative visuals, first viewport modules are often enough. You usually do not need the full lower-page dashboard system unless the story depends on it.

## Color And Surface Rules

- Use near black or dark blue as an anchor zone for the shell, hero, or flagship module
- Use the Dyna.Ai brand color for active navigation, selected tabs, primary actions, key chart series, and main KPIs
- Use turquoise for secondary series, verified states, healthy signals, and support metrics
- Use mist blue or cool neutral surfaces for quiet containers and filters
- Use yellow only for warnings, anomalies, pending review, or thresholds
- Use red and green only for conventional failed/success or negative/positive status semantics

Use Dyna.Ai brand color `#006CEE` as the default product UI brand color.

## Status Semantics

Keep status and priority separate:

- Critical, failed, error: red
- Warning, blocked, needs review, high priority: yellow
- Running, active, selected, in progress: blue
- Verified, healthy, synced: turquoise
- Completed, passed, resolved: green or turquoise depending on context
- Queued, paused, inactive, draft: muted grey or navy

Use text labels plus icons or dots. Do not rely on color alone.

## Components

Prefer reusable product components:

- KPI cards
- chart cards
- filter bars
- tabs or segmented controls
- operational tables
- status badges
- workflow progress rows
- audit logs
- side navigation
- action panels

Avoid bespoke decorative modules when standard product patterns work.

## Default Dashboard Layout Recipe

When the user asks for a Dyna.Ai dashboard without a more specific architecture, use this recipe:

- **Shell**
  - sidebar or top navigation with Dyna.Ai product identity
  - workspace, region, workflow, or time-range context
  - primary action and search/filter controls when useful

- **Summary Row**
  - 3-4 KPI cards
  - lead KPI may use a dark or blue anchor surface
  - supporting KPIs use blue, light blue, turquoise, or neutral surfaces according to meaning

- **Primary Analytics**
  - one major chart card with `#006CEE` as the primary series
  - use `#9ABCFF` or `#00EDFF` for comparison series
  - reserve `#FFE500` for thresholds, anomalies, or needs-review markers

- **Workflow Status**
  - progress rows or job cards showing workflow name, owner, state, percent complete, and next action
  - use continuous progress bars rather than decorative equal segments

- **Operational Table**
  - dense but readable table for jobs, sources, candidates, tickets, agents, or audit records
  - separate priority and status columns when both dimensions matter

- **Review / Action Panel**
  - surface exceptions, approvals, blocked items, or escalation queue
  - keep actions close to the relevant status or row

For shadcn/ui implementations, map the recipe to `Card`, `Button`, `Badge`, `Tabs`, `Table`, `Separator`, and `Avatar` where available.

## Data Visualization

- Brand series: Dyna.Ai brand color `#006CEE`
- Secondary series: light blue `#9ABCFF` or turquoise `#00EDFF`
- Tertiary non-warning category: controlled purple `#A533FF` when a third brand-controlled category is needed
- Thresholds or anomalies: yellow `#FFE500`
- Errors or negative values: red
- Positive values: green only when users expect conventional semantics

Charts must be responsive, labeled, and readable on small widths. Avoid fixed chart widths and low-contrast gridlines.

## Layout Rules

- Dense is acceptable when organized
- Use clear section titles and compact metadata
- Use product language that reflects workflow, status, ownership, and next action
- Avoid marketing claims inside operational product screens
- Keep repeated cards visually related but not identical when their meanings differ
- Avoid large empty marketing-style hero areas inside operational tools
- Do not put cards inside cards
- Use hover, active, loading, empty, and error states where product behavior implies them
- When used as a supporting skill, prefer compact, reusable product modules over full dashboard sprawl

## Quality Check

Before finalizing:

1. The dashboard supports a real workflow
2. KPIs and charts are semantically colored
3. Priority and status states are distinguishable
4. The first viewport shows at least three brand-controlled zones
5. Tables and charts remain readable on mobile or narrow layouts
6. The result feels like Dyna.Ai product software, not a campaign poster
7. If used as a supporting skill, the output strengthens product credibility without overwhelming the main narrative

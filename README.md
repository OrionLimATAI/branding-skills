# Branding Skills

Open, reusable Dyna.Ai branding skills for marketing, brand strategy, visual review, campaign design, digital assets, events, sales enablement, presentations, dashboards, websites, and office/environment applications.

## Skills

| Skill | Use for |
|---|---|
| `dyna-brand-foundation` | Core brand routing, source-of-truth selection, shared tokens, output contracts, and quality bar |
| `dyna-brand-reviewer` | Brand QA, release readiness, severity-labeled review, and production risk checks |
| `dyna-campaign-design` | Campaign KVs, launch visuals, integrated campaign systems, and cross-channel adaptation |
| `dyna-social-digital-design` | LinkedIn, carousels, EDM headers, web banners, digital ads, webinar promos, and partner social assets |
| `dyna-website-landing-design` | Marketing websites, landing pages, solution pages, product pages, and campaign destinations |
| `dyna-sales-enablement-design` | Onepages, solution briefs, sales visuals, proposal pages, datasheets, case studies, and sales PDFs |
| `dyna-presentation-design` | PPT decks, slide systems, company profiles, sales decks, webinar decks, and executive presentations |
| `dyna-dashboard-design-guideline` | Product dashboards, AI consoles, KPI views, analytics pages, and operational workspaces |
| `dyna-event-design-guideline` | Event KVs, booths, webinars, billboards, vendor-ready event systems, and production checks |
| `dyna-office-environment-design` | Reception, showroom, office signage, screen content, supplies, ID cards, apparel, and workplace branding |

## Recommended Starting Point

Start with `dyna-brand-foundation` for broad or unclear requests. It routes to the correct scene skill and contains the shared reference files used by the rest of the package.

## Repository Structure

Each skill folder contains:

- `SKILL.md`: Codex skill instructions
- `agents/openai.yaml`: UI-facing metadata
- optional `references/` or `scripts/`: shared guidance and validation helpers


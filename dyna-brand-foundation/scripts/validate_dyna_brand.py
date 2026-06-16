#!/usr/bin/env python3
"""Validate the local Dyna.Ai branding skill package."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
REQUIRED_SKILLS = [
    "dyna-brand-foundation",
    "dyna-brand-reviewer",
    "dyna-campaign-design",
    "dyna-dashboard-design-guideline",
    "dyna-event-design-guideline",
    "dyna-office-environment-design",
    "dyna-presentation-design",
    "dyna-sales-enablement-design",
    "dyna-social-digital-design",
    "dyna-website-landing-design",
]
REQUIRED_REFERENCES = [
    "tokens.md",
    "channel-rules.md",
    "output-contracts.md",
    "review-rubric.md",
    "smoke-tests.yaml",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    sys.exit(1)


def main() -> None:
    for skill in REQUIRED_SKILLS:
        skill_dir = ROOT / skill
        skill_md = skill_dir / "SKILL.md"
        agent_yaml = skill_dir / "agents" / "openai.yaml"
        if not skill_md.exists():
            fail(f"Missing {skill}/SKILL.md")
        if not agent_yaml.exists():
            fail(f"Missing {skill}/agents/openai.yaml")
        text = skill_md.read_text()
        if not re.match(r"^---\nname: [a-z0-9-]+\ndescription: .+\n---", text, re.S):
            fail(f"Invalid frontmatter in {skill}/SKILL.md")

    ref_dir = ROOT / "dyna-brand-foundation" / "references"
    for ref in REQUIRED_REFERENCES:
        if not (ref_dir / ref).exists():
            fail(f"Missing dyna-brand-foundation/references/{ref}")

    print("[OK] Dyna.Ai branding skill package looks complete.")


if __name__ == "__main__":
    main()


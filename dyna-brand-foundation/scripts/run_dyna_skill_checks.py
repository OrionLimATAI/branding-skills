#!/usr/bin/env python3
"""Run lightweight Dyna.Ai branding smoke checks."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    foundation = (ROOT / "dyna-brand-foundation" / "SKILL.md").read_text()
    tokens = (ROOT / "dyna-brand-foundation" / "references" / "tokens.md").read_text()
    required = ["Dyna.Ai", "#006CEE", "Poppins", "0.5b"]
    missing = [item for item in required if item not in foundation and item not in tokens]
    if missing:
        print(f"[FAIL] Missing required brand tokens: {', '.join(missing)}")
        sys.exit(1)

    print("[OK] Smoke checks passed.")


if __name__ == "__main__":
    main()


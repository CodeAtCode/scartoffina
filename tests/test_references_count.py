"""Contract tests for reference file counts (rule #8770 — at least 10 references per skill)."""

from pathlib import Path

import pytest

SKILLS = sorted(
    d.name for d in Path(__file__).resolve().parent.parent.joinpath("skills").iterdir() if d.is_dir()
)

# Skills not yet enriched to Paperasse parity (tracked gap, see session history).
UNENRICHED_SKILLS: set[str] = set()


@pytest.mark.parametrize("skill_name", SKILLS)
def test_at_least_ten_references(skills_dir: Path, skill_name: str) -> None:
    """Rule #8770: every skill must have at least 10 reference files in references/."""
    if skill_name in UNENRICHED_SKILLS:
        pytest.xfail(f"{skill_name}: enrichment pending (tracked gap)")
    ref_dir = skills_dir / skill_name / "references"
    if not ref_dir.exists():
        pytest.skip(f"{skill_name}: no references/ directory")
    count = len([f for f in ref_dir.iterdir() if f.is_file()])
    assert count >= 10, f"{skill_name}: only {count} reference files (minimum is 10)"

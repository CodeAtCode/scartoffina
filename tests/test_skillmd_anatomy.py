"""Contract tests for SKILL.md section anatomy and version uniformity."""

import re
from pathlib import Path

import pytest

from conftest import parse_skillmd_frontmatter

SKILLS = sorted(
    d.name for d in Path(__file__).resolve().parent.parent.joinpath("skills").iterdir() if d.is_dir()
)

CANONICAL_SECTION_ORDER = [
    "Dichiarazione dual-use",  # optional, section 0
    "Scope",
    "Prerequisiti",
    "Freschezza dei Dati",
    "Workflow",
    "Script",
    "Promemoria Obbligatori",
    # optional topic sections (free titles, numbered 7, 8, ...)
    "Output",
    "Controlli di coerenza",  # optional
    "Limiti e responsabilità",
]

MANDATORY_SECTIONS = {
    "Scope",
    "Prerequisiti",
    "Freschezza dei Dati",
    "Workflow",
    "Script",
    "Promemoria Obbligatori",
    "Output",
    "Limiti e responsabilità",
}


def extract_sections(skill_path: Path) -> list[tuple[int, str]]:
    """Extract numbered ## N. Title sections from a SKILL.md file."""
    content = skill_path.read_text(encoding="utf-8")
    pattern = re.compile(r"^##\s+(\d+)\.\s+(.+)$", re.MULTILINE)
    return [(int(num), title.strip()) for num, title in pattern.findall(content)]


@pytest.mark.parametrize("skill_name", SKILLS)
def test_mandatory_sections_present(skills_dir: Path, skill_name: str) -> None:
    """All mandatory sections must be present in every SKILL.md."""
    skill_path = skills_dir / skill_name / "SKILL.md"
    sections = extract_sections(skill_path)
    section_titles = {title for _, title in sections}

    missing = MANDATORY_SECTIONS - section_titles
    assert not missing, f"{skill_name}: missing mandatory sections: {missing}"


@pytest.mark.parametrize("skill_name", SKILLS)
def test_mandatory_sections_order(skills_dir: Path, skill_name: str) -> None:
    """Mandatory sections must appear in canonical order."""
    skill_path = skills_dir / skill_name / "SKILL.md"
    sections = extract_sections(skill_path)

    # Filter to only mandatory sections (and optional dual-use)
    relevant_sections = [
        title for _, title in sections
        if title in MANDATORY_SECTIONS or title == "Dichiarazione dual-use"
    ]

    # Check order matches canonical
    expected_order = [s for s in CANONICAL_SECTION_ORDER if s in relevant_sections or s == "Dichiarazione dual-use"]
    
    # Build actual order from found sections
    actual_order = []
    for title in relevant_sections:
        if title in expected_order and title not in actual_order:
            actual_order.append(title)
    
    # Check that mandatory sections appear in the correct relative order
    mandatory_in_file = [t for t in relevant_sections if t in MANDATORY_SECTIONS]
    expected_mandatory = [s for s in CANONICAL_SECTION_ORDER if s in mandatory_in_file]
    
    assert mandatory_in_file == expected_mandatory, (
        f"{skill_name}: mandatory section order mismatch.\n"
        f"Expected: {expected_mandatory}\n"
        f"Actual: {mandatory_in_file}"
    )


@pytest.mark.parametrize("skill_name", SKILLS)
def test_contiguous_numbering(skills_dir: Path, skill_name: str) -> None:
    """Section numbers must be contiguous starting at 0 or 1."""
    skill_path = skills_dir / skill_name / "SKILL.md"
    sections = extract_sections(skill_path)
    
    if not sections:
        pytest.skip(f"{skill_name}: no numbered sections found")
    
    numbers = sorted(num for num, _ in sections)
    start = numbers[0]
    
    assert start in (0, 1), f"{skill_name}: sections must start at 0 or 1, found {start}"
    
    expected = list(range(start, start + len(numbers)))
    assert numbers == expected, (
        f"{skill_name}: section numbers not contiguous.\n"
        f"Expected: {expected}\n"
        f"Actual: {numbers}"
    )


@pytest.mark.parametrize("skill_name", SKILLS)
def test_uniform_version(skills_dir: Path, skill_name: str) -> None:
    """All SKILL.md files must have the same version."""
    skill_path = skills_dir / skill_name / "SKILL.md"
    fm = parse_skillmd_frontmatter(skill_path)
    
    assert fm is not None, f"{skill_name}: cannot parse frontmatter"
    
    version = fm.get("metadata", {}).get("version")
    assert version == "0.2.0", f"{skill_name}: version={version!r}, expected 0.2.0"
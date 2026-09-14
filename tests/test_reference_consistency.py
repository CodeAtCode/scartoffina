"""Contract tests for reference file consistency across skills."""

from pathlib import Path

import pytest

SKILLS = sorted(
    d.name for d in Path(__file__).resolve().parent.parent.joinpath("skills").iterdir() if d.is_dir()
)


def find_reference_files(skills_dir: Path) -> dict[str, list[Path]]:
    """Find all reference files grouped by basename across skills."""
    by_basename: dict[str, list[Path]] = {}
    
    for skill_name in SKILLS:
        ref_dir = skills_dir / skill_name / "references"
        if not ref_dir.exists():
            continue
        
        for ref_file in ref_dir.iterdir():
            if ref_file.is_file() and ref_file.suffix == ".md":
                basename = ref_file.name
                if basename not in by_basename:
                    by_basename[basename] = []
                by_basename[basename].append(ref_file)
    
    return by_basename


# Duplicate reference file basenames discovered across skills
DUPLICATE_BASENAMES = [
    "naspi.md",
    "formati.md",
    "ravvedimento-operoso.md",
]


@pytest.mark.parametrize("basename", DUPLICATE_BASENAMES)
def test_duplicate_references_are_identical(skills_dir: Path, basename: str) -> None:
    """All reference files with the same basename across skills must be byte-equal."""
    ref_files = find_reference_files(skills_dir).get(basename, [])
    
    if len(ref_files) < 2:
        pytest.skip(f"{basename}: only one or no reference file found")
    
    # Read all files
    contents = [(f, f.read_text(encoding="utf-8")) for f in ref_files]
    
    # Compare all to the first
    first_file, first_content = contents[0]
    
    for file, content in contents[1:]:
        assert content == first_content, (
            f"{basename}: files differ\n"
            f"Reference: {first_file}\n"
            f"Differ: {file}\n"
            f"Size difference: {len(first_content)} vs {len(content)} bytes"
        )
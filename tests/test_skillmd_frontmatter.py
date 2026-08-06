"""Contract tests for SKILL.md YAML frontmatter (rule #8707 — skillreg.dev compliance)."""

import re
from pathlib import Path

import pytest

from conftest import parse_skillmd_frontmatter

SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def _all_skills(skills_dir: Path) -> list[str]:
    return sorted(d.name for d in skills_dir.iterdir() if d.is_dir())


def _skill_names(skills_dir: Path):
    return pytest.mark.parametrize("skill_name", _all_skills(skills_dir))


def test_every_skill_has_skillmd(skills_dir: Path) -> None:
    """Rule #8707: every skill directory must contain a SKILL.md file."""
    missing = [d.name for d in skills_dir.iterdir() if d.is_dir() and not (d / "SKILL.md").exists()]
    assert not missing, f"Skills missing SKILL.md: {missing}"


@pytest.mark.parametrize(
    "skill_name",
    sorted(d.name for d in Path(__file__).resolve().parent.parent.joinpath("skills").iterdir() if d.is_dir()),
)
def test_frontmatter_parses(skills_dir: Path, skill_name: str) -> None:
    """Rule #8707: YAML frontmatter must parse without error."""
    fm = parse_skillmd_frontmatter(skills_dir / skill_name / "SKILL.md")
    assert fm is not None, f"{skill_name}: frontmatter missing or malformed"


@pytest.mark.parametrize(
    "skill_name",
    sorted(d.name for d in Path(__file__).resolve().parent.parent.joinpath("skills").iterdir() if d.is_dir()),
)
def test_name_matches_directory(skills_dir: Path, skill_name: str) -> None:
    """Rule #8707: frontmatter `name` must equal the directory name."""
    fm = parse_skillmd_frontmatter(skills_dir / skill_name / "SKILL.md")
    assert fm is not None, f"{skill_name}: cannot parse frontmatter"
    assert fm.get("name") == skill_name, f"{skill_name}: name={fm.get('name')!r} != dir={skill_name!r}"


@pytest.mark.parametrize(
    "skill_name",
    sorted(d.name for d in Path(__file__).resolve().parent.parent.joinpath("skills").iterdir() if d.is_dir()),
)
def test_has_metadata_author(skills_dir: Path, skill_name: str) -> None:
    """Rule #8707: metadata.author must be present."""
    fm = parse_skillmd_frontmatter(skills_dir / skill_name / "SKILL.md")
    assert fm is not None
    assert fm.get("metadata", {}).get("author"), f"{skill_name}: missing metadata.author"


@pytest.mark.parametrize(
    "skill_name",
    sorted(d.name for d in Path(__file__).resolve().parent.parent.joinpath("skills").iterdir() if d.is_dir()),
)
def test_has_metadata_version(skills_dir: Path, skill_name: str) -> None:
    """Rule #8707: metadata.version must be present and valid semver (major.minor.patch)."""
    fm = parse_skillmd_frontmatter(skills_dir / skill_name / "SKILL.md")
    assert fm is not None
    version = fm.get("metadata", {}).get("version")
    assert version, f"{skill_name}: missing metadata.version"
    assert SEMVER_RE.match(str(version)), f"{skill_name}: version={version!r} is not valid semver"


@pytest.mark.parametrize(
    "skill_name",
    sorted(d.name for d in Path(__file__).resolve().parent.parent.joinpath("skills").iterdir() if d.is_dir()),
)
def test_tags_count(skills_dir: Path, skill_name: str) -> None:
    """Rule #8707: maximum 10 tags allowed."""
    fm = parse_skillmd_frontmatter(skills_dir / skill_name / "SKILL.md")
    assert fm is not None
    tags = fm.get("metadata", {}).get("tags", [])
    assert len(tags) <= 10, f"{skill_name}: {len(tags)} tags exceeds limit of 10"


@pytest.mark.parametrize(
    "skill_name",
    sorted(d.name for d in Path(__file__).resolve().parent.parent.joinpath("skills").iterdir() if d.is_dir()),
)
def test_tag_length(skills_dir: Path, skill_name: str) -> None:
    """Rule #8707: each tag must be ≤ 32 characters."""
    fm = parse_skillmd_frontmatter(skills_dir / skill_name / "SKILL.md")
    assert fm is not None
    tags = fm.get("metadata", {}).get("tags", [])
    for tag in tags:
        assert len(tag) <= 32, f"{skill_name}: tag {tag!r} exceeds 32 chars ({len(tag)})"


@pytest.mark.parametrize(
    "skill_name",
    sorted(d.name for d in Path(__file__).resolve().parent.parent.joinpath("skills").iterdir() if d.is_dir()),
)
def test_env_count(skills_dir: Path, skill_name: str) -> None:
    """Rule #8707: maximum 20 env vars allowed."""
    fm = parse_skillmd_frontmatter(skills_dir / skill_name / "SKILL.md")
    assert fm is not None
    env = fm.get("env", [])
    assert len(env) <= 20, f"{skill_name}: {len(env)} env vars exceeds limit of 20"


@pytest.mark.parametrize(
    "skill_name",
    sorted(d.name for d in Path(__file__).resolve().parent.parent.joinpath("skills").iterdir() if d.is_dir()),
)
def test_env_required_default(skills_dir: Path, skill_name: str) -> None:
    """Rule #8707: env vars with required: false must have a default value."""
    fm = parse_skillmd_frontmatter(skills_dir / skill_name / "SKILL.md")
    assert fm is not None
    env = fm.get("env", [])
    for var in env:
        if var.get("required") is False:
            assert "default" in var, (
                f"{skill_name}: env var {var.get('name')!r} has required: false but no default"
            )

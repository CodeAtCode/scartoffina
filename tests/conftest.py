"""Shared fixtures and helpers for the Scartoffina test suite."""

from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def skills_dir(repo_root: Path) -> Path:
    return repo_root / "skills"


@pytest.fixture(scope="session")
def data_dir(repo_root: Path) -> Path:
    return repo_root / "data"


@pytest.fixture(scope="session")
def skill_dirs(skills_dir: Path) -> list[Path]:
    return sorted(d for d in skills_dir.iterdir() if d.is_dir())


def parse_skillmd_frontmatter(path: Path) -> dict | None:
    """Parse YAML frontmatter from a SKILL.md file.

    Returns the parsed dict, or None if the file is missing or malformed.
    """
    if not path.exists():
        return None
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None

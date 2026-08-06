"""Contract tests for JSON data files (rule #8717 — _meta block with freshness fields)."""

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

VALID_TIERS = {"1", "2", "manual", 1, 2}

REQUIRED_META_KEYS = {"verified_at", "source", "tier", "next_check_due"}


def _collect_json_files() -> list[str]:
    files: list[str] = []
    # Shared data/ at repo root
    shared = REPO_ROOT / "data"
    if shared.exists():
        files.extend(str(p) for p in shared.glob("*.json"))
    # Skill-specific data/ directories
    skills = REPO_ROOT / "skills"
    if skills.exists():
        for skill_dir in skills.iterdir():
            skill_data = skill_dir / "data"
            if skill_data.exists():
                files.extend(str(p) for p in skill_data.glob("*.json"))
    return sorted(files)


JSON_FILES = _collect_json_files()


def _relpath(path_str: str) -> str:
    return str(Path(path_str).relative_to(REPO_ROOT))


@pytest.mark.parametrize("json_file", JSON_FILES, ids=_relpath)
def test_json_parses(json_file: str) -> None:
    """Every JSON data file must parse without error."""
    data = json.loads(Path(json_file).read_text(encoding="utf-8"))
    assert data is not None


@pytest.mark.parametrize("json_file", JSON_FILES, ids=_relpath)
def test_meta_block_valid(json_file: str) -> None:
    """Rule #8717: if a JSON file has a _meta key, it must contain verified_at, source, tier, next_check_due."""
    data = json.loads(Path(json_file).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return
    meta = data.get("_meta")
    if meta is None:
        return
    assert isinstance(meta, dict), f"{_relpath(json_file)}: _meta is not a dict"
    missing = REQUIRED_META_KEYS - set(meta.keys())
    assert not missing, f"{_relpath(json_file)}: _meta missing keys: {missing}"
    assert meta["tier"] in VALID_TIERS, (
        f"{_relpath(json_file)}: _meta.tier={meta['tier']!r} not in {VALID_TIERS}"
    )

"""Contract tests for script interfaces (SKILL.md Script tables must match actual script CLIs).

This is the highest-leverage test: it catches the exact class of bug where a SKILL.md
documents a CLI invocation that doesn't match the actual script's argparse interface.
"""

import json
import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

# Matches: | `script.py` | `python3 scripts/...` | description |
TABLE_ROW_RE = re.compile(
    r"^\|\s*`([^`]+\.py)`\s*\|\s*`([^`]+)`\s*\|"
)
# Matches: ## N. Script
SCRIPT_HEADER_RE = re.compile(r"^##\s+\d+\.\s*Script\s*$", re.MULTILINE)


def _collect_script_cases() -> list:
    """Scan all SKILL.md files and collect (skill_name, command) pairs from Script tables."""
    cases = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        content = skill_md.read_text(encoding="utf-8")

        header_match = SCRIPT_HEADER_RE.search(content)
        if not header_match:
            continue

        start = header_match.end()
        next_header = re.search(r"^##\s+", content[start:], re.MULTILINE)
        if next_header:
            section = content[start : start + next_header.start()]
        else:
            section = content[start:]

        for line in section.splitlines():
            m = TABLE_ROW_RE.match(line)
            if m:
                script_name = m.group(1)
                command = m.group(2)
                tid = f"{skill_dir.name}:{command[:50]}"
                cases.append(pytest.param(skill_dir.name, command, id=tid))
    return cases


SCRIPT_CASES = _collect_script_cases()


@pytest.mark.parametrize("skill_name,command", SCRIPT_CASES)
def test_script_runs_and_emits_json(skill_name: str, command: str) -> None:
    """Every script command documented in a SKILL.md Script table must exit 0 and emit valid JSON on stdout."""
    skill_dir = SKILLS_DIR / skill_name
    result = subprocess.run(
        command,
        shell=True,
        cwd=skill_dir,
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, (
        f"{skill_name}: `{command}` exited {result.returncode}\n"
        f"stdout: {result.stdout[:500]}\n"
        f"stderr: {result.stderr[:500]}"
    )
    assert result.stdout.strip(), f"{skill_name}: `{command}` produced no stdout"
    # Scripts that emit JSON (calc_*, validate_*) must produce valid JSON.
    # Scripts that write to files (generate_*, import_*) emit a text confirmation.
    is_json_script = any(
        kw in command for kw in ("calc_", "calc.py", "validate_")
    ) and "validate_fattura" not in command
    if is_json_script:
        try:
            json.loads(result.stdout)
        except json.JSONDecodeError as e:
            pytest.fail(
                f"{skill_name}: `{command}` did not emit valid JSON: {e}\n"
                f"stdout: {result.stdout[:500]}"
            )


def test_at_least_one_skill_has_scripts() -> None:
    """Sanity check: at least one skill should have a Script section with documented commands."""
    assert len(SCRIPT_CASES) > 0, "No script cases found — check that SKILL.md Script tables exist"

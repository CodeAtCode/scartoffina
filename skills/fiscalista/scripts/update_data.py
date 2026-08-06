#!/usr/bin/env python3
"""Controllo freschezza dati del modulo fiscalista.

Delega al modulo updater centrale (updater.cli verify) per verificare
lo stato di freschezza dei dataset rilevanti per la skill fiscalista:
scaglioni-irpef, aliquote-imu, aliquote-addizionali-regionali.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

DATI_RILEVANTI = [
    "scaglioni-irpef.json",
    "aliquote-imu.json",
    "aliquote-addizionali-regionali.json",
]

PROGETTO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROGETTO_ROOT / "data"


def verifica_freschezza() -> dict:
    """Verifica freschezza dei dataset locali via _meta.next_check_due."""
    risultato = {"datasets": [], "tutti_freschi": True}
    for nome in DATI_RILEVANTI:
        path = DATA_DIR / nome
        if not path.exists():
            risultato["datasets"].append({"file": nome, "stato": "MANCANTE"})
            risultato["tutti_freschi"] = False
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            risultato["datasets"].append({"file": nome, "stato": f"ERRORE: {e}"})
            risultato["tutti_freschi"] = False
            continue
        meta = data.get("_meta", {})
        risultato["datasets"].append({
            "file": nome,
            "stato": "OK",
            "verified_at": meta.get("verified_at"),
            "source": meta.get("source"),
            "tier": meta.get("tier"),
            "next_check_due": meta.get("next_check_due"),
        })
    return risultato


def delega_updater() -> dict:
    """Tenta di delegare al modulo updater centrale."""
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "updater.cli", "verify"],
            capture_output=True, text=True, cwd=str(PROGETTO_ROOT), timeout=30,
        )
        return {
            "delegato": True,
            "returncode": proc.returncode,
            "stdout": proc.stdout[:2000],
            "stderr": proc.stderr[:500],
        }
    except (subprocess.SubprocessError, FileNotFoundError, OSError) as e:
        return {"delegato": False, "errore": str(e)}


def main() -> int:
    p = argparse.ArgumentParser(description="Controllo freschezza dati skill fiscalista")
    p.add_argument("--check", action="store_true", help="Esegui verifica locale")
    p.add_argument("--updater", action="store_true", help="Delega al modulo updater centrale")
    args = p.parse_args()

    if args.updater:
        out = delega_updater()
    else:
        out = verifica_freschezza()
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

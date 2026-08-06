#!/usr/bin/env python3
"""Calcolo contributi previdenziali DM10 (dipendenti).

Contributi a carico azienda e dipendente, aliquote INPS per categoria.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def calc_contributi(retribuzione: float, aliquote_path: str) -> dict:
    """Calcolo contributi DM10 da file aliquote JSON."""
    aliquote_file = Path(aliquote_path)
    if not aliquote_file.exists():
        print(json.dumps({"errore": f"File aliquote non trovato: {aliquote_path}"}))
        return {"errore": f"File aliquote non trovato: {aliquote_path}"}

    aliquote = json.loads(aliquote_file.read_text(encoding="utf-8"))
    aliquota_dipendente = aliquote.get("dipendente", 0.0919)
    aliquota_azienda = aliquote.get("azienda", 0.3019)

    contributo_dipendente = retribuzione * aliquota_dipendente
    contributo_azienda = retribuzione * aliquota_azienda
    totale = contributo_dipendente + contributo_azienda

    return {
        "retribuzione": retribuzione,
        "aliquota_dipendente": aliquota_dipendente,
        "aliquota_azienda": aliquota_azienda,
        "contributo_dipendente": round(contributo_dipendente, 2),
        "contributo_azienda": round(contributo_azienda, 2),
        "totale": round(totale, 2),
        "codice_dm10": "DM10",
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo contributi previdenziali DM10")
    p.add_argument("--retribuzione", type=float, required=True, help="Retribuzione lorda mensile")
    p.add_argument("--aliquote", type=str, required=True, help="Percorso al file JSON aliquote")
    args = p.parse_args()

    result = calc_contributi(args.retribuzione, args.aliquote)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

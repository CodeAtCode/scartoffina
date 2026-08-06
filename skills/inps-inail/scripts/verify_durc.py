#!/usr/bin/env python3
"""Verifica dello stato DURC (Documento Unico di Regolarita' Contributiva).

Usage: verify_durc.py --input data/durc.example.json
"""
import argparse
import json
import sys
from datetime import datetime, timedelta


VALIDITA_GIORNI = 120


def main() -> int:
    p = argparse.ArgumentParser(description="Verifica stato DURC")
    p.add_argument("--input", required=True)
    args = p.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        durc = json.load(f)

    data_rilascio = datetime.fromisoformat(durc["data_rilascio"])
    data_scadenza = data_rilascio + timedelta(days=VALIDITA_GIORNI)
    oggi = datetime.now()
    in_validita = oggi <= data_scadenza
    giorni_residui = (data_scadenza - oggi).days

    regolare = durc.get("esito_regolarita", "regolare") == "regolare"

    result = {
        "azienda": durc["azienda"],
        "data_rilascio": durc["data_rilascio"],
        "data_scadenza": data_scadenza.date().isoformat(),
        "in_validita": in_validita,
        "giorni_residui": giorni_residui,
        "esito_regolarita": durc.get("esito_regolarita", "regolare"),
        "regolare": regolare,
        "inps_regolare": durc.get("inps_regolare", True),
        "inail_regolare": durc.get("inail_regolare", True),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

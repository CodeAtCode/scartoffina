#!/usr/bin/env python3
"""Valida una dichiarazione di successione JSON.

Controlli: presenza eredi, quote sommano a 1, asse > passività, franchigie corrette.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def valida_successione(data: dict) -> dict:
    report = {"valido": True, "errori": [], "warning": [], "controlli": []}

    # 1. Eredi presenti
    eredi = data.get("eredi", [])
    if not eredi:
        report["errori"].append("Nessun erede dichiarato")
        report["valido"] = False
    else:
        report["controlli"].append(f"OK: {len(eredi)} eredi dichiarati")

    # 2. Quote sommano a 1
    totale_quote = sum(e.get("quota", 0) for e in eredi)
    if abs(totale_quote - 1.0) > 0.001:
        report["errori"].append(f"Quote eredi sommano a {totale_quote:.4f}, devono essere 1.0")
        report["valido"] = False
    else:
        report["controlli"].append(f"OK: quote eredi sommano a 1.0")

    # 3. Asse ereditario > 0
    asse = data.get("asse_ereditario", 0)
    if asse <= 0:
        report["errori"].append(f"Asse ereditario non valido: {asse}")
        report["valido"] = False
    else:
        report["controlli"].append(f"OK: asse ereditario {asse} EUR")

    # 4. Passività non superiore ad asse
    passivita = data.get("passivita", 0)
    if passivita > asse:
        report["warning"].append(f"Passività ({passivita}) superiore ad asse ({asse}) — verificare")

    # 5. Franchigie per grado
    FRANCHIGIA = {
        "coniuge_figli": 1_000_000.0,
        "fratelli_sorelle": 100_000.0,
        "altri_parenti_4_grado": 100_000.0,
        "altri": 0.0,
    }
    for erede in eredi:
        grado = erede.get("grado_parentela", "altri")
        if grado not in FRANCHIGIA:
            report["warning"].append(f"Erede {erede.get('nome', '?')}: grado '{grado}' non standard")

    # 6. De cuius presente
    dc = data.get("de_cuius", {})
    if not dc.get("nome"):
        report["errori"].append("De cuius: nome mancante")
        report["valido"] = False
    if not dc.get("data_decesso"):
        report["errori"].append("De cuius: data decesso mancante")
        report["valido"] = False

    return report


def main() -> int:
    p = argparse.ArgumentParser(description="Valida dichiarazione di successione JSON")
    p.add_argument("--input", required=True, help="File JSON dichiarazione")
    args = p.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    report = valida_successione(data)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["valido"] else 1


if __name__ == "__main__":
    sys.exit(main())

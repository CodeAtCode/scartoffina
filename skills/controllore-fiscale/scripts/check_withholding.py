#!/usr/bin/env python3
"""Calcolo della ritenuta d'acconto su compenso."""
from __future__ import annotations

import argparse
import json
import sys


def calcola_ritenuta(
    compenso: float,
    aliquota: float,
    tipo: str,
) -> dict:
    ritenuta = compenso * aliquota
    netto = compenso - ritenuta
    # per i dipendenti, la ritenuta è a titolo d'imposta; per gli altri è d'acconto
    titolo = "imposta" if tipo == "dipendente" else "acconto"
    return {
        "compenso_lordo": round(compenso, 2),
        "aliquota": aliquota,
        "tipo": tipo,
        "titolo": titolo,
        "ritenuta": round(ritenuta, 2),
        "compenso_netto": round(netto, 2),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Calcolo ritenuta d'acconto su compenso."
    )
    parser.add_argument(
        "--compenso", required=True, type=float, help="Compenso lordo in euro."
    )
    parser.add_argument(
        "--aliquota",
        type=float,
        default=0.20,
        help="Aliquota ritenuta (default: 0.20 = 20%%).",
    )
    parser.add_argument(
        "--tipo",
        default="autonomo",
        choices=["dipendente", "autonomo", "provvigioni"],
        help="Tipo rapporto (default: autonomo).",
    )
    args = parser.parse_args()

    result = calcola_ritenuta(args.compenso, args.aliquota, args.tipo)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

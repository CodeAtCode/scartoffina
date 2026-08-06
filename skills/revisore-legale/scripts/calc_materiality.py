#!/usr/bin/env python3
"""Calcolo della materialita' in revisione contabile (OIC 1, ISA 320).

Usage: calc_materiality.py --totale-attivo 1000000 --ricavi 2500000 --utile 50000
"""
import argparse
import json
import sys


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo materialità revisione")
    p.add_argument("--totale-attivo", type=float, required=True)
    p.add_argument("--ricavi", type=float, required=True)
    p.add_argument("--utile", type=float, required=True)
    args = p.parse_args()

    materialita_globale = max(
        round(args.totale_attivo * 0.015, 2),
        round(args.ricavi * 0.01, 2),
        round(abs(args.utile) * 0.05, 2) if args.utile > 0 else 0,
    )

    soglia_correzioni = round(materialita_globale * 0.75, 2)
    soglia_errori_trascurabili = round(materialita_globale * 0.05, 2)

    result = {
        "totale_attivo": args.totale_attivo,
        "ricavi": args.ricavi,
        "utile": args.utile,
        "materialita_globale": materialita_globale,
        "soglia_correzioni": soglia_correzioni,
        "soglia_errori_trascurabili": soglia_errori_trascurabili,
        "metodo": "metodo delle percentuali (OIC 1, ISA 320)",
        "base_applicazione": [
            f"1,5% totale attivo: {round(args.totale_attivo * 0.015, 2)}",
            f"1% ricavi: {round(args.ricavi * 0.01, 2)}",
            f"5% utile: {round(args.utile * 0.05, 2)}",
        ],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Calcolo premio INAIL annuo.

Usage: calc_premium_inail.py --retribuzione-annua 30000 --tasso-base 3.5 --classe-rischio 1.10
"""
import argparse
import json
import sys


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo premio INAIL annuo")
    p.add_argument("--retribuzione-annua", type=float, required=True)
    p.add_argument("--tasso-base", type=float, required=True, help="Tasso base per categoria INAIL")
    p.add_argument("--classe-rischio", type=float, default=1.0, help="Moltiplicatore classe rischio (default 1.0)")
    args = p.parse_args()

    tasso_effettivo = round(args.tasso_base * args.classe_rischio, 4)
    premio = round(args.retribuzione_annua * tasso_effettivo / 100, 2)

    result = {
        "retribuzione_annua": args.retribuzione_annua,
        "tasso_base": args.tasso_base,
        "classe_rischio": args.classe_rischio,
        "tasso_effettivo": tasso_effettivo,
        "premio_inail": premio,
        "scadenza-versamento": "16 febbraio dell'anno successivo",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

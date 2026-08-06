#!/usr/bin/env python3
"""Verifica requisiti pensione (vecchiaia / anticipata).

Usage: calc_pension.py --eta 67 --anni-contributi 20 --tipo vecchiaia
"""
import argparse
import json
import sys


REQUISITI = {
    "vecchiaia": {"eta_minima": 67, "contributi_minimi": 20},
    "anticipata": {"eta_minima": 41, "contributi_minimi": 42},
    "quota_102": {"eta_minima": 64, "contributi_minimi": 38},
    "ape_sociale": {"eta_minima": 62, "contributi_minimi": 36},
}


def main() -> int:
    p = argparse.ArgumentParser(description="Verifica requisiti pensionistici")
    p.add_argument("--eta", type=int, required=True)
    p.add_argument("--anni-contributi", type=int, required=True)
    p.add_argument("--tipo", choices=list(REQUISITI.keys()), required=True)
    args = p.parse_args()

    req = REQUISITI[args.tipo]
    eta_ok = args.eta >= req["eta_minima"]
    contributi_ok = args.anni_contributi >= req["contributi_minimi"]
    ammissibile = eta_ok and contributi_ok

    result = {
        "tipo_pensione": args.tipo,
        "eta": args.eta,
        "anni_contributi": args.anni_contributi,
        "eta_minima_richiesta": req["eta_minima"],
        "contributi_minimi_richiesti": req["contributi_minimi"],
        "eta_ok": eta_ok,
        "contributi_ok": contributi_ok,
        "ammissibile": ammissibile,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

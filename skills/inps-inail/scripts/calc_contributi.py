#!/usr/bin/env python3
"""Calcolo contributi INPS per lavoratore dipendente.

Usage: calc_contributi.py --retribuzione 2500 --gestione dipendenti --mese 12
"""
import argparse
import json
import sys


ALIQUOTE = {
    "dipendenti": {"datore": 0.3232, "lavatore": 0.0919},
    "artigiani": {"datore": 0.2268, "lavatore": 0.1688},
    "commercianti": {"datore": 0.2268, "lavatore": 0.1688},
    "separata": {"datore": 0.0, "lavatore": 0.2607},
}

MINIMO_MENSILE = 551.69
MASSIMALE_GG = 120.02


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo contributi INPS mensili")
    p.add_argument("--retribuzione", type=float, required=True)
    p.add_argument("--gestione", choices=list(ALIQUOTE.keys()), required=True)
    p.add_argument("--mese", type=int, default=1)
    args = p.parse_args()

    aliquote = ALIQUOTE[args.gestione]
    quota_datore = round(args.retribuzione * aliquote["datore"], 2)
    quota_lavatore = round(args.retribuzione * aliquote["lavatore"], 2)
    totale = round(quota_datore + quota_lavatore, 2)

    result = {
        "gestione": args.gestione,
        "retribuzione_mensile": args.retribuzione,
        "mese": args.mese,
        "quota_datore": quota_datore,
        "quota_lavatore": quota_lavatore,
        "totale_contributi": totale,
        "aliquota_datore": aliquote["datore"],
        "aliquota_lavatore": aliquote["lavatore"],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

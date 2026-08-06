#!/usr/bin/env python3
"""Calcolo indennita' NASpI (disoccupazione).

Usage: calc_naspi.py --retribuzione-media 1800 --settimane-contributi 52 --eta 45
"""
import argparse
import json
import sys


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo indennità NASpI")
    p.add_argument("--retribuzione-media", type=float, required=True)
    p.add_argument("--settimane-contributi", type=int, required=True, help="Settimane di contribuzione ultimi 4 anni")
    p.add_argument("--eta", type=int, default=40)
    args = p.parse_args()

    if args.settimane_contributi < 13:
        result = {
            "ammissibile": False,
            "motivo": "contributi insufficienti (minimo 13 settimane negli ultimi 12 mesi)",
            "settimane_contributi": args.settimane_contributi,
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    indennita_mensile = round(args.retribuzione_media * 0.75, 2)
    durata_mesi = max(args.settimane_contributi // 4, 0)

    result = {
        "ammissibile": True,
        "retribuzione_media_mensile": args.retribuzione_media,
        "percentuale_indennita": 0.75,
        "indennita_mensile": indennita_mensile,
        "durata_mesi": durata_mesi,
        "settimane_contributi": args.settimane_contributi,
        "eta": args.eta,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

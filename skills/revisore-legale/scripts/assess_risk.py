#!/usr/bin/env python3
"""Modello di rischio di revisione (ISA 200, ISA 315).

Rischio di revisione = Rischio inerente x Rischio di controllo x Rischio di individuazione

Usage: assess_risk.py --rischio-inerente 0.8 --rischio-controllo 0.5
"""
import argparse
import json
import sys


def main() -> int:
    p = argparse.ArgumentParser(description="Modello rischio di revisione")
    p.add_argument("--rischio-inerente", type=float, required=True, help="0-1")
    p.add_argument("--rischio-controllo", type=float, required=True, help="0-1")
    p.add_argument("--livello-garanzia", type=float, default=0.95, help="Livello di garanzia richiesto (0-1)")
    args = p.parse_args()

    rischio_revisione = 1 - args.livello_garanzia
    rischio_individuazione = round(
        rischio_revisione / (args.rischio_inerente * args.rischio_controllo), 4
    )
    rischio_individuazione = max(0.0, min(1.0, rischio_individuazione))

    if args.rischio_inerente >= 0.7:
        approccio = "sostanziale (rischio inerente elevato)"
    elif args.rischio_controllo >= 0.7:
        approccio = "combinato (controlli insufficienti)"
    else:
        approccio = "sistematico (controlli affidabili)"

    result = {
        "rischio_inerente": args.rischio_inerente,
        "rischio_controllo": args.rischio_controllo,
        "livello_garanzia": args.livello_garanzia,
        "rischio_revisione_accettabile": rischio_revisione,
        "rischio_individuazione": rischio_individuazione,
        "approccio_consigliato": approccio,
        "riferimento": "ISA 200, ISA 315",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

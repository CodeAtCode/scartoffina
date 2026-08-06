#!/usr/bin/env python3
"""Quadratura di una dichiarazione fiscale annuale."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def quadratura(dati: dict, anno: int) -> dict:
    redditi = dati.get("redditi", {})
    ritenute = dati.get("ritenute", {})
    crediti = dati.get("crediti", {})

    totale_redditi = sum(float(v) for v in redditi.values() if isinstance(v, (int, float)))
    totale_ritenute = sum(float(v) for v in ritenute.values() if isinstance(v, (int, float)))
    totale_crediti = sum(float(v) for v in crediti.values() if isinstance(v, (int, float)))

    imposta_dovuta = dati.get("imposta_dichiarata")
    differenze = []

    if imposta_dovuta is not None:
        # verifica: imposta dichiarata = imposta calcolata - ritenute - crediti
        imposta_calcolata = dati.get("imposta_calcolata", 0.0)
        atteso = imposta_calcolata - totale_ritenute - totale_crediti
        scarto = round(imposta_dovuta - atteso, 2)
        if abs(scarto) > 0.01:
            differenze.append(
                {
                    "campo": "imposta_dovuta",
                    "dichiarato": imposta_dovuta,
                    "atteso": round(atteso, 2),
                    "scarto": scarto,
                }
            )

    # verifica coerenza: ritenute <= redditi
    if totale_ritenute > totale_redditi:
        differenze.append(
            {
                "campo": "ritenute",
                "dichiarato": totale_ritenute,
                "atteso": f"<= {totale_redditi}",
                "scarto": round(totale_ritenute - totale_redditi, 2),
            }
        )

    result = {
        "anno": anno,
        "totale_redditi": round(totale_redditi, 2),
        "totale_ritenute": round(totale_ritenute, 2),
        "totale_crediti": round(totale_crediti, 2),
        "quadratura": len(differenze) == 0,
        "differenze": differenze,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Quadratura dichiarazione fiscale annuale."
    )
    parser.add_argument(
        "--input", required=True, help="Percorso file JSON della dichiarazione."
    )
    parser.add_argument(
        "--anno", required=True, type=int, help="Anno d'imposta."
    )
    args = parser.parse_args()

    dati = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = quadratura(dati, args.anno)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

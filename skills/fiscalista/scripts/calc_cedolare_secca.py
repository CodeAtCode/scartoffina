#!/usr/bin/env python3
"""Calcolo cedolare secca su locazioni 2025.

Aliquote:
- 10% abitazione principale (canone libero)
- 21% abitazione non principale (canone libero)
- 10% canone concordato (L. 431/1998)
- 21% locazione commerciale (non residenziale)
- 15% contratto di locazione per transitorio (DAL 2024, art. 3 c.1 DL 6/2024)
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass


@dataclass
class EsitoCedolare:
    canone_annuo: float
    aliquota: float
    imposta: float
    regime: str


def calcola_cedolare(canone: float, aliquota: float = 0.21, regime: str = "libero") -> dict:
    imposta = canone * aliquota
    esito = EsitoCedolare(
        canone_annuo=canone,
        aliquota=aliquota,
        imposta=round(imposta, 2),
        regime=regime,
    )
    d = asdict(esito)
    d["note"] = (
        "La cedolare secca si applica sull'intero canone, non ammette detrazioni, "
        "sostituisce IRPEF sui redditi fondiari."
    )
    return d


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo cedolare secca 2025")
    p.add_argument("--canone", type=float, required=True, help="Canone annuo (EUR)")
    p.add_argument("--aliquota", type=float, default=0.21, help="Aliquota (0.10, 0.15, 0.21)")
    p.add_argument("--regime", type=str, default="libero",
                   choices=["libero", "concordato", "transitorio"],
                   help="Tipo contratto")
    args = p.parse_args()

    risultato = calcola_cedolare(
        canone=args.canone,
        aliquota=args.aliquota,
        regime=args.regime,
    )
    print(json.dumps(risultato, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

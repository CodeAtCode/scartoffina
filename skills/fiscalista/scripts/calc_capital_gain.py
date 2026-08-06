#!/usr/bin/env python3
"""Calcolo capital gains (plusvalenze) 2025.

- Crypto-attivita: PF 26% (DL 21/2024, in vigore dal 2025)
- Azioni/quota partecipazione: PF 26%
- Partecipazione qualificata (>20% o >5% quotata): IMU sostitutiva 20%
- Riporto perdite: 4 esercizi successivi
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass


@dataclass
class EsitoCapitalGain:
    costo_acquisto: float
    valore_vendita: float
    plusvalenza: float
    tipo: str
    aliquota: float
    imposta: float


def calcola_capital_gain(
    acquisto: float,
    vendita: float,
    tipo: str = "crypto",
) -> dict:
    plusvalenza = vendita - acquisto
    if plusvalenza <= 0:
        return {
            "costo_acquisto": acquisto,
            "valore_vendita": vendita,
            "plusvalenza": round(plusvalenza, 2),
            "tipo": tipo,
            "aliquota": 0.0,
            "imposta": 0.0,
            "perdita_riportabile": round(abs(plusvalenza), 2),
            "riportabile_anni": 4,
        }

    aliquote = {"crypto": 0.26, "azioni": 0.26, "partecipazione_qualificata": 0.20}
    aliquota = aliquote.get(tipo, 0.26)
    imposta = plusvalenza * aliquota

    esito = EsitoCapitalGain(
        costo_acquisto=acquisto,
        valore_vendita=vendita,
        plusvalenza=round(plusvalenza, 2),
        tipo=tipo,
        aliquota=aliquota,
        imposta=round(imposta, 2),
    )
    d = asdict(esito)
    d["perdita_riportabile"] = 0.0
    d["riportabile_anni"] = 4
    d["monitoraggio_rw"] = tipo in ("crypto",) or tipo == "estero"
    return d


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo capital gains 2025")
    p.add_argument("--acquisto", type=float, required=True, help="Costo acquisto (EUR)")
    p.add_argument("--vendita", type=float, required=True, help="Valore vendita (EUR)")
    p.add_argument("--tipo", type=str, default="crypto",
                   choices=["crypto", "azioni", "partecipazione_qualificata"],
                   help="Tipo plusvalenza")
    args = p.parse_args()

    risultato = calcola_capital_gain(
        acquisto=args.acquisto,
        vendita=args.vendita,
        tipo=args.tipo,
    )
    print(json.dumps(risultato, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

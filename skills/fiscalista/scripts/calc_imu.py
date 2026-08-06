#!/usr/bin/env python3
"""Calcolo IMU 2025.

IMU = rendita catastale * moltiplicatore * aliquota.

Moltiplicatori (DL 504/1992 art. 13 c.5):
- A/2,A/3,A/4,A/5,A/6 (abitazioni): 160
- A/7 (box, autorimessa): 55
- A/1,A/8,A/9 (lusso): 76
- C/2,C/6,C/7 (pertinenze): 160
- C/1 (negozi, laboratori): 55
- D (immobili strumentali): 65
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass

MOLTIPLICATORI: dict[str, int] = {
    "A/1": 76, "A/8": 76, "A/9": 76,
    "A/2": 160, "A/3": 160, "A/4": 160, "A/5": 160, "A/6": 160, "A/7": 160,
    "A/11": 160,
    "B": 140,
    "C/1": 55,
    "C/2": 160, "C/3": 160, "C/4": 160, "C/5": 160, "C/6": 160, "C/7": 160,
    "D": 65,
}

COEFFICIENTE_ABITAZIONE = 1.05  # art. 13 c.5 DL 504/1992 per le abitazioni
COEFFICIENTE_BOX = 1.5


@dataclass
class EsitoIMU:
    rendita_catastale: float
    categoria: str
    moltiplicatore: int
    coefficiente: float
    valore_immobiliare: float
    aliquota: float
    imposta: float


def calcola_imu(
    rendita: float,
    categoria: str,
    aliquota: float,
    prima_casa: bool = False,
) -> dict:
    cat = categoria.upper().strip()
    molt = MOLTIPLICATORI.get(cat, 160)

    is_abitazione = cat.startswith("A/") and cat not in ("A/10",)
    coeff = COEFFICIENTE_ABITAZIONE if is_abitazione else 1.0

    # Prima casa: aliquota ridotta 0.5 per abitazioni principali
    alq = 0.005 if prima_casa and is_abitazione else aliquota

    valore = rendita * coeff * molt
    imposta = valore * alq

    esito = EsitoIMU(
        rendita_catastale=rendita,
        categoria=cat,
        moltiplicatore=molt,
        coefficiente=coeff,
        valore_immobiliare=round(valore, 2),
        aliquota=alq,
        imposta=round(imposta, 2),
    )
    d = asdict(esito)
    d["prima_casa"] = prima_casa
    return d


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo IMU 2025")
    p.add_argument("--rendita", type=float, required=True, help="Rendita catastale (EUR)")
    p.add_argument("--categoria", type=str, required=True, help="Categoria catastale (es. A2, A7, C1)")
    p.add_argument("--aliquota", type=float, required=True, help="Aliquota IMU (0-1, es. 0.0076)")
    p.add_argument("--prima-casa", action="store_true", help="Abitazione principale (aliquota 0.5%%)")
    args = p.parse_args()

    risultato = calcola_imu(
        rendita=args.rendita,
        categoria=args.categoria,
        aliquota=args.aliquota,
        prima_casa=args.prima_casa,
    )
    print(json.dumps(risultato, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

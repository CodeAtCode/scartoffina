#!/usr/bin/env python3
"""Calcolo sanzioni con ravvedimento operoso (D.Lgs. 472/1997 art. 13)."""
from __future__ import annotations

import argparse
import json
import sys

TASSO_LEGALE_2025 = 0.025  # 2,5%

# aliquota minima edittale per tipo di violazione (in percentuale dell'imposta)
SANZIONI_MINIME = {
    "omesso": 1.00,   # 100% (omesso versamento)
    "ritardato": 1.00,  # 100% (tardivo, ma ridotto con ravvedimento)
    "infedele": 1.00,  # 100% (infedele dichiarazione)
}

# coefficiente di riduzione per tipo di ravvedimento
RAVVEDIMENTO = {
    "sprint": 0.10,   # 1/10, entro 30 giorni
    "breve": 0.125,   # 1/8, entro 90 giorni
    "lungo": 0.111,   # 1/9, entro 1 anno
    "lungo_stra": 0.166,  # 1/6, entro termine accertamento
}


def calc_ravvedimento(
    imposta: float,
    giorni_ritardo: int,
    tipo_violazione: str,
) -> dict:
    minimo = SANZIONI_MINIME.get(tipo_violazione, 1.00)
    sanzione_base = imposta * minimo

    if giorni_ritardo <= 30:
        coeff = RAVVEDIMENTO["sprint"]
    elif giorni_ritardo <= 90:
        coeff = RAVVEDIMENTO["breve"]
    elif giorni_ritardo <= 365:
        coeff = RAVVEDIMENTO["lungo"]
    else:
        coeff = RAVVEDIMENTO["lungo_stra"]

    sanzione_ridotta = sanzione_base * coeff
    interessi = imposta * TASSO_LEGALE_2025 * (giorni_ritardo / 365)
    totale = imposta + sanzione_ridotta + interessi

    return {
        "imposta": round(imposta, 2),
        "giorni_ritardo": giorni_ritardo,
        "tipo_violazione": tipo_violazione,
        "sanzione_base": round(sanzione_base, 2),
        "coefficiente_riduzione": coeff,
        "sanzione_ridotta": round(sanzione_ridotta, 2),
        "interessi": round(interessi, 2),
        "totale": round(totale, 2),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Calcolo sanzioni con ravvedimento operoso."
    )
    parser.add_argument(
        "--imposta", required=True, type=float, help="Imposta dovuta in euro."
    )
    parser.add_argument(
        "--giorni-ritardo",
        required=True,
        type=int,
        help="Giorni di ritardo dalla scadenza.",
    )
    parser.add_argument(
        "--tipo",
        default="ritardato",
        choices=["omesso", "ritardato", "infedele"],
        help="Tipo di violazione (default: ritardato).",
    )
    args = parser.parse_args()

    result = calc_ravvedimento(args.imposta, args.giorni_ritardo, args.tipo)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

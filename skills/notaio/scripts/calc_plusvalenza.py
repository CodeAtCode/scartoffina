#!/usr/bin/env python3
"""Calcolo plusvalenze immobiliari (art. 67 TUIR).

Plusvalenza = prezzo vendita - costo acquisto - spese incremento - oneri accessorì.
Tassazione: 26% imposta sostitutiva (art. 67 c.1 lett. b TUIR).
"""
from __future__ import annotations

import argparse
import json
import sys


def calc_plusvalenza(
    prezzo_vendita: float,
    costo_acquisto: float,
    spese_acquisto: float = 0.0,
    spese_miglioramento: float = 0.0,
    anni_detenzione: int = 0,
) -> dict:
    """Calcolo plusvalenza immobiliare ex art. 67 c.1 lett. b TUIR.

    Esenzione: vendita entro 5 anni (costruzione) o mai (eredità).
    """
    base_costo = costo_acquisto + spese_acquisto + spese_miglioramento
    plusvalenza = prezzo_vendita - base_costo

    if plusvalenza <= 0:
        return {
            "prezzo_vendita": prezzo_vendita,
            "costo_acquisto": costo_acquisto,
            "spese_acquisto": spese_acquisto,
            "spese_miglioramento": spese_miglioramento,
            "base_costo": round(base_costo, 2),
            "plusvalenza": 0.0,
            "imposta_sostitutiva": 0.0,
            "esito": "minusvalenza — nessuna tassazione",
        }

    aliquota = 0.26  # art. 67 TUIR imposta sostitutiva
    imposta = plusvalenza * aliquota

    esito = {
        "prezzo_vendita": prezzo_vendita,
        "costo_acquisto": costo_acquisto,
        "spese_acquisto": spese_acquisto,
        "spese_miglioramento": spese_miglioramento,
        "base_costo": round(base_costo, 2),
        "plusvalenza": round(plusvalenza, 2),
        "aliquota": aliquota,
        "imposta_sostitutiva": round(imposta, 2),
        "anni_detenzione": anni_detenzione,
    }

    # Verifica esenzione
    if anni_detenzione >= 5:
        esito["esenzione"] = "Esenzione art. 67 c.1 lett. b TUIR: immobile detenuto oltre 5 anni"
        esito["imposta_sostitutiva"] = 0.0
    else:
        esito["obbligo_dichiarazione"] = "Modello RL plusvalenze entro 30 giugno dell'anno successivo"

    return esito


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo plusvalenza immobiliare (art. 67 TUIR)")
    p.add_argument("--prezzo", type=float, required=True, help="Prezzo di vendita")
    p.add_argument("--acquisto", type=float, required=True, help="Costo di acquisto")
    p.add_argument("--spese-acquisto", type=float, default=0.0, help="Spese in acquisto (notaio, provvigioni, imposte)")
    p.add_argument("--miglioramenti", type=float, default=0.0, help="Spese per incrementi")
    p.add_argument("--anni", type=int, default=0, help="Anni di detenzione")
    args = p.parse_args()

    result = calc_plusvalenza(args.prezzo, args.acquisto, args.spese_acquisto, args.miglioramenti, args.anni)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

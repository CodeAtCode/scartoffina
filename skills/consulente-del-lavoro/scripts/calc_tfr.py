#!/usr/bin/env python3
"""Calcolo TFR (Trattamento di Fine Rapporto, D.Lgs. 303/1989).

TFR annuo = 6,91% della retribuzione lorda.
Quote rivalutate per legge (art. 2120 c.c. + D.Lgs. 303/1989).
"""
from __future__ import annotations

import argparse
import json
import sys

ALIQUOTA_TFR = 0.0691
TASSA_IMPOSTA_SOSTITUTIVA = 0.17  # Art. 2120 c.c. comma 2


def calc_tfr(ral: float, anzianita: int, retribuzione_mensile: float) -> dict:
    """Calcolo TFR ex D.Lgs. 303/1989."""
    base_annua = ral * ALIQUOTA_TFR
    quota_annua = base_annua
    tfr_total = base_annua * anzianita

    # Rivalutazione media annua (1,5% + 75% inflazione ISTAT)
    tasso_rivalutazione = 0.015 + 0.75 * 0.02  # inflazione 2% media
    tfr_rivalutato = tfr_total * (1 + tasso_rivalutazione) ** anzianita

    # Imposta sostitutiva separata (se non anticipato)
    imposta = tfr_rivalutato * TASSA_IMPOSTA_SOSTITUTIVA
    tfr_netto = tfr_rivalutato - imposta

    # Anticipazione (entro 70%)
    anticipo_max = tfr_rivalutato * 0.70

    return {
        "ral": ral,
        "anzianita_anni": anzianita,
        "retribuzione_mensile": retribuzione_mensile,
        "aliquota_tfr": ALIQUOTA_TFR,
        "base_annua": round(base_annua, 2),
        "quota_annua": round(quota_annua, 2),
        "tfr_base": round(tfr_total, 2),
        "tasso_rivalutazione": round(tasso_rivalutazione, 4),
        "tfr_rivalutato": round(tfr_rivalutato, 2),
        "imposta_sostitutiva": round(imposta, 2),
        "tfr_netto": round(tfr_netto, 2),
        "anticipo": round(anticipo_max, 2),
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo TFR (D.Lgs. 303/1989)")
    p.add_argument("--ral", type=float, required=True, help="RAL lordo annuo")
    p.add_argument("--anzianita", type=int, required=True, help="Anni di anzianita")
    p.add_argument("--retribuzione-mensile", type=float, required=True, help="Retribuzione mensile lorda")
    args = p.parse_args()

    result = calc_tfr(args.ral, args.anzianita, args.retribuzione_mensile)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

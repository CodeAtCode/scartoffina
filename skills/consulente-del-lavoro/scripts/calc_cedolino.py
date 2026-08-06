#!/usr/bin/env python3
"""Calcolo cedolino paga mensile.

RAL lordo annuo -> IRPEF per scaglioni, addizionali regionali/comunali,
contributi INPS a carico del lavoratore (9,19%), TFR mensile (6,91%).
"""
from __future__ import annotations

import argparse
import json
import sys

# Scaglioni IRPEF 2025 (D.Lgs. 51/2024 riforma IRPEF)
IRPEF_SCAGLIONI = [
    (28000.0, 0.23),
    (50000.0, 0.35),
    (float("inf"), 0.43),
]

# Contributo INPS a carico dipendente (D.Lgs. 46/2024)
ALIQUOTA_INPS_DIPENDENTE = 0.0919
ALIQUOTA_TFR = 0.0691


def calc_irpef(imponibile: float) -> dict:
    """IRPEF a scaglioni (art. 11 TUIR)."""
    rimanente = imponibile
    imposta = 0.0
    dettaglio = []
    for limite, aliquota in IRPEF_SCAGLIONI:
        if rimanente <= 0:
            break
        base = min(rimanente, limite)
        quota = base * aliquota
        imposta += quota
        dettaglio.append({"base": round(base, 2), "aliquota": aliquota, "imposta": round(quota, 2)})
        rimanente -= base
    return {"imposta": round(imposta, 2), "dettaglio": dettaglio}


def calc_cedolino(ral: float, mesi: int = 13, figli: int = 0, regione: str = "") -> dict:
    """Calcolo cedolino paga mensile."""
    imponibile_annuo = ral
    contributi_annui = ral * ALIQUOTA_INPS_DIPENDENTE
    base_irpef = ral - contributi_annui
    irpef = calc_irpef(base_irpef)

    # Detrazioni per lavoro dipendente (art. 13 TUIR)
    detrazione_base = 0.0
    if base_irpef <= 15000:
        detrazione_base = 1955
    elif base_irpef <= 28000:
        detrazione_base = 1910 + 1198 * (28000 - base_irpef) / 13000
    elif base_irpef <= 50000:
        detrazione_base = 1910 * (50000 - base_irpef) / 22000
    detrazione_base = max(0.0, detrazione_base)

    # Detrazioni per figli a carico (art. 12 TUIR)
    detrazione_figli = figli * 1220 if figli <= 3 else (3 * 1220 + (figli - 3) * 950)
    detrazione_totale = detrazione_base + detrazione_figli
    irpef_netto = max(0.0, irpef["imposta"] - detrazione_totale)

    # Addizionale regionale (semplice: 1.5% media)
    addizionale_regionale = base_irpef * 0.015

    tfr_annuo = ral * ALIQUOTA_TFR
    netto_annuo = ral - contributi_annui - irpef_netto - addizionale_regionale
    netto_mensile = netto_annuo / mesi

    return {
        "ral": ral,
        "mesi": mesi,
        "figli": figli,
        "regione": regione or "non specificata",
        "contributi_inps_annui": round(contributi_annui, 2),
        "base_irpef": round(base_irpef, 2),
        "irpef_lorda": irpef["imposta"],
        "detrazione_lavoro": round(detrazione_base, 2),
        "detrazione_figli": round(detrazione_figli, 2),
        "irpef_netta": round(irpef_netto, 2),
        "addizionale_regionale": round(addizionale_regionale, 2),
        "tfr_annuo": round(tfr_annuo, 2),
        "netto_annuo": round(netto_annuo, 2),
        "netto_mensile": round(netto_mensile, 2),
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo cedolino paga mensile")
    p.add_argument("--ral", type=float, required=True, help="RAL lordo annuo")
    p.add_argument("--mesi", type=int, default=13, help="Mensilita (13 o 14)")
    p.add_argument("--figli", type=int, default=0, help="Numero figli a carico")
    p.add_argument("--regione", type=str, default="", help="Regione (per addizionale regionale)")
    args = p.parse_args()

    result = calc_cedolino(args.ral, args.mesi, args.figli, args.regione)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

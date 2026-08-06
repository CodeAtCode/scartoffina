#!/usr/bin/env python3
"""Calcolo NASpI (Nuova prestazione di Assicurazione Sociale per l'Impiego, D.Lgs. 150/2015).

Indennita mensile = 75% retribuzione media mensile per primi 3 mesi,
decrescita del 3% ogni mese successivo.
Durata massima: metà settimane contributive + mesi di lavoro.
"""
from __future__ import annotations

import argparse
import json
import sys

RIDUZIONE_MENSILE = 0.03  # Riduzione 3% ogni mese dopo i primi 3


def calc_naspi(retribuzione_media: float, settimane: int = 13, eta: int = 30) -> dict:
    """Calcolo NASpI ex D.Lgs. 150/2015."""
    # Importo iniziale: 75% retribuzione media (se <= 1300) o formula progressiva
    if retribuzione_media <= 1300:
        indennita_iniziale = retribuzione_media * 0.75
    else:
        indennita_iniziale = 975 + (retribuzione_media - 1300) * 0.25

    # Tetto massimo 1300 netti
    indennita_iniziale = min(indennita_iniziale, 1300)

    # Durata: 50% settimane contributive negli ultimi 12 mesi
    durata_settimane = settimane // 2
    durata_mesi = max(6, min(durata_settimane // 4, 24))

    # Decalage: 3% al mese dopo i primi 3
    mesi_pieni = min(3, durata_mesi)
    mesi_ridotti = max(0, durata_mesi - 3)
    indennita_media = indennita_iniziale
    for _ in range(mesi_ridotti):
        indennita_media *= (1 - RIDUZIONE_MENSILE)

    aliquota_media = indennita_media / indennita_iniziale if indennita_iniziale > 0 else 0

    # Franchigia 8% se età > 50 e durata sufficiente
    franchigia = 0
    if eta >= 50:
        franchigia = 1
        durata_mesi = min(durata_mesi + 12, 36)

    return {
        "retribuzione_media": retribuzione_media,
        "settimane_contributive": settimane,
        "eta": eta,
        "indennita_iniziale": round(indennita_iniziale, 2),
        "durata_mesi": durata_mesi,
        "aliquota_iniziale": 0.75,
        "aliquota_media": round(aliquota_media, 4),
        "indennita_media": round(indennita_media, 2),
        "franchigia_over50": franchigia,
        "settimane_utilizzabili": durata_settimane,
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo NASpI (D.Lgs. 150/2015)")
    p.add_argument("--retribuzione-media", type=float, required=True, help="Retribuzione media mensile ultimi 4 mesi")
    p.add_argument("--settimane", type=int, default=13, help="Settimane contributive ultimi 12 mesi")
    p.add_argument("--eta", type=int, default=30, help="Eta del lavoratore")
    args = p.parse_args()

    result = calc_naspi(args.retribuzione_media, args.settimane, args.eta)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

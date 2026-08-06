#!/usr/bin/env python3
"""Calcolo IRPEF deterministico anno 2025 (dichiarazione 2026).

Applica: scaglioni -> detrazione lavoro dipendente (art. 13 TUIR)
-> detrazioni carichi di famiglia (art. 12 TUIR) -> no-tax-area
-> addizionali regionali e comunali -> IRPEF netta.

Output JSON con ogni passaggio intermedio.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from typing import Any

# IRPEF 2025 - DPR 917/86 art. 11 (L. 213/2023 riforma IRPEF)
SCAGLIONI_2025: list[tuple[float, float, float]] = [
    (0.0, 28_000.0, 0.23),
    (28_000.0, 50_000.0, 0.35),
    (50_000.0, float("inf"), 0.43),
]

# Addizionali regionali 2025 (aliquota media per regione, %/100)
ADDIZIONALI_REGIONALI: dict[str, float] = {
    "abruzzo": 0.0210, "basilicata": 0.0243, "calabria": 0.0243,
    "campania": 0.0253, "emilia_romagna": 0.0190, "friuli_venezia_giulia": 0.0170,
    "lazio": 0.0202, "liguria": 0.0219, "lombardia": 0.0173,
    "marche": 0.0195, "molise": 0.0213, "piemonte": 0.0227,
    "puglia": 0.0253, "sardegna": 0.0173, "sicilia": 0.0289,
    "toscana": 0.0202, "trentino_alto_adige": 0.0186, "umbria": 0.0186,
    "valle_d_aosta": 0.0135, "veneto": 0.0185,
}

NO_TAX_AREA_SOGLIA = 8_500.0  # soglia no-tax-area single 2025


@dataclass
class EsitoScaglione:
    da: float
    a: float
    aliquota: float
    imponibile: float
    imposta: float


@dataclass
class EsitoIRPEF:
    reddito: float
    irpef_lorda: float
    scaglioni: list[EsitoScaglione] = field(default_factory=list)
    detrazione_lavoro: float = 0.0
    detrazione_coniuge: float = 0.0
    detrazione_figli: float = 0.0
    irpef_dopo_detrazioni: float = 0.0
    addizionale_regionale: float = 0.0
    addizionale_comunale: float = 0.0
    irpef_netta: float = 0.0
    no_tax_area: bool = False


def calcola_scaglioni(reddito: float) -> tuple[float, list[EsitoScaglione]]:
    """Calcola IRPEF lorda per scaglioni cumulativi."""
    irpef = 0.0
    out: list[EsitoScaglione] = []
    for da, a, aliquota in SCAGLIONI_2025:
        if reddito <= da:
            break
        imponibile = min(reddito, a) - da
        if imponibile <= 0:
            continue
        imposta = imponibile * aliquota
        irpef += imposta
        out.append(EsitoScaglione(da, a, aliquota, imponibile, imposta))
    return irpef, out


def detrazione_lavoro_dipendente(reddito: float) -> float:
    """Art. 13 TUIR - detrazione per redditi da lavoro dipendente 2025."""
    if reddito <= 15_000.0:
        return 1_880.0
    if reddito <= 28_000.0:
        return 1_910.0 + 1_910.0 * (28_000.0 - reddito) / 13_000.0
    if reddito <= 50_000.0:
        return 1_910.0 * (50_000.0 - reddito) / 22_000.0
    return 0.0


def detrazione_coniuge(reddito: float) -> float:
    """Art. 12 c.1 TUIR - detrazione per coniuge a carico 2025."""
    if reddito > 80_000.0:
        return 0.0
    if reddito <= 15_000.0:
        return 690.0
    return 690.0 * (80_000.0 - reddito) / 65_000.0


def detrazione_figli(reddito: float, n_figli: int) -> float:
    """Art. 12 c.1 TUIR - detrazione per figli a carico 2025.

    Semplificata: per il primo figlio 800/950 (se 4 figli), successivi 900/1200.
    Tapering lineare da 95.000 EUR.
    """
    if n_figli <= 0 or reddito >= 95_000.0:
        return 0.0
    base = 950.0 if n_figli >= 4 else 800.0
    per_successivo = 1_200.0 if n_figli >= 4 else 900.0
    totale = base + max(0, n_figli - 1) * per_successivo
    fattore = (95_000.0 - reddito) / 95_000.0
    return totale * max(0.0, fattore)


def calcola_irpef(
    reddito: float,
    coniuge: int = 0,
    figli: int = 0,
    regione: str | None = None,
    comune: str | None = None,
    aliquota_comunale: float = 0.0,
) -> dict[str, Any]:
    """Calcolo IRPEF completo con breakdown."""
    irpef_lorda, scaglioni = calcola_scaglioni(reddito)

    d_lavoro = detrazione_lavoro_dipendente(reddito) if reddito > 0 else 0.0
    d_coniuge = detrazione_coniuge(reddito) if coniuge else 0.0
    d_figli = detrazione_figli(reddito, figli) if figli else 0.0
    detrazioni = d_lavoro + d_coniuge + d_figli

    irpef_dopo = max(0.0, irpef_lorda - detrazioni)

    no_tax = reddito > 0 and reddito <= NO_TAX_AREA_SOGLIA and irpef_dopo == 0.0

    add_reg = 0.0
    if regione:
        alq = ADDIZIONALI_REGIONALI.get(regione.lower().replace("-", "_").replace(" ", "_"), 0.0)
        add_reg = irpef_lorda * alq

    add_com = irpef_lorda * aliquota_comunale if aliquota_comunale else 0.0

    netta = irpef_dopo + add_reg + add_com

    esito = EsitoIRPEF(
        reddito=reddito,
        irpef_lorda=round(irpef_lorda, 2),
        scaglioni=scaglioni,
        detrazione_lavoro=round(d_lavoro, 2),
        detrazione_coniuge=round(d_coniuge, 2),
        detrazione_figli=round(d_figli, 2),
        irpef_dopo_detrazioni=round(irpef_dopo, 2),
        addizionale_regionale=round(add_reg, 2),
        addizionale_comunale=round(add_com, 2),
        irpef_netta=round(netta, 2),
        no_tax_area=no_tax,
    )

    d = asdict(esito)
    d["scaglioni"] = [asdict(s) for s in scaglioni]
    d["regione"] = regione
    d["comune"] = comune
    d["aliquota_addizionale_comunale"] = aliquota_comunale
    return d


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo IRPEF 2025 deterministico")
    p.add_argument("--reddito", type=float, required=True, help="Reddito complessivo netto (EUR)")
    p.add_argument("--coniuge", type=int, default=0, choices=[0, 1], help="1 se coniuge a carico")
    p.add_argument("--figli", type=int, default=0, help="Numero figli a carico")
    p.add_argument("--regione", type=str, default=None, help="Regione (es. lombardia)")
    p.add_argument("--comune", type=str, default=None, help="Comune (informativo)")
    p.add_argument("--aliquota-comunale", type=float, default=0.0, help="Aliquota addiz. comunale (0-1)")
    args = p.parse_args()

    risultato = calcola_irpef(
        reddito=args.reddito,
        coniuge=args.coniuge,
        figli=args.figli,
        regione=args.regione,
        comune=args.comune,
        aliquota_comunale=args.aliquota_comunale,
    )
    print(json.dumps(risultato, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

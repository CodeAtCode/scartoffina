#!/usr/bin/env python3
"""Calcoli deterministici per la skill amministratore-condominio.

Comandi:
  riparto        Riparto spese in millesimi
  bilancio       Verifica quadratura bilancio preventivo/consuntivo
  maggioranze    Verifica raggiungimento maggioranze assembleari
  mora           Calcolo interessi su mora
  riserva        Verifica fondo di riserva (min 3% preventivo)
"""
from __future__ import annotations

import argparse
import json
import sys


def calc_riparto(spesa_totale: float, millesimi_condomino: float, tipo: str = "generale") -> dict:
    """Riparto spese in millesimi (art. 1123 c.c.)."""
    quota = spesa_totale * millesimi_condomino / 1000.0
    return {
        "spesa_totale": spesa_totale,
        "millesimi_condomino": millesimi_condomino,
        "tipo_tabella": tipo,
        "quota_condomino": round(quota, 2),
        "formula": f"({spesa_totale} × {millesimi_condomino}) / 1000",
        "riferimento_normativo": "art. 1123 c.c." if tipo == "generale" else "art. 1124 c.c. (ascensore) / art. 1120 c.c. (riscaldamento)",
    }


def calc_bilancio(entrate: list[dict], uscite: list[dict]) -> dict:
    """Verifica quadratura bilancio."""
    totale_entrate = sum(e.get("importo", 0) for e in entrate)
    totale_uscite = sum(u.get("importo", 0) for u in uscite)
    saldo = totale_entrate - totale_uscite
    return {
        "totale_entrate": round(totale_entrate, 2),
        "totale_uscite": round(totale_uscite, 2),
        "saldo": round(saldo, 2),
        "stato": "pareggio" if abs(saldo) < 0.01 else ("avanzo" if saldo > 0 else "disavanzo"),
    }


def calc_maggioranze(millesimi_presenti: float, millesimi_favorevoli: float, tipo_delibera: str = "ordinaria") -> dict:
    """Verifica raggiungimento maggioranze assembleari (art. 1136 c.c.)."""
    SOGLIE = {
        "ordinaria": {"prima": 500.0, "seconda": 333.0, "descrizione": "maggioranza semplice (500/1000 prima, 333/1000 seconda)"},
        "qualificata": {"prima": 666.0, "seconda": 466.0, "descrizione": "2/3 (666/1000 prima, 466/1000 seconda)"},
        "quattro_quinti": {"prima": 800.0, "seconda": 533.0, "descrizione": "4/5 (800/1000 prima, 533/1000 seconda)"},
        "cinque_sesti": {"prima": 833.0, "seconda": 555.0, "descrizione": "5/6 (833/1000 prima, 555/1000 seconda)"},
        "unanimita": {"prima": 1000.0, "seconda": 1000.0, "descrizione": "unanimità (1000/1000)"},
    }
    soglia = SOGLIE.get(tipo_delibera, SOGLIE["ordinaria"])
    raggiunta_prima = millesimi_favorevoli >= soglia["prima"]
    raggiunta_seconda = millesimi_favorevoli >= soglia["seconda"]
    return {
        "tipo_delibera": tipo_delibera,
        "millesimi_presenti": millesimi_presenti,
        "millesimi_favorevoli": millesimi_favorevoli,
        "soglia_prima": soglia["prima"],
        "soglia_seconda": soglia["seconda"],
        "raggiunta_prima_convocazione": raggiunta_prima,
        "raggiunta_seconda_convocazione": raggiunta_seconda,
        "descrizione": soglia["descrizione"],
        "riferimento_normativo": "art. 1136 c.c.",
    }


def calc_interessi_mora(importo: float, giorni_ritardo: int, tasso: float = 0.03) -> dict:
    """Interessi legali su morosità condominiale."""
    interessi = importo * tasso * giorni_ritardo / 365.0
    return {
        "importo": importo,
        "giorni_ritardo": giorni_ritardo,
        "tasso_interesse": tasso,
        "interessi": round(interessi, 2),
        "totale_dovuto": round(importo + interessi, 2),
    }


def calc_fondo_riserva(preventivo_annuale: float, fondo_attuale: float = 0.0) -> dict:
    """Verifica fondo di riserva (min 3% preventivo, max 5%)."""
    minimo = preventivo_annuale * 0.03
    massimo = preventivo_annuale * 0.05
    return {
        "preventivo_annuale": preventivo_annuale,
        "fondo_attuale": fondo_attuale,
        "fondo_minimo_obbligatorio": round(minimo, 2),
        "fondo_massimo": round(massimo, 2),
        "sotto_soglia": fondo_attuale < minimo,
        "integrazione_necessaria": round(max(0.0, minimo - fondo_attuale), 2),
        "riferimento_normativo": "L. 220/2012 (fondo riserva obbligatorio)",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Calcoli deterministici skill amministratore-condominio")
    sub = parser.add_subparsers(dest="comando", required=True)

    p_rip = sub.add_parser("riparto", help="Riparto spese in millesimi")
    p_rip.add_argument("--spesa", type=float, required=True)
    p_rip.add_argument("--millesimi", type=float, required=True)
    p_rip.add_argument("--tipo", default="generale", choices=["generale", "scala", "riscaldamento", "ascensore"])

    p_bil = sub.add_parser("bilancio", help="Verifica quadratura bilancio")
    p_bil.add_argument("--entrate", required=True, help="JSON lista entrate")
    p_bil.add_argument("--uscite", required=True, help="JSON lista uscite")

    p_mag = sub.add_parser("maggioranze", help="Verifica maggioranze assembleari")
    p_mag.add_argument("--presenti", type=float, required=True)
    p_mag.add_argument("--favorevoli", type=float, required=True)
    p_mag.add_argument("--tipo", default="ordinaria",
                       choices=["ordinaria", "qualificata", "quattro_quinti", "cinque_sesti", "unanimita"])

    p_mora = sub.add_parser("mora", help="Calcolo interessi su mora")
    p_mora.add_argument("--importo", type=float, required=True)
    p_mora.add_argument("--giorni", type=int, required=True)
    p_mora.add_argument("--tasso", type=float, default=0.03)

    p_ris = sub.add_parser("riserva", help="Verifica fondo di riserva")
    p_ris.add_argument("--preventivo", type=float, required=True)
    p_ris.add_argument("--attuale", type=float, default=0.0)

    args = parser.parse_args()

    if args.comando == "riparto":
        out = calc_riparto(args.spesa, args.millesimi, args.tipo)
    elif args.comando == "bilancio":
        entrate = json.loads(args.entrate)
        uscite = json.loads(args.uscite)
        out = calc_bilancio(entrate, uscite)
    elif args.comando == "maggioranze":
        out = calc_maggioranze(args.presenti, args.favorevoli, args.tipo)
    elif args.comando == "mora":
        out = calc_interessi_mora(args.importo, args.giorni, args.tasso)
    elif args.comando == "riserva":
        out = calc_fondo_riserva(args.preventivo, args.attuale)
    else:
        parser.print_help()
        return 1

    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Genera checklist di audit fiscale per un'azienda."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


VOCI_AUDIT = [
    "Registrazione fatture di acquisto entro termine",
    "Registrazione fatture di vendita entro 15 giorni",
    "Liquidazione IVA periodica versata nei termini",
    "Dichiarazione IVA annuale presentata",
    "Modello 770 presentato dal sostituto di imposta",
    "Modello Unico presentato dai titolari",
    "Ravvedimento operoso per ritardi identificati",
    "Verifica studi di settore (GERICO) eseguita",
    "Archiviazione fatture elettroniche (SDI)",
    "Comunicazione delle operazioni 2025 (esterometro)",
    "Verifica reverse charge (subappalto, rottami)",
    "Controllo plafond esportatore abituale",
    "Adempimenti antiriciclaggio (SUS)",
    "Verifica ritenute d'acconto operate",
    "Adempimenti INPS/INAIL (F24)",
    "Controllo coerenza con contabilità",
    "Verifica studi di settore: adeguamento spontaneo",
    "Archiviazione dichiarazioni precedenti (10 anni)",
]


def genera_checklist(dati_azienda: dict, anno: int) -> dict:
    settori = dati_azienda.get("settori", ["generale"])
    soglia_ricavi = dati_azienda.get("ricavi", 0) > 400000
    checklist = []
    for voce in VOCI_AUDIT:
        stato = "da_verificare"
        note = ""
        # IVA trimestrale vs mensile dipende dai ricavi
        if "IVA periodica" in voce and soglia_ricavi:
            note = "Liquidazione mensile (ricavi > 400k euro)"
        elif "antiriciclaggio" in voce and "professionista" in settori:
            note = "Obbligo antiriciclaggio applicabile"
        checklist.append({"voce": voce, "stato": stato, "note": note})

    return {
        "azienda": dati_azienda.get("denominazione", "N/D"),
        "anno": anno,
        "totale_voci": len(checklist),
        "checklist": checklist,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Genera checklist di audit fiscale per azienda."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Percorso file JSON con dati azienda.",
    )
    parser.add_argument(
        "--anno", required=True, type=int, help="Anno di audit."
    )
    args = parser.parse_args()

    dati_azienda = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = genera_checklist(dati_azienda, args.anno)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

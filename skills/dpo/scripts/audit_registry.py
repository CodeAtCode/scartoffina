#!/usr/bin/env python3
"""Genera checklist di audit per il registro dei trattamenti (art. 30 GDPR)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


VOCI_AUDIT = [
    "Identificazione titolare/responsabile",
    "Finalità di trattamento documentata per ogni voce",
    "Categorie di interessati specificate",
    "Categorie di dati specificate",
    "Categorie di destinatari elencate",
    "Trasferimenti extra-UE mappati (se presenti)",
    "Base giuridica identificata per ogni trattamento",
    "Termini di cancellazione definiti",
    "Misure di sicurezza tecniche e organizzative descritte",
    "Aggiornamento registro entro 48h da modifiche",
    "Designazione DPO (se obbligatoria) documentata",
    "Conservazione registro disponibile per autorità",
]


def genera_audit(registro: dict) -> dict:
    trattamenti = registro.get("trattamenti", [])
    voci_verificate = []
    for voce in VOCI_AUDIT:
        stato = "da_verificare"
        note = ""
        if "Finalità" in voce:
            completi = sum(1 for t in trattamenti if t.get("finalita"))
            note = f"{completi}/{len(trattamenti)} trattamenti con finalità"
        elif "Base giuridica" in voce:
            completi = sum(1 for t in trattamenti if t.get("base_giuridica"))
            note = f"{completi}/{len(trattamenti)} con base giuridica"
        elif "Trasferimenti" in voce:
            extra_ue = [t for t in trattamenti if t.get("trasferimento_extra_ue")]
            note = f"{len(extra_ue)} trattamenti con trasferimenti extra-UE"
        voci_verificate.append({"voce": voce, "stato": stato, "note": note})

    return {
        "titolare": registro.get("titolare", "N/D"),
        "totale_trattamenti": len(trattamenti),
        "voci_audit": len(voci_verificate),
        "checklist": voci_verificate,
        "esito": "audit_da_completare",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Genera audit checklist per registro art. 30 GDPR.")
    parser.add_argument("--input", required=True, help="Percorso file JSON registro.")
    args = parser.parse_args()

    registro = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = genera_audit(registro)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

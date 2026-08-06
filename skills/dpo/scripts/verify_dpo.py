#!/usr/bin/env python3
"""Verifica l'obbligo di designazione del DPO (art. 37 GDPR)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def verifica_obbligo(azienda: dict) -> dict:
    tipo_org = azienda.get("tipo_organizzazione", "")
    settori = azienda.get("settori", [])
    numero_interessati = azienda.get("numero_interessati", 0)
    categorie_particolari = azienda.get("categorie_particolari", [])
    monitoraggio_sistematico = azienda.get("monitoraggio_sistematico_larga_scala", False)

    obblighi = []
    if tipo_org == "pubblica_amministrazione":
        obblighi.append("Autorità pubblica o organismo pubblico (art. 37 c. 1 a)")

    if monitoraggio_sistematico:
        obblighi.append("Monitoraggio sistematico su larga scala (art. 37 c. 1 b)")

    if categorie_particolari and numero_interessati > 0:
        obblighi.append(f"Trattamento su larga scala di categorie particolari (art. 37 c. 1 b): {', '.join(categorie_particolari)}")

    settori_alto_rischio = {"sanita", "finanziario", "assicurativo", "telecomunicazioni", "trasporti"}
    settori_rilevanti = set(settori) & settori_alto_rischio
    if settori_rilevanti:
        obblighi.append(f"Settore ad alto rischio: {', '.join(settori_rilevanti)}")

    obbligo_designazione = len(obblighi) > 0
    dpo_designato = azienda.get("dpo_designato", False)

    avvisi = []
    if obbligo_designazione and not dpo_designato:
        avvisi.append("OBBLIGO designazione DPO non adempiuto: sanzione art. 83 c. 4 GDPR")
    if not obbligo_designazione and dpo_designato:
        avvisi.append("Designazione volontaria: DPO non obbligatorio ma consentita (art. 37 c. 5)")

    return {
        "denominazione": azienda.get("denominazione", "N/D"),
        "tipo_organizzazione": tipo_org,
        "obbligo_designazione_dpo": obbligo_designazione,
        "dpo_designato": dpo_designato,
        "motivi_obbligo": obblighi if obbligo_designazione else [],
        "avvisi": avvisi,
        "riferimento_normativo": "art. 37 GDPR + art. 2-sexies c. 1 Codice privacy",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verifica obbligo designazione DPO art. 37 GDPR.")
    parser.add_argument("--input", required=True, help="Percorso file JSON azienda.")
    args = parser.parse_args()

    azienda = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = verifica_obbligo(azienda)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

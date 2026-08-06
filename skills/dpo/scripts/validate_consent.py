#!/usr/bin/env python3
"""Valida un record di consenso GDPR (art. 7)."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path


def valida(consenso: dict) -> dict:
    errori = []
    avvisi = []

    obbligatori = ["interessato_id", "finalita", "base_giuridica", "data_raccolta", "modalita"]
    for campo in obbligatori:
        if campo not in consenso:
            errori.append(f"Campo obbligatorio mancante: {campo}")

    base = consenso.get("base_giuridica", "")
    if base not in ("consenso", "contratto", "obbligo_legale", "interesse_vitale", "interesse_pubblico", "legittimo_interesse"):
        errori.append(f"Base giuridica non valida: {base}")

    if base == "consenso":
        if not consenso.get("prova_consenso"):
            errori.append("Base consenso richiede prova_consenso")
        if consenso.get("revocabile") is False:
            avvisi.append("Consenso non revocabile: verificare legittimità")

    try:
        data_raccolta = date.fromisoformat(consenso["data_raccolta"])
        oggi = date.today()
        eta_giorni = (oggi - data_raccolta).days
        if eta_giorni > 730:
            avvisi.append(f"Consenso raccolto {eta_giorni} giorni fa: verificare rinnovo")
    except (KeyError, ValueError):
        errori.append("data_raccolta non valida (formato YYYY-MM-DD)")

    categorie_particolari = consenso.get("categorie_particolari", [])
    if categorie_particolari:
        if base == "consenso" and not consenso.get("consenso_explicito"):
            errori.append("Categorie particolari (art. 9) richiedono consenso esplicito")

    valido = len(errori) == 0
    return {
        "interessato_id": consenso.get("interessato_id", "N/D"),
        "finalita": consenso.get("finalita", "N/D"),
        "valido": valido,
        "errori": errori,
        "avvisi": avvisi,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida record di consenso GDPR art. 7.")
    parser.add_argument("--input", required=True, help="Percorso file JSON consenso.")
    args = parser.parse_args()

    consenso = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = valida(consenso)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

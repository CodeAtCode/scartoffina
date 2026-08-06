#!/usr/bin/env python3
"""Generazione relazione di revisione (OIC 12, ISA 700).

Usage: generate_report.py --input data/relazione.example.json
"""
import argparse
import json
import sys


def main() -> int:
    p = argparse.ArgumentParser(description="Generazione relazione di revisione")
    p.add_argument("--input", required=True)
    args = p.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        dati = json.load(f)

    opinioni = {
        "senza_osservazioni": "i conti danno un quadro fedele",
        "con_osservazioni": "i conti danno un quadro fedele, fatta eccezione per",
        "avverse": "i conti non danno un quadro fedele",
        "mancata": "impossibile esprimere un giudizio",
    }

    tipo = dati.get("tipo_giudizio", "senza_osservazioni")
    giudizio = opinioni.get(tipo, "non definito")

    result = {
        "azienda": dati["azienda"]["denominazione"],
        "esercizio": dati["azienda"]["esercizio"],
        "revisore": dati.get("revisore", {}),
        "tipo_giudizio": tipo,
        "giudizio_testuale": giudizio,
        "riferimento_normativo": "OIC 12; ISA 700; D.Lgs. 39/2010",
        "firma": dati.get("firma", ""),
        "data_relazione": dati.get("data_relazione", ""),
        "allegati": [
            "Relazione al Consiglio di Amministrazione",
            "Lettera di incarico",
        ],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

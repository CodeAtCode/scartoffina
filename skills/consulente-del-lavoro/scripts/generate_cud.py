#!/usr/bin/env python3
"""Generazione CU (Certificazione Unica) da dati JSON.

Legge un file JSON con dati lavoratore e retribuzioni, produce CU in formato JSON.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def generate_cud(input_path: str, output_path: str) -> dict:
    """Genera CU da file JSON di input."""
    input_file = Path(input_path)
    if not input_file.exists():
        return {"errore": f"File input non trovato: {input_path}"}

    dati = json.loads(input_file.read_text(encoding="utf-8"))

    cud = {
        "anno": dati.get("anno", 2025),
        "lavoratore": {
            "codice_fiscale": dati.get("codice_fiscale", ""),
            "cognome": dati.get("cognome", ""),
            "nome": dati.get("nome", ""),
            "data_nascita": dati.get("data_nascita", ""),
            "comune_nascita": dati.get("comune_nascita", ""),
            "comune_residenza": dati.get("comune_residenza", ""),
            "indirizzo": dati.get("indirizzo", ""),
        },
        "datore_lavoro": {
            "ragione_sociale": dati.get("ragione_sociale", ""),
            "codice_fiscale": dati.get("cf_datore", ""),
            "piva": dati.get("piva_datore", ""),
            "posizione_inps": dati.get("posizione_inps", ""),
        },
        "dati_retributivi": {
            "reddito_dipendente": dati.get("reddito_dipendente", 0),
            "reddito_assimilato": dati.get("reddito_assimilato", 0),
            "ritenute_irpef": dati.get("ritenute_irpef", 0),
            "contributi_previdenziali": dati.get("contributi_previdenziali", 0),
            "addizionali_regionale": dati.get("addizionale_regionale", 0),
            "addizionale_comunale": dati.get("addizionale_comunale", 0),
        },
        "dipendenti_altri_dati": {
            "giorni_lavoro": dati.get("giorni_lavoro", 365),
            "mesi_lavoro": dati.get("mesi_lavoro", 12),
            "tipologia_rapporto": dati.get("tipologia_rapporto", "tempo indeterminato"),
            "tipo_retribuzione": dati.get("tipo_retribuzione", "mensile"),
        },
    }

    output_file = Path(output_path)
    output_file.write_text(json.dumps(cud, indent=2, ensure_ascii=False), encoding="utf-8")
    return {
        "esito": "ok",
        "file_generato": str(output_file),
        "anno": cud["anno"],
        "lavoratore": f"{cud['lavoratore']['cognome']} {cud['lavoratore']['nome']}",
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Genera CU da dati JSON")
    p.add_argument("--input", type=str, required=True, help="Percorso file JSON input")
    p.add_argument("--output", type=str, required=True, help="Percorso file JSON output")
    args = p.parse_args()

    result = generate_cud(args.input, args.output)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

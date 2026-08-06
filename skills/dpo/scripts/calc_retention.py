#!/usr/bin/env python3
"""Calcola il periodo di conservazione dei dati secondo tipologia di trattamento."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta


TABELLA_CONSERVAZIONE = {
    "amministrativo_fiscale": {"anni": 10, "riferimento": "art. 2220 c.c. + D.P.R. 600/1973"},
    "paghe_stipendi": {"anni": 10, "riferimento": "D.Lgs. 196/2003 art. 2-sexies"},
    "video_sorveglianza": {"giorni": 7, "riferimento": "Garante Privacy - Provvedimento 8 aprile 2010"},
    "cookie_tecnici": {"giorni": 0, "riferimento": "Necessari (sessione)"},
    "cookie_analitici": {"mesi": 12, "riferimento": "Linee guida cookie Garante 2021"},
    "cookie_profilazione": {"mesi": 6, "riferimento": "Linee guida cookie Garante 2021"},
    "curriculum_candidati": {"mesi": 24, "riferimento": "Garante Privacy - Pratica selezione personale"},
    "dati_sanitari": {"anni": 15, "riferimento": "D.Lgs. 196/2003 art. 2-sexies + DM sanità"},
    "fatture_elettroniche": {"anni": 10, "riferimento": "D.P.R. 633/1972 art. 39 + DM 17 giugno 2004"},
    "log_sistema": {"giorni": 30, "riferimento": "Misure minime sicurezza - Allegato B Garante"},
    "marketing_direct": {"mesi": 24, "riferimento": "Garante Privacy - Pratica marketing"},
}


def calcola(tipo_trattamento: str, data_raccolta: str) -> dict:
    if tipo_trattamento not in TABELLA_CONSERVAZIONE:
        return {
            "tipo_trattamento": tipo_trattamento,
            "errore": f"Tipologia non supportata. Valide: {', '.join(TABELLA_CONSERVAZIONE.keys())}",
        }

    regola = TABELLA_CONSERVAZIONE[tipo_trattamento]
    try:
        inizio = date.fromisoformat(data_raccolta)
    except ValueError:
        return {
            "tipo_trattamento": tipo_trattamento,
            "errore": "data_raccolta non valida (formato YYYY-MM-DD)",
        }

    if "anni" in regola:
        scadenza = inizio.replace(year=inizio.year + regola["anni"])
        unita = "anni"
        valore = regola["anni"]
    elif "mesi" in regola:
        scadenza = inizio + timedelta(days=regola["mesi"] * 30)
        unita = "mesi"
        valore = regola["mesi"]
    else:
        scadenza = inizio + timedelta(days=regola["giorni"])
        unita = "giorni"
        valore = regola["giorni"]

    oggi = date.today()
    giorni_rimanenti = (scadenza - oggi).days
    stato = "attivo" if giorni_rimanenti > 0 else "scaduto_da_cancellare"

    return {
        "tipo_trattamento": tipo_trattamento,
        "data_raccolta": data_raccolta,
        "periodo_conservazione": f"{valore} {unita}",
        "data_scadenza_cancellazione": scadenza.isoformat(),
        "giorni_rimanenti": giorni_rimanenti,
        "stato": stato,
        "riferimento_normativo": regola["riferimento"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Calcola periodo conservazione dati GDPR.")
    parser.add_argument("--tipo-trattamento", required=True, help="Tipologia di trattamento.")
    parser.add_argument("--data-raccolta", required=True, help="Data raccolta (YYYY-MM-DD).")
    args = parser.parse_args()

    result = calcola(args.tipo_trattamento, args.data_raccolta)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

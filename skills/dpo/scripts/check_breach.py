#!/usr/bin/env python3
"""Verifica le scadenze di notifica per un data breach (art. 33-34 GDPR)."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta


SCADENZA_GARANTE_ORE = 72


MATRICE_RISCHIO = {
    ("dati_personali", "basso"): "notifica_non_obbligatoria",
    ("dati_personali", "medio"): "notifica_garante_consigliata",
    ("dati_personali", "alto"): "notifica_garante_obbligatoria",
    ("dati_particolari", "basso"): "notifica_garante_obbligatoria",
    ("dati_particolari", "medio"): "notifica_garante_e_interessati",
    ("dati_particolari", "alto"): "notifica_garante_e_interessati",
    ("dati_finanziari", "basso"): "notifica_garante_consigliata",
    ("dati_finanziari", "medio"): "notifica_garante_obbligatoria",
    ("dati_finanziari", "alto"): "notifica_garante_e_interessati",
}


def valuta(data_breach: str, tipo: str, numero_interessati: int = 0) -> dict:
    try:
        scoperta = datetime.fromisoformat(data_breach)
    except ValueError:
        return {"errore": "data_breach non valida (formato YYYY-MM-DD o YYYY-MM-DDTHH:MM)"}

    ora = datetime.now()
    ore_trascorse = (ora - scoperta).total_seconds() / 3600.0
    ore_rimanenti_garante = SCADENZA_GARANTE_ORE - ore_trascorse

    if numero_interessati > 1000:
        livello_rischio = "alto"
    elif numero_interessati > 100:
        livello_rischio = "medio"
    else:
        livello_rischio = "basso"

    if tipo not in ("dati_personali", "dati_particolari", "dati_finanziari"):
        return {"errore": f"tipo non valido. Validi: dati_personali, dati_particolari, dati_finanziari"}

    azione = MATRICE_RISCHIO.get((tipo, livello_rischio), "valutazione_manuale")
    notifica_garante = azione in ("notifica_garante_obbligatoria", "notifica_garante_e_interessati")
    notifica_interessati = azione == "notifica_garante_e_interessati"

    scadenza_garante = scoperta + timedelta(hours=SCADENZA_GARANTE_ORE)
    stato_scadenza = "entro_termine" if ore_rimanenti_garante > 0 else "termine_superato"

    return {
        "data_breach": data_breach,
        "tipo_dati": tipo,
        "numero_interessati": numero_interessati,
        "livello_rischio": livello_rischio,
        "azione_richiesta": azione,
        "notifica_garante_obbligatoria": notifica_garante,
        "comunicazione_interessati_obbligatoria": notifica_interessati,
        "scadenza_notifica_garante": scadenza_garante.isoformat(),
        "ore_rimanenti_per_garante": round(ore_rimanenti_garante, 1),
        "stato_scadenza": stato_scadenza,
        "riferimento_normativo": "art. 33-34 GDPR",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verifica scadenze notifica data breach GDPR.")
    parser.add_argument("--data-breach", required=True, help="Data scoperta breach (YYYY-MM-DD).")
    parser.add_argument("--tipo", required=True, help="Tipo: dati_personali, dati_particolari, dati_finanziari.")
    parser.add_argument("--numero-interessati", type=int, default=0, help="Numero interessati coinvolti.")
    args = parser.parse_args()

    result = valuta(args.data_breach, args.tipo, args.numero_interessati)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

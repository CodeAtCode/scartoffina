#!/usr/bin/env python3
"""Genera Stato Patrimoniale, Conto Economico e Nota Integrativa skeleton.

Schema OIC 34 (Documento di bilancio secondo i principi contabili italiani).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Schema OIC 34 - Stato Patrimoniale (Civilistico)
STATO_PATRIMONIALE_SCHEMA = {
    "attivo": {
        "A_immobilizzazioni": {
            "I_immobilizzazioni_immateriali": ["costi_impianto_ampliamento", "costi_ricerca_sviluppo", "diritti_brevetto", "avviamento", "immobilizzazioni_in_corso"],
            "II_immobilizzazioni_materiali": ["terreni", "fabbricati", "impianti_macchinari", "attrezzature", "beni_in_leasing"],
            "III_immobilizzazioni_finanziarie": ["partecipazioni", "crediti", "titoli", "depositi"],
        },
        "B_attivo_circulante": {
            "I_rimanenze": ["materie_prime", "prodotti_in_corso", "prodotti_finiti"],
            "II_crediti": ["crediti_clienti", "crediti_commerciali", "crediti_diversi"],
            "III_attivita_finanziarie_non_immobilizzate": ["titoli_breve_termine", "depositi_bancari"],
            "IV_disponibilita_liquide": ["depositi_bancari", "assegni", "denaro_cassa"],
        },
        "C_ratei_e_risconti": ["ratei_attivi", "risconti_attivi"],
    },
    "passivo": {
        "A_patrimonio_netto": ["capitale_sociale", "riserve", "utile_esercizio", "perdita_esercizio"],
        "B_fondo_ammortamento": ["fondo_ammortamento_immobilizzazioni"],
        "C_fondi_rischi_e_oneri": ["fondo_trattamento_fine_rapporto", "fondo_imposte"],
        "D_trattamento_fine_rapporto_dipendenti": ["tfr_dipendenti"],
        "E_debiti": ["debiti_finanziari_breve", "debiti_fornitori", "debiti_commerciali", "debiti_diversi", "debiti_fiscali"],
        "F_ratei_e_risconti_passivi": ["ratei_passivi", "risconti_passivi"],
    },
}

# Schema OIC 34 - Conto Economico (Civilistico)
CONTO_ECONOMICO_SCHEMA = {
    "valore_produzione": {
        "A_ricavi_vendite_prestazioni": "ricavi_vendite",
        "B_variazioni_rimanenze": "variazione_rimanenze",
        "C_incrementi_immobilizzazioni_lavori_interni": "incrementi_interni",
        "D_altri_ricavi_proventi": "altri_ricavi",
    },
    "costi_produzione": {
        "E_acquisti_consumo": "acquisti_materie",
        "F_servizi": "servizi",
        "G_costi_personale": ["salari_stipendi", "oneri_sociali", "tfr", "trattamento_quiescenza"],
        "H_ammortamenti": "ammortamenti",
        "I_svalutazioni": "svalutazioni_crediti",
        "L_altri_accantonamenti": "accantonamenti_rischi",
        "M_altri_costi": "altri_costi",
        "N_acquisti_personale_interinale": "costi_personale_interinale",
    },
    "risultato_esercizio": "differenza_valore_costi",
}


def genera_bilancio(pdc: dict) -> dict:
    """Genera bilancio da piano dei conti aggregato."""
    stato_patrimoniale = json.loads(json.dumps(STATO_PATRIMONIALE_SCHEMA))
    conto_economico = json.loads(json.dumps(CONTO_ECONOMICO_SCHEMA))

    # Applica saldi dal piano dei conti (se forniti)
    for sezione, voci in pdc.items():
        if sezione == "stato_patrimoniale":
            _applica_saldi(stato_patrimoniale, voci)
        elif sezione == "conto_economico":
            _applica_saldi_ce(conto_economico, voci)

    # Calcola totali
    totale_attivo = _calcola_totale_attivo(stato_patrimoniale["attivo"])
    totale_passivo = _calcola_totale_passivo(stato_patrimoniale["passivo"])
    valore_produzione = _calcola_totale_ce(conto_economico["valore_produzione"])
    costi_produzione = _calcola_totale_ce(conto_economico["costi_produzione"])
    utile = valore_produzione - costi_produzione

    conto_economico["risultato_esercizio"] = round(utile, 2)
    conto_economico["valore_produzione_totale"] = round(valore_produzione, 2)
    conto_economico["costi_produzione_totale"] = round(costi_produzione, 2)

    return {
        "stato_patrimoniale": stato_patrimoniale,
        "totale_attivo": round(totale_attivo, 2),
        "totale_passivo": round(totale_passivo, 2),
        "conto_economico": conto_economico,
        "nota_integrativa_sezioni": [
            "1. Criteri di redazione e di valutazione",
            "2. Informazioni sulle immobilizzazioni",
            "3. Informazioni sulle partecipazioni",
            "4. Informazioni sugli immobili",
            "5. Informazioni sui crediti e debiti",
            "6. Informazioni sui titoli e depositi",
            "7. Informazioni sulle rimanenze",
            "8. Informazioni su patrimonio netto e riserve",
            "9. Informazioni su accantonamenti e fondi rischi",
            "10. Informazioni su debit/crediti finanziari",
            "11. Informazioni su ratei e riscontri",
            "12. Informazioni su fatti di gestione successivi",
            "13. Informazioni su rapporti con collegate",
            "14. Informazioni su operazioni con parti correlate",
            "15. Informazioni su eventi straordinari",
            "16. Informazioni su trattamento fiscale",
            "17. Altre informazioni",
        ],
    }


def _applica_saldi(schema: dict, valori: dict) -> None:
    for k, v in valori.items():
        if k in schema:
            if isinstance(schema[k], dict) and isinstance(v, dict):
                _applica_saldi(schema[k], v)
            elif isinstance(schema[k], list):
                if isinstance(v, dict):
                    for voce in schema[k]:
                        if voce in v:
                            schema[k][schema[k].index(voce)] = {voce: v[voce]}
                else:
                    schema[k] = [v]
            else:
                schema[k] = v


def _applica_saldi_ce(schema: dict, valori: dict) -> None:
    for k, v in valori.items():
        if k in schema:
            schema[k] = v


def _calcola_totale_attivo(attivo: dict) -> float:
    totale = 0.0
    for macro, voci in attivo.items():
        if isinstance(voci, dict):
            for categoria, contenuto in voci.items():
                if isinstance(contenuto, list):
                    for voce in contenuto:
                        if isinstance(voce, dict):
                            totale += sum(v for v in voce.values() if isinstance(v, (int, float)))
                elif isinstance(contenuto, dict):
                    totale += sum(v for v in contenuto.values() if isinstance(v, (int, float)))
                elif isinstance(contenuto, (int, float)):
                    totale += contenuto
    return totale


def _calcola_totale_passivo(passivo: dict) -> float:
    totale = 0.0
    for macro, voci in passivo.items():
        if isinstance(voci, list):
            for voce in voci:
                if isinstance(voce, dict):
                    totale += sum(v for v in voce.values() if isinstance(v, (int, float)))
                elif isinstance(voce, (int, float)):
                    totale += voce
        elif isinstance(voci, dict):
            totale += _calcola_totale_passivo(voci)
    return totale


def _calcola_totale_ce(sezione: dict) -> float:
    totale = 0.0
    for k, v in sezione.items():
        if isinstance(v, (int, float)):
            totale += v
        elif isinstance(v, list):
            totale += sum(x for x in v if isinstance(x, (int, float)))
        elif isinstance(v, dict):
            totale += _calcola_totale_ce(v)
    return totale


def main() -> int:
    p = argparse.ArgumentParser(description="Genera bilancio OIC 34")
    p.add_argument("--pdc", required=True, help="File JSON piano dei conti con saldi")
    p.add_argument("--output", default="bilancio.json", help="File output")
    args = p.parse_args()

    pdc = json.loads(Path(args.pdc).read_text(encoding="utf-8"))
    bilancio = genera_bilancio(pdc)
    Path(args.output).write_text(json.dumps(bilancio, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Bilancio generato: {args.output}")
    print(f"  Totale attivo: {bilancio['totale_attivo']} EUR")
    print(f"  Totale passivo: {bilancio['totale_passivo']} EUR")
    print(f"  Utile esercizio: {bilancio['conto_economico']['risultato_esercizio']} EUR")
    return 0


if __name__ == "__main__":
    sys.exit(main())

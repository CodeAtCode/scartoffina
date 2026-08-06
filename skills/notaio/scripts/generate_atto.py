#!/usr/bin/env python3
"""Genera schema atto notarile in markdown/JSON da parametri.

Output: bozza strutturata di atto (vendita, donazione, successione, societario).
Non sostituisce la formulazione del notaio — è uno schema di riferimento.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


SCHEMI_ATTI = {
    "vendita": [
        ("intestazione", "REPUBBLICA ITALIANA — ATTO DI VENDITA"),
        ("data_luogo", "Data: {data} — Luogo: {luogo}"),
        ("ante_fatto", "Premesso che: {antefatto}"),
        ("parte_venditore", "Venditore: {venditore_nome}, {venditore_dati}"),
        ("parte_acquirente", "Acquirente: {acquirente_nome}, {acquirente_dati}"),
        ("oggetto", "Oggetto: {oggetto_descrizione}"),
        ("prezzo", "Prezzo: {prezzo} EUR"),
        ("pagamento", "Pagamento: {modalita_pagamento}"),
        ("garanzie", "Garanzie: {garanzie}"),
        ("imposte", "Imposte: registro {registro}, ipotecaria {ipotecaria}, catastale {catastale}"),
        ("sottoscrizione", "Sottoscrizione: {sottoscrizione}"),
    ],
    "donazione": [
        ("intestazione", "REPUBBLICA ITALIANA — ATTO DI DONAZIONE"),
        ("data_luogo", "Data: {data} — Luogo: {luogo}"),
        ("donante", "Donante: {donante_nome}, {donante_dati}"),
        ("donatario", "Donatario: {donatario_nome}, {donatario_dati}"),
        ("oggetto", "Oggetto della donazione: {oggetto_descrizione}"),
        ("valore", "Valore dichiarato: {valore} EUR"),
        ("accettazione", "Accettazione donatario: {accettazione}"),
        ("imposte", "Imposte: {imposta_donazione} (art. 57 D.Lgs. 346/1990)"),
        ("sottoscrizione", "Sottoscrizione: {sottoscrizione}"),
    ],
    "successione": [
        ("intestazione", "REPUBBLICA ITALIANA — DICHIARAZIONE DI SUCCESSIONE"),
        ("de_cuius", "De cuius: {dc_nome}, deceduto il {dc_data} a {dc_luogo}"),
        ("eredi", "Eredi: {eredi_elenco}"),
        ("asse", "Asse ereditario: {asse} EUR"),
        ("passivita", "Passività: {passivita} EUR"),
        ("attivo_liquido", "Attivo liquido: {attivo_liquido} EUR"),
        ("imposta", "Imposta di successione: {imposta_successione} EUR"),
        ("sottoscrizione", "Sottoscrizione: {sottoscrizione}"),
    ],
}


def genera_atto(tipo: str, parametri: dict) -> dict:
    if tipo not in SCHEMI_ATTI:
        return {"errore": f"Tipo atto non supportato: {tipo}"}

    schema = SCHEMI_ATTI[tipo]
    sezioni = []
    for tag, template in schema:
        try:
            testo = template.format(**parametri)
        except KeyError:
            testo = template
        sezioni.append({"tag": tag, "testo": testo})

    return {
        "tipo_atto": tipo,
        "data_generazione": datetime.now().isoformat(),
        "sezioni": sezioni,
        "nota": "Schema di riferimento. Non sostituisce la formulazione del notaio rogante.",
    }


def to_markdown(atto: dict) -> str:
    lines = [f"# {atto['sezioni'][0]['testo']}", ""]
    for s in atto["sezioni"][1:]:
        lines.append(f"## {s['tag']}")
        lines.append(s["testo"])
        lines.append("")
    lines.append(f"> {atto['nota']}")
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Genera schema atto notarile")
    p.add_argument("--tipo", required=True, choices=["vendita", "donazione", "successione"])
    p.add_argument("--params", required=True, help="File JSON con parametri")
    p.add_argument("--format", choices=["json", "markdown"], default="markdown")
    p.add_argument("--output", help="File output")
    args = p.parse_args()

    parametri = json.loads(Path(args.params).read_text(encoding="utf-8"))
    atto = genera_atto(args.tipo, parametri)

    if args.format == "json":
        out = json.dumps(atto, indent=2, ensure_ascii=False)
    else:
        out = to_markdown(atto)

    if args.output:
        Path(args.output).write_text(out, encoding="utf-8")
        print(f"Atto generato: {args.output}")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())

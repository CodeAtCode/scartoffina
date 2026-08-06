#!/usr/bin/env python3
"""Genera convocazione assemblea condominiale.

Output: testo formattato pronto da inviare (raccomandata o PEC).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path


def genera_convocazione(data: dict) -> str:
    condominio = data.get("condominio", "Condominio [nome]")
    indirizzo = data.get("indirizzo", "[indirizzo]")
    data_prima = data.get("data_prima_convocazione", "")
    ora_prima = data.get("ora_prima_convocazione", "")
    data_seconda = data.get("data_seconda_convocazione", "")
    ora_seconda = data.get("ora_seconda_convocazione", "")
    luogo = data.get("luogo", "Sala riunioni del condominio")
    odg = data.get("ordine_del_giorno", [])

    lines = [
        f"CONVOCAZIONE ASSEMBLEA CONDOMINIALE",
        f"",
        f"Condominio: {condominio}",
        f"Sede: {indirizzo}",
        f"",
        f"Il sottoscritto amministratore del condominio in oggetto convoca",
        f"l'assemblea dei condomini nei seguenti giorni:",
        f"",
        f"PRIMA CONVOCAZIONE",
        f"  Data: {data_prima}",
        f"  Ora: {ora_prima}",
        f"  Luogo: {luogo}",
        f"",
        f"SECONDA CONVOCAZIONE",
        f"  Data: {data_seconda}",
        f"  Ora: {ora_seconda}",
        f"  Luogo: {luogo}",
        f"",
        f"ORDINE DEL GIORNO:",
    ]
    for i, arg in enumerate(odg, 1):
        lines.append(f"  {i}. {arg}")
    lines.extend([
        f"",
        f"I documenti relativi agli argomenti all'ordine del giorno sono disponibili",
        f"presso la sede del condominio e possono essere consultati dai condomini",
        f"nei giorni precedenti l'assemblea.",
        f"",
        f"Si ricorda che ogni condomino può farsi rappresentare mediante delega scritta.",
        f"Ciascun delegato può rappresentare massimo 3 condomini (art. 1136 c.c. c.9).",
        f"",
        f"L'amministratore",
        f"[firma]",
    ])
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Genera convocazione assemblea condominiale")
    p.add_argument("--input", required=True, help="File JSON con dati convocazione")
    p.add_argument("--output", help="File output (default: stdout)")
    args = p.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    testo = genera_convocazione(data)

    if args.output:
        Path(args.output).write_text(testo, encoding="utf-8")
        print(f"Convocazione generata: {args.output}")
    else:
        print(testo)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Genera verbale assemblea condominiale.

Output: testo formattato conforme art. 1130 c.c.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


def genera_verbale(data: dict) -> str:
    condominio = data.get("condominio", "Condominio [nome]")
    data_assemblea = data.get("data", "")
    luogo = data.get("luogo", "")
    convocazione = data.get("convocazione", "prima")
    presenti = data.get("presenti", [])
    millesimi_presenti = sum(p.get("millesimi", 0) for p in presenti)
    odg = data.get("ordine_del_giorno", [])
    deliberazioni = data.get("deliberazioni", [])

    lines = [
        f"VERBALE ASSEMBLEA CONDOMINIALE",
        f"",
        f"Condominio: {condominio}",
        f"Data: {data_assemblea}",
        f"Luogo: {luogo}",
        f"Convocazione: {convocazione}",
        f"",
        f"PRESIDENTE: {data.get('presidente', '[amministratore]')}",
        f"SEGRETARIO: {data.get('segretario', '[amministratore]')}",
        f"",
        f"PRESENTI:",
    ]
    for p in presenti:
        lines.append(f"  - {p.get('nome', '?')} — {p.get('millesimi', 0)} millesimi {p.get('delega', '')}")
    lines.append(f"")
    lines.append(f"Totale millesimi presenti: {millesimi_presenti}/1000")
    lines.append(f"")
    lines.append(f"ORDINE DEL GIORNO:")
    for i, arg in enumerate(odg, 1):
        lines.append(f"  {i}. {arg}")
    lines.append(f"")
    lines.append(f"DISCUSSIONE E DELIBERAZIONI:")
    lines.append(f"")
    for i, delib in enumerate(deliberazioni, 1):
        arg = delib.get("argomento", "")
        millesimi_favorevoli = delib.get("favorevoli", 0)
        millesimi_contrari = delib.get("contrari", 0)
        millesimi_astenuti = delib.get("astenuti", 0)
        esito = delib.get("esito", "APPROVATA" if millesimi_favorevoli > millesimi_contrari else "RESPINTA")
        tipo = delib.get("tipo_maggioranza", "ordinaria")
        lines.append(f"Argomento {i}: {arg}")
        lines.append(f"  Favorevoli: {millesimi_favorevoli} millesimi")
        lines.append(f"  Contrari: {millesimi_contrari} millesimi")
        lines.append(f"  Astenuti: {millesimi_astenuti} millesimi")
        lines.append(f"  Tipo maggioranza richiesta: {tipo}")
        lines.append(f"  Esito: {esito}")
        if delib.get("note"):
            lines.append(f"  Note: {delib['note']}")
        lines.append(f"")
    lines.extend([
        f"La presente verbale viene letto e approvato dai presenti.",
        f"",
        f"Il Presidente: [firma]",
        f"Il Segretario: [firma]",
        f"",
        f"Data: {data_assemblea}",
    ])
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Genera verbale assemblea condominiale")
    p.add_argument("--input", required=True, help="File JSON con dati verbale")
    p.add_argument("--output", help="File output (default: stdout)")
    args = p.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    testo = genera_verbale(data)

    if args.output:
        Path(args.output).write_text(testo, encoding="utf-8")
        print(f"Verbale generato: {args.output}")
    else:
        print(testo)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Genera registro IVA e libro giornale da un file JSON di operazioni.

Italy non ha il FEC francese; equivalente: registro IVA (DPR 633/1972 art. 23-24)
e libro giornale (art. 2214 c.c.).

Output: JSON o CSV.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


def carica_operazioni(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return data.get("operazioni", [])
    return data


def genera_registro_iva(operazioni: list[dict]) -> list[dict]:
    """Registro IVA vendite (art. 23) e acquisti (art. 24)."""
    registro = []
    for op in operazioni:
        imponibile = op.get("imponibile", 0.0)
        aliquota = op.get("aliquota", 0.22)
        imposta = imponibile * aliquota
        registro.append({
            "data": op.get("data"),
            "numero": op.get("numero"),
            "tipo": op.get("tipo", "vendita"),
            "cliente_fornitore": op.get("controparte"),
            "partita_iva": op.get("partita_iva_controparte"),
            "imponibile": round(imponibile, 2),
            "aliquota": aliquota,
            "imposta": round(imposta, 2),
            "totale": round(imponibile + imposta, 2),
            "registro": "vendite" if op.get("tipo", "vendita") == "vendita" else "acquisti",
        })
    return registro


def genera_libro_giornale(operazioni: list[dict]) -> list[dict]:
    """Libro giornale per art. 2214 c.c. (metodo partita doppia semplificato)."""
    movimenti = []
    for op in operazioni:
        imponibile = op.get("imponibile", 0.0)
        aliquota = op.get("aliquota", 0.22)
        imposta = imponibile * aliquota
        tipo = op.get("tipo", "vendita")
        conto_controparte = op.get("conto_controparte", "Clienti" if tipo == "vendita" else "Fornitori")

        # Scritture in partita doppia (semplificata)
        if tipo == "vendita":
            # Dare: Clienti / Avere: Ricavi + IVA debito
            movimenti.append({"data": op.get("data"), "conto_dare": conto_controparte, "descrizione": op.get("descrizione", ""), "dare": round(imponibile + imposta, 2), "avere": 0.0})
            movimenti.append({"data": op.get("data"), "conto_avere": "Ricavi vendite", "descrizione": op.get("descrizione", ""), "dare": 0.0, "avere": round(imponibile, 2)})
            movimenti.append({"data": op.get("data"), "conto_avere": "IVA debito", "descrizione": "IVA su vendite", "dare": 0.0, "avere": round(imposta, 2)})
        else:
            # Acquisto: Dare: Costi + IVA credito / Avere: Fornitori
            movimenti.append({"data": op.get("data"), "conto_dare": op.get("conto_costo", "Acquisti"), "descrizione": op.get("descrizione", ""), "dare": round(imponibile, 2), "avere": 0.0})
            movimenti.append({"data": op.get("data"), "conto_dare": "IVA credito", "descrizione": "IVA su acquisti", "dare": round(imposta, 2), "avere": 0.0})
            movimenti.append({"data": op.get("data"), "conto_avere": conto_controparte, "descrizione": op.get("descrizione", ""), "dare": 0.0, "avere": round(imponibile + imposta, 2)})
    return movimenti


def write_csv(rows: list[dict], path: Path) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    p = argparse.ArgumentParser(description="Genera registro IVA e libro giornale")
    p.add_argument("--input", required=True, help="File JSON con operazioni")
    p.add_argument("--format", choices=["csv", "json"], default="json")
    p.add_argument("--output", help="Prefisso file output (es. 'registri' -> registri.json)")
    p.add_argument("--tipo", choices=["registro_iva", "libro_giornale", "entrambi"], default="entrambi")
    args = p.parse_args()

    operazioni = carica_operazioni(Path(args.input))

    if args.tipo in ("registro_iva", "entrambi"):
        registro = genera_registro_iva(operazioni)
        if args.format == "csv":
            out = Path(f"{args.output or 'registro_iva'}.csv")
            write_csv(registro, out)
        else:
            out = Path(f"{args.output or 'registro_iva'}.json")
            out.write_text(json.dumps(registro, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Registro IVA: {out} ({len(registro)} righe)")

    if args.tipo in ("libro_giornale", "entrambi"):
        giornale = genera_libro_giornale(operazioni)
        if args.format == "csv":
            out = Path(f"{args.output or 'libro_giornale'}.csv")
            write_csv(giornale, out)
        else:
            out = Path(f"{args.output or 'libro_giornale'}.json")
            out.write_text(json.dumps(giornale, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Libro giornale: {out} ({len(giornale)} righe)")

    return 0


if __name__ == "__main__":
    sys.exit(main())

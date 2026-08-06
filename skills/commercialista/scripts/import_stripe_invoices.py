#!/usr/bin/env python3
"""Importa fatture da un export Stripe e genera file JSON FatturaPA-ready.

L'export Stripe (CSV) viene trasformato in un array di fatture JSON nel formato
atteso da generate_fatturapa.py e validate_fattura.py.

Idempotente: traccia un indice (stripe_invoice_id) per evitare duplicati.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


def estrai_da_csv(path_csv: Path) -> list[dict]:
    """Legge export Stripe CSV e restituisce lista di fatture JSON."""
    fatture: list[dict] = []
    with path_csv.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Mappatura campi Stripe -> formato fattura JSON
            amount = float(row.get("Amount (EUR)", row.get("amount", 0))) / 100.0
            tax = float(row.get("Tax (EUR)", row.get("tax", 0))) / 100.0
            imponibile = amount - tax
            aliquota = tax / imponibile if imponibile > 0 else 0.0

            fattura = {
                "stripe_invoice_id": row.get("ID", row.get("id", "")),
                "numero": row.get("Number", row.get("number", "")),
                "data": row.get("Created (UTC)", row.get("created", "")),
                "tipo_documento": "TD01",
                "cedente": {
                    "denominazione": "Stripe Italy S.r.l.",
                    "partita_iva": "12345678901",
                },
                "cessiomario": {
                    "denominazione": row.get("Customer Name", row.get("customer_name", "")),
                },
                "linee": [
                    {
                        "numero": 1,
                        "descrizione": row.get("Description", row.get("description", "Servizio")),
                        "quantita": 1,
                        "unita_misura": "pz",
                        "prezzo_unitario": round(imponibile, 2),
                        "prezzo_totale": round(imponibile, 2),
                        "aliquota_iva": round(aliquota, 4),
                    }
                ],
                "imponibile": round(imponibile, 2),
                "imposta": round(tax, 2),
                "totale": round(amount, 2),
            }
            fatture.append(fattura)
    return fatture


def filtra_duplicati(fatture: list[dict], indice_path: Path | None = None) -> list[dict]:
    """Filtra fatture già importate (idempotenza)."""
    if indice_path is None or not indice_path.exists():
        return fatture

    existing = json.loads(indice_path.read_text(encoding="utf-8"))
    seen_ids = {f.get("stripe_invoice_id") for f in existing}
    return [f for f in fatture if f.get("stripe_invoice_id") not in seen_ids]


def aggiorna_indice(fatture: list[dict], indice_path: Path) -> None:
    """Aggiorna file indice con le nuove fatture importate."""
    existing = []
    if indice_path.exists():
        existing = json.loads(indice_path.read_text(encoding="utf-8"))
    existing.extend(fatture)
    indice_path.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser(description="Importa fatture Stripe -> JSON FatturaPA-ready")
    p.add_argument("--input", required=True, help="File CSV export Stripe")
    p.add_argument("--output", required=True, help="File JSON output")
    p.add_argument("--indice", help="File JSON indice per idempotenza (default: .stripe-import-index.json)")
    args = p.parse_args()

    indice_path = Path(args.indice) if args.indice else Path(".stripe-import-index.json")

    fatture = estrai_da_csv(Path(args.input))
    nuove = filtra_duplicati(fatture, indice_path)

    Path(args.output).write_text(json.dumps(nuove, indent=2, ensure_ascii=False), encoding="utf-8")
    aggiorna_indice(nuove, indice_path)

    print(f"Importate {len(nuove)} nuove fatture (su {len(fatture)} totali) -> {args.output}")
    print(f"Indice idempotenza: {indice_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

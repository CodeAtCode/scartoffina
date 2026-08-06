#!/usr/bin/env python3
"""Validazione di una partita IVA italiana tramite algoritmo di checksum (Luhn)."""
from __future__ import annotations

import argparse
import json
import sys


def normalize(partita_iva: str) -> str:
    return "".join(ch for ch in partita_iva if ch.isdigit())


def luhn_check(digits: str) -> tuple[bool, int]:
    if len(digits) != 11:
        return False, -1
    total = 0
    for idx, ch in enumerate(digits):
        digit = int(ch)
        if (idx + 1) % 2 == 0:
            doubled = digit * 2
            total += doubled if doubled < 10 else doubled - 9
        else:
            total += digit
    controllo = (10 - (total % 10)) % 10
    codice_controllo_inserito = int(digits[-1])
    return controllo == codice_controllo_inserito, controllo


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validazione partita IVA italiana (algoritmo Luhn)."
    )
    parser.add_argument(
        "--partita-iva", required=True, help="Partita IVA da validare (11 cifre)."
    )
    args = parser.parse_args()

    digits = normalize(args.partita_iva)
    valid, controllo = luhn_check(digits)

    result = {
        "partita_iva": args.partita_iva,
        "valid": valid,
        "codice_controllo": controllo if controllo >= 0 else None,
        "lunghezza": len(digits),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

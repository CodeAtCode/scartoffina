#!/usr/bin/env python3
"""Verifica indipendenza del revisore (D.Lgs. 39/2010, Codice Deontologico).

Usage: verify_independence.py --input data/indipendenza.example.json
"""
import argparse
import json
import sys


def main() -> int:
    p = argparse.ArgumentParser(description="Verifica indipendenza revisore")
    p.add_argument("--input", required=True)
    args = p.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        dati = json.load(f)

    minacce = dati.get("minacce", [])
    salvaguardie = dati.get("salvagardie", [])

    minacce_non_mitigate = []
    for m in minacce:
        if not m.get("mitigata", False):
            minacce_non_mitigate.append(m)

    indipendente = len(minacce_non_mitigate) == 0

    result = {
        "revisore": dati.get("revisore", {}),
        "cliente": dati.get("cliente", {}),
        "numero_minacce": len(minacce),
        "numero_salvaguardie": len(salvaguardie),
        "minacce_non_mitigate": len(minacce_non_mitigate),
        "indipendente": indipendente,
        "esito": "idoneo" if indipendente else "non idoneo - minacce non mitigate",
        "riferimento": "D.Lgs. 39/2010 art. 5; Codice Deontologico CNDC",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Calcolo ampiezza campionaria per test di controllo e sostanziali (ISA 530).

Usage: calc_sample_size.py --popolazione 5000 --tolleranza 0.05 --rischio-controllo 0.60 --errore-atteso 0.02
"""
import argparse
import json
import math
import sys


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo ampiezza campionaria")
    p.add_argument("--popolazione", type=int, required=True)
    p.add_argument("--tolleranza", type=float, required=True, help="Tasso di deviazione tollerato (0-1)")
    p.add_argument("--rischio-controllo", type=float, required=True, help="Rischio di valutazione troppo basso (0-1)")
    p.add_argument("--errore-atteso", type=float, default=0.0, help="Tasso di errore atteso (0-1)")
    args = p.parse_args()

    fattore_assicurazione = 2.0
    n = (fattore_assicurazione / args.tolleranza) * (1 + args.errore_atteso)
    n_finale = int(math.ceil(n))

    if args.popolazione < 5000:
        n_finale = max(n_finale, 25)
    else:
        n_finale = min(n_finale, args.popolazione)

    result = {
        "popolazione": args.popolazione,
        "tolleranza": args.tolleranza,
        "rischio_controllo": args.rischio_controllo,
        "errore_atteso": args.errore_atteso,
        "ampiezza_campione": n_finale,
        "metodo": "attributo sampling (ISA 530)",
        "tipo_test": "test di controllo",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

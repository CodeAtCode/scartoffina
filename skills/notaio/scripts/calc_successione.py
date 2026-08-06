#!/usr/bin/env python3
"""Calcolo completo dell'imposta di successione con ripartizione tra eredi.

D.Lgs. 346/1990 artt. 16-17 (franchigie e aliquote per grado di parentela).
Ripartizione per quote ereditarie ex art. 566 c.c.
"""
from __future__ import annotations

import argparse
import json
import sys


def calc_successione(asse: float, eredi: list[dict]) -> dict:
    """Calcola imposta di successione ripartita tra eredi.

    Args:
        asse: valore complessivo asse ereditario
        eredi: lista dict {nome, grado_parentela, quota (0-1)}

    Returns:
        dict con totale imposta, ripartizione per erede
    """
    FRANCHIGIA = {
        "coniuge_figli": 1_000_000.0,
        "fratelli_sorelle": 100_000.0,
        "altri_parenti_4_grado": 100_000.0,
        "altri": 0.0,
    }
    ALIQUOTA = {
        "coniuge_figli": 0.04,
        "fratelli_sorelle": 0.06,
        "altri_parenti_4_grado": 0.06,
        "altri": 0.08,
    }

    riparto = []
    totale_imposta = 0.0
    for erede in eredi:
        nome = erede.get("nome", "Erede")
        grado = erede.get("grado_parentela", "altri")
        quota_pct = erede.get("quota", 1.0 / len(eredi))

        quota_asse = asse * quota_pct
        franchigia_ereditaria = FRANCHIGIA.get(grado, 0.0) * quota_pct
        imponibile = max(0.0, quota_asse - franchigia_ereditaria)
        aliquota = ALIQUOTA.get(grado, 0.08)
        imposta = imponibile * aliquota

        riparto.append({
            "nome": nome,
            "grado_parentela": grado,
            "quota_percentuale": round(quota_pct, 4),
            "quota_asse": round(quota_asse, 2),
            "franchigia_ereditaria": round(franchigia_ereditaria, 2),
            "imponibile": round(imponibile, 2),
            "aliquota": aliquota,
            "imposta": round(imposta, 2),
        })
        totale_imposta += imposta

    return {
        "asse_ereditario": asse,
        "numero_eredi": len(eredi),
        "totale_imposta": round(totale_imposta, 2),
        "riparto": riparto,
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Calcolo imposta di successione con ripartizione eredi")
    p.add_argument("--asse", type=float, required=True, help="Valore complessivo asse ereditario")
    p.add_argument("--eredi", required=True, help="JSON: lista eredi [{nome, grado_parentela, quota}]")
    args = p.parse_args()

    eredi = json.loads(args.eredi)
    result = calc_successione(args.asse, eredi)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

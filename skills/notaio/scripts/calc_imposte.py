#!/usr/bin/env python3
"""Calcoli deterministici per la skill notaio.

Comandi:
  registro    Imposta di registro (proporzionale / fissa)
  ipotecaria  Imposta ipotecaria
  catastale   Imposta catastale
  bollo       Imposta di bollo
  successione Imposta di successione
  donazione   Imposta di donazione
"""
from __future__ import annotations

import argparse
import json
import sys

# Aliquote imposta di registro (DPR 131/1986 art. 11)
REGISTRO_PROPORZIONALE = {
    "vendita_abitazioni_agevolate": 0.02,   # prima casa (DPR 601/1970 art. 7)
    "vendita_abitazioni_non_agevolate": 0.09,
    "vendita_c terreni_agricoli": 0.15,
    "vendita_terreni_edificabili": 0.09,
    "vendita_campagna_comunale": 0.11,
    "successione_donazione": 0.00,  # esclusa
    "affitto": 0.01,                  # canone annuo (DPR 131/1986 tabella)
    "locazione_finanziaria": 0.00,   # leasing
    "altri_atti": 0.03,               # transfer
    "societa_costituzione": 0.00,    # €200 fissa (art. 9 c.1 lett. c)
    "societa_aumento_capitale": 0.00, # €200 fissa
}

# Imposta ipotecaria (DPR 601/1970 art. 11)
IPOTECARIA = {
    "fissa": 50.0,         # atti non soggetti a proporzionale
    "proporzionale": 0.01,  # 1%
}

# Imposta catastale (DPR 601/1970 art. 10)
CATASTALE = {
    "fissa": 50.0,         # atti non soggetti a proporzionale
    "proporzionale": 0.01,  # 1%
}

# Imposta di bollo (DPR 642/1972)
BOLLO = {
    "atto": 16.0,          # marca da bollo
    "copia": 16.0,         # copia conforme
    "verbale_assemblea": 16.0,
    "registro": 155.00,    # iscrizione atto (L. 13/1980)
}

# Imposta di successione (D.Lgs. 346/1990 art. 16-17)
# Scagloni franchigia per successione (2025)
SUCCESSIONE_FRANCHIGIA = {
    "coniuge_figli": 1_000_000.0,   # €1.000.000 per figli
    "fratelli_sorelle": 100_000.0,
    "altri_parenti_4_grado": 100_000.0,
    "altri": 0.0,
}

# Aliquote successione
SUCCESSIONE_ALIQUOTE = {
    "coniuge_figli": 0.04,   # 4% eccedente franchigia
    "fratelli_sorelle": 0.06,
    "altri_parenti_4_grado": 0.06,
    "altri": 0.08,
}


def calc_registro(valore: float, tipo: str = "altri_atti", agevolata: bool = False) -> dict:
    """Imposta di registro proporzionale o fissa."""
    aliquota = REGISTRO_PROPORZIONALE.get(tipo, 0.03)
    if agevolata and "vendita_abitazioni" in tipo:
        aliquota = REGISTRO_PROPORZIONALE["vendita_abitazioni_agevolate"]
    if tipo.startswith("societa_"):
        return {
            "valore": valore,
            "tipo": tipo,
            "imposta": 200.0,  # fissa €200
            "tipo_calcolo": "fissa (art. 9 c.1 lett. c DPR 131/1986)",
        }
    imposta = valore * aliquota
    return {
        "valore": valore,
        "tipo": tipo,
        "aliquota": aliquota,
        "imposta": round(imposta, 2),
        "tipo_calcolo": "proporzionale",
    }


def calc_ipotecaria(valore: float, proporzionale: bool = False) -> dict:
    if proporzionale:
        imposta = valore * IPOTECARIA["proporzionale"]
        return {"valore": valore, "aliquota": IPOTECARIA["proporzionale"], "imposta": round(imposta, 2), "tipo": "proporzionale"}
    return {"valore": valore, "imposta": IPOTECARIA["fissa"], "tipo": "fissa"}


def calc_catastale(valore: float, proporzionale: bool = False) -> dict:
    if proporzionale:
        imposta = valore * CATASTALE["proporzionale"]
        return {"valore": valore, "aliquota": CATASTALE["proporzionale"], "imposta": round(imposta, 2), "tipo": "proporzionale"}
    return {"valore": valore, "imposta": CATASTALE["fissa"], "tipo": "fissa"}


def calc_successione(asse_ereditario: float, grado: str = "coniuge_figli") -> dict:
    """Imposta di successione con franchigia (D.Lgs. 346/1990)."""
    franchigia = SUCCESSIONE_FRANCHIGIA.get(grado, 0.0)
    aliquota = SUCCESSIONE_ALIQUOTE.get(grado, 0.08)
    imponibile = max(0.0, asse_ereditario - franchigia)
    imposta = imponibile * aliquota
    return {
        "asse_ereditario": asse_ereditario,
        "grado_parentela": grado,
        "franchigia": franchigia,
        "imponibile": round(imponibile, 2),
        "aliquota": aliquota,
        "imposta": round(imposta, 2),
    }


def calc_donazione(valore: float, grado: str = "coniuge_figli") -> dict:
    """Imposta di donazione (stessa franchigia/aliquote della successione ex art. 57 D.Lgs. 346/1990)."""
    return calc_successione(valore, grado)


def main() -> int:
    parser = argparse.ArgumentParser(description="Calcoli deterministici skill notaio")
    sub = parser.add_subparsers(dest="comando", required=True)

    p_reg = sub.add_parser("registro", help="Imposta di registro")
    p_reg.add_argument("--valore", type=float, required=True)
    p_reg.add_argument("--tipo", default="altri_atti")
    p_reg.add_argument("--agevolata", action="store_true")

    p_ip = sub.add_parser("ipotecaria", help="Imposta ipotecaria")
    p_ip.add_argument("--valore", type=float, required=True)
    p_ip.add_argument("--proporzionale", action="store_true")

    p_cat = sub.add_parser("catastale", help="Imposta catastale")
    p_cat.add_argument("--valore", type=float, required=True)
    p_cat.add_argument("--proporzionale", action="store_true")

    p_bol = sub.add_parser("bollo", help="Imposta di bollo")
    p_bol.add_argument("--tipo", default="atto")

    p_suc = sub.add_parser("successione", help="Imposta di successione")
    p_suc.add_argument("--asse", type=float, required=True)
    p_suc.add_argument("--grado", default="coniuge_figli",
                        choices=["coniuge_figli", "fratelli_sorelle", "altri_parenti_4_grado", "altri"])

    p_don = sub.add_parser("donazione", help="Imposta di donazione")
    p_don.add_argument("--valore", type=float, required=True)
    p_don.add_argument("--grado", default="coniuge_figli",
                        choices=["coniuge_figli", "fratelli_sorelle", "altri_parenti_4_grado", "altri"])

    args = parser.parse_args()

    if args.comando == "registro":
        out = calc_registro(args.valore, args.tipo, args.agevolata)
    elif args.comando == "ipotecaria":
        out = calc_ipotecaria(args.valore, args.proporzionale)
    elif args.comando == "catastale":
        out = calc_catastale(args.valore, args.proporzionale)
    elif args.comando == "bollo":
        out = {"tipo": args.tipo, "imposta": BOLLO.get(args.tipo, 16.0)}
    elif args.comando == "successione":
        out = calc_successione(args.asse, args.grado)
    elif args.comando == "donazione":
        out = calc_donazione(args.valore, args.grado)
    else:
        parser.print_help()
        return 1

    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

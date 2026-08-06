#!/usr/bin/env python3
"""Calcoli deterministici per la skill commercialista.

Comandi:
  iva        Calcolo IVA (imponibile, imposta, reverse charge, split payment)
  ires       Calcolo IRES (24%)
  irap       Calcolo IRAP (3,9% base + addizionale regionale)
  ammortamento  Calcolo ammortamento civilistico/fiscale
  ratei_risconti  Calcolo ratei e risconti
  cca        Calcolo canone di locazione finanziaria (leasing)
  pro_rata   Calcolo pro-rata IVA
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass

# Aliquote IVA 2025 (DPR 633/1972 tabella allegata)
IVA_ALIQUOTE = {
    "ordinaria": 0.22,
    "ridotta": 0.10,
    "minima": 0.04,
    "esente": 0.0,
}

# IRES 24% (D.Lgs. 344/2003 art. 73)
IRES_ALIQUOTA = 0.24

# IRAP 3,9% base (D.Lgs. 446/1997 art. 6) + addizionale comunale
IRAP_BASE = 0.039

# Coefficienti ammortamento tipici (DM 31/12/1988 - Tabella categoria)
COEFF_AMMORTAMENTO = {
    "beni_strumentali_generici": 0.15,
    "macchinari": 0.12,
    "impianti": 0.10,
    "attrezzature": 0.12,
    "automezzi": 0.20,
    "mobili_arredamento": 0.10,
    "impianti_informatici": 0.20,
    "software": 0.20,
    "immobili_strumentali": 0.03,
    "beni_usati": 0.10,
}


@dataclass
class EsitoIVA:
    imponibile: float
    aliquota: float
    imposta: float
    totale: float
    tipo: str


def calc_iva(imponibile: float, aliquota: float = 0.22, tipo: str = "ordinaria") -> dict:
    imposta = imponibile * aliquota
    esito = EsitoIVA(
        imponibile=imponibile,
        aliquota=aliquota,
        imposta=round(imposta, 2),
        totale=round(imponibile + imposta, 2),
        tipo=tipo,
    )
    d = asdict(esito)
    if tipo == "reverse_charge":
        d["reverse_charge"] = (
            "Reverse charge: l'IVA non è liquidadal cedente, ma assolta dal cessionario. "
            "Operazione non imponibile ex art. 17 c.2 DPR 633/1972."
        )
        d["imposta"] = 0.0
        d["totale"] = imponibile
    elif tipo == "split_payment":
        d["split_payment"] = (
            "Split payment: l'IVA è versata dal cessionario (PA o autonome). "
            "Imponibile al cedente, imposta al cessionario (art. 17-ter DPR 633/1972)."
        )
        d["totale"] = imponibile
    return d


def calc_ires(imponibile: float, aliquota: float = IRES_ALIQUOTA) -> dict:
    imposta = max(0.0, imponibile) * aliquota
    return {
        "imponibile": imponibile,
        "aliquota": aliquota,
        "imposta": round(imposta, 2),
        "deduzione_esenzione": 0.0,
    }


def calc_irap(valore_produzione: float, aliquota: float = IRAP_BASE) -> dict:
    imposta = max(0.0, valore_produzione) * aliquota
    return {
        "valore_produzione": valore_produzione,
        "aliquota": aliquota,
        "imposta": round(imposta, 2),
        "componente_negativa": 0.0,
    }


@dataclass
class EsitoAmmortamento:
    costo_storico: float
    coefficiente: float
    quota_annua: float
    fondo_ammortamento: float
    residuo: float
    tipo: str


def calc_ammortamento(costo: float, coeff: float, anno: int = 1, tipo: str = "civilistico") -> dict:
    """Calcolo quota ammortamento.

    Primo anno: only 50% quota se bene durata > 1 anno (TUIR art. 102 c.7).
    """
    quota_full = costo * coeff
    if anno == 1:
        quota = quota_full / 2  # mezza quota primo anno (TUIR art. 102 c.7)
        nota = "Primo anno: mezza quota ex art. 102 c.7 TUIR"
    else:
        quota = quota_full
        nota = "Quota intera"
    fondo = quota * min(anno, int(1 / coeff))
    residuo = costo - fondo
    esito = EsitoAmmortamento(
        costo_storico=costo,
        coefficiente=coeff,
        quota_annua=round(quota, 2),
        fondo_ammortamento=round(fondo, 2),
        residuo=round(residuo, 2),
        tipo=tipo,
    )
    d = asdict(esito)
    d["nota"] = nota
    return d


def calc_ratei_risconti(importo: float, giorni: int, tipo: str = "rateo") -> dict:
    """Calcolo ratei (competenza futura) o risconti (competenza già registrata)."""
    quota_giornaliera = importo / 365
    importo_rilevato = quota_giornaliera * giorni
    return {
        "importo_totale": importo,
        "giorni": giorni,
        "importo_rilevato": round(importo_rilevato, 2),
        "tipo": tipo,
        "scritture": (
            "Rateo (competenza futura): storno costo, iscrizione debito. "
            "Riscontro (competenza già registrata): iscrizione credito, quota costo."
        ) if tipo == "rateo" else
        (
            "Riscontro (competenza già registrata): quota costo, storno credito. "
            "Rateo (competenza futura): iscrizione debito, storno costo."
        ),
    }


def calc_pro_rata_iva(operazioni_imponibili: float, operazioni_totali: float) -> dict:
    """Pro-rata IVA (art. 19 c.5 DPR 633/1972)."""
    if operazioni_totali <= 0:
        return {"errore": "Operazioni totali deve essere > 0"}
    pro_rata = operazioni_imponibili / operazioni_totali
    return {
        "operazioni_imponibili": operazioni_imponibili,
        "operazioni_totali": operazioni_totali,
        "pro_rata": round(pro_rata, 4),
        "percentuale_detrazione": round(pro_rata * 100, 2),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Calcoli deterministici skill commercialista")
    sub = parser.add_subparsers(dest="comando", required=True)

    p_iva = sub.add_parser("iva", help="Calcolo IVA")
    p_iva.add_argument("--imponibile", type=float, required=True)
    p_iva.add_argument("--aliquota", type=float, default=0.22)
    p_iva.add_argument("--tipo", choices=["ordinaria", "reverse_charge", "split_payment"], default="ordinaria")

    p_ires = sub.add_parser("ires", help="Calcolo IRES (24%%)")
    p_ires.add_argument("--imponibile", type=float, required=True)

    p_irap = sub.add_parser("irap", help="Calcolo IRAP")
    p_irap.add_argument("--valore-produzione", type=float, required=True)
    p_irap.add_argument("--aliquota", type=float, default=IRAP_BASE)

    p_amm = sub.add_parser("ammortamento", help="Calcolo ammortamento")
    p_amm.add_argument("--costo", type=float, required=True)
    p_amm.add_argument("--coeff", type=float, required=True)
    p_amm.add_argument("--anno", type=int, default=1)
    p_amm.add_argument("--tipo", choices=["civilistico", "fiscale"], default="civilistico")

    p_rr = sub.add_parser("ratei_risconti", help="Calcolo ratei/riscontri")
    p_rr.add_argument("--importo", type=float, required=True)
    p_rr.add_argument("--giorni", type=int, required=True)
    p_rr.add_argument("--tipo", choices=["rateo", "riscontro"], default="rateo")

    p_pr = sub.add_parser("pro_rata", help="Pro-rata IVA")
    p_pr.add_argument("--imponibili", type=float, required=True)
    p_pr.add_argument("--totali", type=float, required=True)

    args = parser.parse_args()

    if args.comando == "iva":
        out = calc_iva(args.imponibile, args.aliquota, args.tipo)
    elif args.comando == "ires":
        out = calc_ires(args.imponibile)
    elif args.comando == "irap":
        out = calc_irap(args.valore_produzione, args.aliquota)
    elif args.comando == "ammortamento":
        out = calc_ammortamento(args.costo, args.coeff, args.anno, args.tipo)
    elif args.comando == "ratei_risconti":
        out = calc_ratei_risconti(args.importo, args.giorni, args.tipo)
    elif args.comando == "pro_rata":
        out = calc_pro_rata_iva(args.imponibili, args.totali)
    else:
        parser.print_help()
        return 1

    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

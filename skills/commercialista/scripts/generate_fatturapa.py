#!/usr/bin/env python3
"""Genera FatturaPA XML (formato FPR12) da una fattura JSON.

FPR12 = fattura tra privati (Fatturazione Elettronica tra privati).
Specifica: SDICoop - regole tecniche vigenti.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring

NAMESPACES = {
    "p": "http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2",
}


def _text(parent: Element, tag: str, text: str | None) -> Element:
    el = SubElement(parent, tag)
    if text is not None:
        el.text = text
    return el


def genera_fattura_xml(fattura: dict, cedente: dict, cessiomario: dict) -> str:
    """Genera XML FPR12 da dict."""
    root = Element("p:FatturaElettronica")
    root.set("versione", "FPR12")
    root.set("xmlns:ds", "http://www.w3.org/2000/09/xmldsig#")
    root.set("xmlns:p", NAMESPACES["p"])
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")

    # FatturaElettronicaHeader
    header = SubElement(root, "FatturaElettronicaHeader")

    # DatiTrasmissione
    trasmissione = SubElement(header, "DatiTrasmissione")
    _text(trasmissione, "IdTrasmittente", cedente.get("id_trasmittente"))
    _text(trasmissione, "ProgressivoInvio", fattura.get("progressivo", "1"))
    _text(trasmissione, "FormatoTrasmissione", "FPR12")
    _text(trasmissione, "CodiceDestinatario", cessiomario.get("codice_destinatario", "0000000"))

    # CedentePrestatore
    cedente_el = SubElement(header, "CedentePrestatore")
    dati_anag = SubElement(cedente_el, "DatiAnagrafici")
    _text(dati_anag, "IdFiscaleIVA", cedente.get("partita_iva"))
    _text(dati_anag, "Anagrafica", cedente.get("denominazione"))
    _text(dati_anag, "RegimeFiscale", cedente.get("regime_fiscale", "RF01"))

    # CessionarioCommittente
    cessiomario_el = SubElement(header, "CessionarioCommittente")
    dati_anag_c = SubElement(cessiomario_el, "DatiAnagrafici")
    _text(dati_anag_c, "IdFiscaleIVA", cessiomario.get("partita_iva"))
    _text(dati_anag_c, "Anagrafica", cessiomario.get("denominazione"))

    # FatturaElettronicaBody
    body = SubElement(root, "FatturaElettronicaBody")
    dati_gen = SubElement(body, "DatiGenerali")
    dati_doc = SubElement(dati_gen, "DatiDocumento")
    _text(dati_doc, "TipoDocumento", fattura.get("tipo_documento", "TD01"))
    _text(dati_doc, "Divisa", "EUR")
    _text(dati_doc, "Data", fattura.get("data", datetime.now().strftime("%Y-%m-%d")))
    _text(dati_doc, "Numero", fattura.get("numero", "1"))

    # DatiBeniServizi
    dati_bs = SubElement(body, "DatiBeniServizi")
    for riga in fattura.get("linee", []):
        dettaglio = SubElement(dati_bs, "DettaglioLinee")
        _text(dettaglio, "NumeroLinea", str(riga.get("numero", 1)))
        _text(dettaglio, "Descrizione", riga.get("descrizione", ""))
        _text(dettaglio, "Quantita", str(riga.get("quantita", 1)))
        _text(dettaglio, "UnitaMisura", riga.get("unita_misura", "pz"))
        _text(dettaglio, "PrezzoUnitario", f"{riga.get('prezzo_unitario', 0):.2f}")
        _text(dettaglio, "PrezzoTotale", f"{riga.get('prezzo_totale', 0):.2f}")
        _text(dettaglio, "AliquotaIVA", f"{riga.get('aliquota_iva', 0.22) * 100:.2f}")

    # DatiRiepilogo
    riepilogo = SubElement(dati_bs, "DatiRiepilogo")
    imponibile = sum(r.get("prezzo_totale", 0) for r in fattura.get("linee", []))
    aliquota = fattura.get("linee", [{}])[0].get("aliquota_iva", 0.22) if fattura.get("linee") else 0.22
    imposta = imponibile * aliquota
    _text(riepilogo, "AliquotaIVA", f"{aliquota * 100:.2f}")
    _text(riepilogo, "ImponibileImporto", f"{imponibile:.2f}")
    _text(riepilogo, "Imposta", f"{imposta:.2f}")
    _text(riepilogo, "ImportoTotaleDocumento", f"{imponibile + imposta:.2f}")

    xml_str = tostring(root, encoding="unicode", xml_declaration=True)
    return xml_str


def main() -> int:
    p = argparse.ArgumentParser(description="Genera FatturaPA XML FPR12")
    p.add_argument("--invoice", required=True, help="File JSON fattura")
    p.add_argument("--output", default="fattura.xml", help="File XML output")
    args = p.parse_args()

    data = json.loads(Path(args.invoice).read_text(encoding="utf-8"))
    fattura = data.get("fattura", data)
    cedente = data.get("cedente", {})
    cessiomario = data.get("cessiomario", {})

    xml = genera_fattura_xml(fattura, cedente, cessiomario)
    Path(args.output).write_text(xml, encoding="utf-8")
    print(f"FatturaPA generata: {args.output}")
    print(f"  Imponibile: {sum(r.get('prezzo_totale', 0) for r in fattura.get('linee', [])):.2f} EUR")
    return 0


if __name__ == "__main__":
    sys.exit(main())

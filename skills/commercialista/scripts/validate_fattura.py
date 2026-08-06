#!/usr/bin/env python3
"""Valida i campi obbligatori di una fattura JSON secondo DPR 633/1972 art. 21.

Controlli: integrita strutturale + campi obbligatori + coerenza importi.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Campi obbligatori per DPR 633/1972 art. 21
CAMPI_OBBLIGATORI_TESTATA = [
    "numero",
    "data",
    "tipo_documento",
]

CAMPI_OBBLIGATORI_CEDENTE = [
    "denominazione",
    "partita_iva",
]

CAMPI_OBBLIGATORI_CESSIOMARIO = [
    "denominazione",
]

CAMPI_OBBLIGATORI_RIGA = [
    "numero",
    "descrizione",
    "quantita",
    "prezzo_unitario",
    "prezzo_totale",
    "aliquota_iva",
]

TIPI_DOCUMENTO_VALIDI = {
    "TD01": "fattura",
    "TD02": "acconto/anticipo su fattura",
    "TD03": "acconto/anticipo su parcella",
    "TD04": "nota di credito",
    "TD05": "nota di debito",
    "TD06": "parcella",
    "TD16": "integrazione fattura reverse charge",
    "TD17": "integrazione/autofattura acquisto servizi estero",
    "TD18": "integrazione/autofattura acquisto beni intracomunitari",
    "TD19": "integrazione/autofattura acquisto beni ex art.17 c.2 DPR 633",
    "TD20": "autofattura contribuenti forfettari",
    "TD21": "autofattura altri casi",
    "TD22": "estratto",
    "TD23": "estratto wellsite",
    "TD24": "fattura differita",
    "TD25": "fattura differita esportazioni",
    "TD26": "cessione beni ammortizzabili",
    "TD27": "fattura per autoconsumo",
}


def valida_fattura(fattura: dict) -> dict:
    """Valida fattura restituendo report pass/fail per campo."""
    report = {
        "valido": True,
        "errori": [],
        "warning": [],
        "controlli": [],
    }

    # 1. Testata
    for campo in CAMPI_OBBLIGATORI_TESTATA:
        if campo not in fattura or not fattura[campo]:
            report["errori"].append(f"Testata: campo obbligatorio mancante '{campo}'")
            report["valido"] = False
        else:
            report["controlli"].append(f"OK: testata.{campo}")

    # 2. Tipo documento
    tipo = fattura.get("tipo_documento", "TD01")
    if tipo not in TIPI_DOCUMENTO_VALIDI:
        report["errori"].append(f"Testata: tipo_documento '{tipo}' non valido")
        report["valido"] = False
    else:
        report["controlli"].append(f"OK: tipo_documento {tipo} ({TIPI_DOCUMENTO_VALIDI[tipo]})")

    # 3. Cedente
    cedente = fattura.get("cedente", {})
    for campo in CAMPI_OBBLIGATORI_CEDENTE:
        if campo not in cedente or not cedente[campo]:
            report["errori"].append(f"Cedente: campo obbligatorio mancante '{campo}'")
            report["valido"] = False
        else:
            report["controlli"].append(f"OK: cedente.{campo}")

    # 4. Partita IVA cedente (11 cifre)
    pi = cedente.get("partita_iva", "")
    if pi and (not pi.isdigit() or len(pi) != 11):
        report["warning"].append(f"Cedente: partita_iva '{pi}' non è di 11 cifre")

    # 5. Cessionario
    cessiomario = fattura.get("cessiomario", {})
    for campo in CAMPI_OBBLIGATORI_CESSIOMARIO:
        if campo not in cessiomario or not cessiomario[campo]:
            report["errori"].append(f"Cessionario: campo obbligatorio mancante '{campo}'")
            report["valido"] = False
        else:
            report["controlli"].append(f"OK: cessiomario.{campo}")

    # 6. Righe
    linee = fattura.get("linee", [])
    if not linee:
        report["errori"].append("Linee: nessuna riga dettaglio presente")
        report["valido"] = False

    for i, riga in enumerate(linee):
        for campo in CAMPI_OBBLIGATORI_RIGA:
            if campo not in riga or riga[campo] is None:
                report["errori"].append(f"Riga {i+1}: campo obbligatorio mancante '{campo}'")
                report["valido"] = False
            else:
                report["controlli"].append(f"OK: riga {i+1}.{campo}")

        # Coerenza prezzo totale
        if "quantita" in riga and "prezzo_unitario" in riga and "prezzo_totale" in riga:
            expected = round(riga["quantita"] * riga["prezzo_unitario"], 2)
            actual = round(riga["prezzo_totale"], 2)
            if abs(expected - actual) > 0.01:
                report["errori"].append(
                    f"Riga {i+1}: prezzo_totale {actual} non coerente con quantita * prezzo_unitario ({expected})"
                )
                report["valido"] = False

        # Aliquota IVA valida
        alq = riga.get("aliquota_iva")
        if alq is not None:
            alq_pct = round(alq * 100, 2)
            if alq_pct not in (0, 4, 5, 10, 22):
                report["warning"].append(f"Riga {i+1}: aliquota_iva {alq_pct}% non standard")

    # 7. Coerenza totali
    imponibile_calc = sum(r.get("prezzo_totale", 0) for r in linee)
    if "imponibile" in fattura:
        if abs(fattura["imponibile"] - imponibile_calc) > 0.01:
            report["errori"].append(
                f"Testata: imponibile {fattura['imponibile']} non coerente con somma righe ({imponibile_calc:.2f})"
            )
            report["valido"] = False

    return report


def main() -> int:
    p = argparse.ArgumentParser(description="Valida fattura JSON (DPR 633/1972 art. 21)")
    p.add_argument("--invoice", required=True, help="File JSON fattura")
    args = p.parse_args()

    fattura = json.loads(Path(args.invoice).read_text(encoding="utf-8"))
    report = valida_fattura(fattura)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["valido"] else 1


if __name__ == "__main__":
    sys.exit(main())

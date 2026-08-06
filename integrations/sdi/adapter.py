"""Adapter per il Sistema di Interscambio (SDI) italiano.

Questo modulo fornisce un'interfaccia unificata per l'invio e la ricezione
di fatture elettroniche tramite il Sistema di Interscambio dell'Agenzia delle Entrate.

Formato supportato: FPR12 (fatturazione elettronica tra privati)
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal
from uuid import uuid4
import xml.etree.ElementTree as ET
from datetime import datetime


@dataclass
class FatturaElettronica:
    """Rappresenta una fattura elettronica FPR12.
    
    Attributes:
        numero: Numero progressivo della fattura
        data: Data di emissione (formato YYYY-MM-DD)
        emittente: Dati del cedente/prestatore
        destinatario: Dati del cessionario/committente
        importo_totale: Importo totale della fattura (imponibile + IVA)
        aliquote_iva: Lista di aliquote IVA applicate
        causale: Descrizione della causale di emissione
        regime_fiscale: Codice del regime fiscale dell'emittente
    """
    numero: str
    data: str
    emittente: dict
    destinatario: dict
    importo_totale: float
    aliquote_iva: list[dict]
    causale: str
    regime_fiscale: str


@dataclass
class EsitoTrasmissione:
    """Rappresenta l'esito di una trasmissione SDI.
    
    Attributes:
        id_trasmissione: Identificativo univoco della trasmissione
        data: Data della trasmissione
        esito: Stato della trasmissione (CONSEGNATA, RIFIUTATA, IN_ATTESA)
        descrizione: Descrizione dettagliata dell'esito
        nome_file: Nome del file associato
    """
    id_trasmissione: str
    data: str
    esito: Literal["CONSEGNATA", "RIFIUTATA", "IN_ATTESA"]
    descrizione: str
    nome_file: str


class SDIAdapter:
    """Adapter per il Sistema di Interscambio (SDI).
    
    Supporta due modalità operative:
    - local: scrive i file XML FPR12 su disco per testing e sviluppo
    - remote: richiede accreditamento presso l'Agenzia delle Entrate
    
    Esempio:
        adapter = SDIAdapter(mode="local", local_dir=Path("sdi_out"))
        fattura = FatturaElettronica(...)
        esito = adapter.invia(fattura)
    """
    
    def __init__(self, mode: str = "local", local_dir: Path = Path("sdi_out")):
        """Inizializza l'adapter SDI.
        
        Args:
            mode: Modalità operativa ("local" o "remote")
            local_dir: Directory locale per i file XML (solo modalità local)
        """
        self.mode = mode
        self.local_dir = local_dir
        self.local_dir.mkdir(parents=True, exist_ok=True)
    
    def invia(self, fattura: FatturaElettronica) -> EsitoTrasmissione:
        """Invia una fattura elettronica allo SDI.
        
        In modalità "local", genera il file XML FPR12 e lo salva su disco.
        In modalità "remote", solleva NotImplementedError (richiede accreditamento).
        
        Args:
            fattura: La fattura elettronica da inviare
            
        Returns:
            EsitoTrasmissione con lo stato dell'operazione
            
        Raises:
            NotImplementedError: Se la modalità è "remote" (richiede accreditamento)
        """
        if self.mode == "remote":
            raise NotImplementedError(
                "SDI remote transmission requires accreditation — use local file mode"
            )
        
        # Genera ID trasmissione univoco
        id_trasmissione = uuid4().hex
        progressivo_invio = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Genera XML FPR12
        xml_content = self._to_xml(fattura, id_trasmissione, progressivo_invio)
        
        # Crea nome file
        nome_file = f"{fattura.numero}_{fattura.data}.xml"
        file_path = self.local_dir / nome_file
        
        # Scrive il file XML
        file_path.write_text(xml_content, encoding="utf-8")
        
        return EsitoTrasmissione(
            id_trasmissione=id_trasmissione,
            data=datetime.now().isoformat(),
            esito="CONSEGNATA",
            descrizione="Fattura salvata in modalità locale",
            nome_file=str(file_path)
        )
    
    def _to_xml(
        self, 
        fattura: FatturaElettronica, 
        id_trasmissione: str, 
        progressivo_invio: str
    ) -> str:
        """Converte una FatturaElettronica in XML FPR12.
        
        Args:
            fattura: La fattura da convertire
            id_trasmissione: ID univoco della trasmissione
            progressivo_invio: Numero progressivo dell'invio
            
        Returns:
            Stringa XML formattata FPR12
        """
        # Namespace SDI
        NS = "http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2"
        NS_MAP = {"": NS}
        
        # Root element
        fattura_root = ET.Element(f"{{{NS}}}FatturaElettronica", version="FPR12")
        
        # === FATTURA ELETTRONICA HEADER ===
        header = ET.SubElement(fattura_root, f"{{{NS}}}FatturaElettronicaHeader")
        
        # DatiTrasmissione
        dati_trasmissione = ET.SubElement(header, f"{{{NS}}}DatiTrasmissione")
        ET.SubElement(dati_trasmissione, f"{{{NS}}}IdTrasmissione").text = id_trasmissione
        ET.SubElement(dati_trasmissione, f"{{{NS}}}ProgressivoInvio").text = progressivo_invio
        ET.SubElement(dati_trasmissione, f"{{{NS}}}FormatoTrasmissione").text = "SDI11"
        ET.SubElement(dati_trasmissione, f"{{{NS}}}CodiceDestinatario").text = fattura.destinatario.get("codice_destinatario", "XXXXXXX")
        
        # CedentePrestatore (Emittente)
        cedente = ET.SubElement(header, f"{{{NS}}}CedentePrestatore")
        dati_anagrafici_cedente = ET.SubElement(cedente, f"{{{NS}}}DatiAnagrafici")
        ET.SubElement(dati_anagrafici_cedente, f"{{{NS}}}IdFiscaleIVA").text = fattura.emittente.get("partita_iva", "")
        ET.SubElement(dati_anagrafici_cedente, f"{{{NS}}}CodiceFiscale").text = fattura.emittente.get("codice_fiscale", "")
        ET.SubElement(dati_anagrafici_cedente, f"{{{NS}}}RegimeFiscale").text = fattura.regime_fiscale
        
        anagrafica_cedente = ET.SubElement(cedente, f"{{{NS}}}Anagrafica")
        ET.SubElement(anagrafica_cedente, f"{{{NS}}}Denominazione").text = fattura.emittente.get("denominazione", "")
        
        sede_cedente = ET.SubElement(cedente, f"{{{NS}}}Sede")
        ET.SubElement(sede_cedente, f"{{{NS}}}Indirizzo").text = ""
        ET.SubElement(sede_cedente, f"{{{NS}}}CAP").text = ""
        ET.SubElement(sede_cedente, f"{{{NS}}}Comune").text = ""
        ET.SubElement(sede_cedente, f"{{{NS}}}Provincia").text = ""
        ET.SubElement(sede_cedente, f"{{{NS}}}Nazione").text = "IT"
        
        # CessionarioCommittente (Destinatario)
        cessionario = ET.SubElement(header, f"{{{NS}}}CessionarioCommittente")
        dati_anagrafici_cessionario = ET.SubElement(cessionario, f"{{{NS}}}DatiAnagrafici")
        ET.SubElement(dati_anagrafici_cessionario, f"{{{NS}}}CodiceFiscale").text = fattura.destinatario.get("codice_fiscale", "")
        if fattura.destinatario.get("partita_iva"):
            ET.SubElement(dati_anagrafici_cessionario, f"{{{NS}}}IdFiscaleIVA").text = fattura.destinatario.get("partita_iva", "")
        
        anagrafica_cessionario = ET.SubElement(cessionario, f"{{{NS}}}Anagrafica")
        ET.SubElement(anagrafica_cessionario, f"{{{NS}}}Denominazione").text = fattura.destinatario.get("denominazione", "")
        
        sede_cessionario = ET.SubElement(cessionario, f"{{{NS}}}Sede")
        ET.SubElement(sede_cessionario, f"{{{NS}}}Indirizzo").text = ""
        ET.SubElement(sede_cessionario, f"{{{NS}}}CAP").text = ""
        ET.SubElement(sede_cessionario, f"{{{NS}}}Comune").text = ""
        ET.SubElement(sede_cessionario, f"{{{NS}}}Provincia").text = ""
        ET.SubElement(sede_cessionario, f"{{{NS}}}Nazione").text = "IT"
        
        # === FATTURA ELETTRONICA BODY ===
        body = ET.SubElement(fattura_root, f"{{{NS}}}FatturaElettronicaBody")
        
        # DatiGenerali
        dati_generali = ET.SubElement(body, f"{{{NS}}}DatiGenerali")
        ET.SubElement(dati_generali, f"{{{NS}}}TipoDocumento").text = "TD01"
        ET.SubElement(dati_generali, f"{{{NS}}}Data").text = fattura.data
        ET.SubElement(dati_generali, f"{{{NS}}}Numero").text = fattura.numero
        
        # Importo totale
        for aliquota in fattura.aliquote_iva:
            ET.SubElement(dati_generali, f"{{{NS}}}ImportoTotaleDocumento").text = str(aliquota["imponibile"] + aliquota["imposta"])
        
        # Causale
        ET.SubElement(dati_generali, f"{{{NS}}}Causale").text = fattura.causale
        
        # DatiBeniServizi
        dati_beni_servizi = ET.SubElement(body, f"{{{NS}}}DatiBeniServizi")
        
        for aliquota in fattura.aliquote_iva:
            dettaglio_linee = ET.SubElement(dati_beni_servizi, f"{{{NS}}}DettaglioLinee")
            ET.SubElement(dettaglio_linee, f"{{{NS}}}NumeroLinea").text = str(fattura.aliquote_iva.index(aliquota) + 1)
            ET.SubElement(dettaglio_linee, f"{{{NS}}}Descrizione").text = fattura.causale
            ET.SubElement(dettaglio_linee, f"{{{NS}}}Quantita").text = "1.00"
            ET.SubElement(dettaglio_linee, f"{{{NS}}}PrezzoUnitario").text = str(aliquota["imponibile"])
            ET.SubElement(dettaglio_linee, f"{{{NS}}}PrezzoTotale").text = str(aliquota["imponibile"] + aliquota["imposta"])
            ET.SubElement(dettaglio_linee, f"{{{NS}}}AliquotaIVA").text = str(aliquota["aliquota"] * 100)
            
            dati_aliquote = ET.SubElement(dati_beni_servizi, f"{{{NS}}}DatiRiepilogo")
            ET.SubElement(dati_aliquote, f"{{{NS}}}AliquotaIVA").text = str(aliquota["aliquota"] * 100)
            ET.SubElement(dati_aliquote, f"{{{NS}}}ImponibileImporto").text = str(aliquota["imponibile"])
            ET.SubElement(dati_aliquote, f"{{{NS}}}Imposta").text = str(aliquota["imposta"])
        
        # DatiPagamento
        dati_pagamento = ET.SubElement(body, f"{{{NS}}}DatiPagamento")
        ET.SubElement(dati_pagamento, f"{{{NS}}}CondizioniPagamento").text = "TP02"
        ET.SubElement(dati_pagamento, f"{{{NS}}}DettaglioPagamento").text = str(fattura.importo_totale)
        
        # Converti a stringa XML
        xml_str = ET.tostring(fattura_root, encoding="utf-8", xml_declaration=True)
        
        # Formatta con indentazione
        root = ET.fromstring(xml_str)
        self._indent_xml(root)
        xml_str = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        
        return xml_str.decode("utf-8")
    
    def _indent_xml(self, elem: ET.Element, level: int = 0) -> None:
        """Aggiunge indentazione all'albero XML per formattazione leggibile.
        
        Args:
            elem: Elemento XML radice
            level: Livello di indentazione corrente
        """
        i = "\n" + "  " * level
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for child in elem:
                self._indent_xml(child, level + 1)
            if not child.tail or not child.tail.strip():
                child.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
    
    def _from_xml(self, xml_str: str) -> FatturaElettronica:
        """Converte XML FPR12 in una FatturaElettronica.
        
        Metodo inverso di _to_xml, utilizzato per testing e validazione round-trip.
        
        Args:
            xml_str: Stringa XML FPR12
            
        Returns:
            Oggetto FatturaElettronica parsato
        """
        root = ET.fromstring(xml_str)
        NS = "http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2"
        
        # Helper per trovare elementi
        def find(elem: ET.Element, tag: str) -> str:
            child = elem.find(f"{{{NS}}}{tag}")
            return child.text if child is not None else ""
        
        def find_elem(elem: ET.Element, tag: str) -> ET.Element | None:
            return elem.find(f"{{{NS}}}{tag}")
        
        # Header
        header = root.find(f"{{{NS}}}FatturaElettronicaHeader")
        dati_trasmissione = find_elem(header, "DatiTrasmissione")
        cedente = find_elem(header, "CedentePrestatore")
        cessionario = find_elem(header, "CessionarioCommittente")
        
        # Body
        body = root.find(f"{{{NS}}}FatturaElettronicaBody")
        dati_generali = find_elem(body, "DatiGenerali")
        dati_beni_servizi = find_elem(body, "DatiBeniServizi")
        
        # Estrai emittente
        dati_anagrafici_cedente = find_elem(cedente, "DatiAnagrafici")
        emittente = {
            "partita_iva": find(dati_anagrafici_cedente, "IdFiscaleIVA"),
            "codice_fiscale": find(dati_anagrafici_cedente, "CodiceFiscale"),
            "denominazione": find(find_elem(cedente, "Anagrafica"), "Denominazione")
        }
        
        # Estrai destinatario
        dati_anagrafici_cessionario = find_elem(cessionario, "DatiAnagrafici")
        destinatario = {
            "codice_fiscale": find(dati_anagrafici_cessionario, "CodiceFiscale"),
            "partita_iva": find(dati_anagrafici_cessionario, "IdFiscaleIVA"),
            "denominazione": find(find_elem(cessionario, "Anagrafica"), "Denominazione"),
            "codice_destinatario": find(dati_trasmissione, "CodiceDestinatario")
        }
        
        # Estrai dati generali
        numero = find(dati_generali, "Numero")
        data = find(dati_generali, "Data")
        causale = find(dati_generali, "Causale")
        regime_fiscale = find(dati_anagrafici_cedente, "RegimeFiscale")
        
        # Estrai aliquote IVA
        aliquote_iva = []
        riepilogo = dati_beni_servizi.findall(f"{{{NS}}}DatiRiepilogo")
        for r in riepilogo:
            aliquota = float(find(r, "AliquotaIVA")) / 100
            imponibile = float(find(r, "ImponibileImporto"))
            imposta = float(find(r, "Imposta"))
            aliquote_iva.append({
                "aliquota": aliquota,
                "imponibile": imponibile,
                "imposta": imposta
            })
        
        # Calcola importo totale
        importo_totale = sum(a["imponibile"] + a["imposta"] for a in aliquote_iva)
        
        return FatturaElettronica(
            numero=numero,
            data=data,
            emittente=emittente,
            destinatario=destinatario,
            importo_totale=importo_totale,
            aliquote_iva=aliquote_iva,
            causale=causale,
            regime_fiscale=regime_fiscale
        )
    
    def ricevi(self, id_trasmissione: str) -> EsitoTrasmissione | None:
        """Riceve una fattura dallo SDI.
        
        In modalità "local", cerca il file XML corrispondente nella directory locale.
        In modalità "remote", solleva NotImplementedError (richiede accreditamento).
        
        Args:
            id_trasmissione: ID della trasmissione da ricevere
            
        Returns:
            EsitoTrasmissione se trovata, None altrimenti
            
        Raises:
            NotImplementedError: Se la modalità è "remote" (richiede accreditamento)
        """
        if self.mode == "remote":
            raise NotImplementedError(
                "SDI remote transmission requires accreditation — use local file mode"
            )
        
        # Scansiona la directory locale per file corrispondenti
        for file_path in self.local_dir.glob("*.xml"):
            # In una implementazione reale, si leggerebbe l'ID dalla trasmissione
            # Per ora, restituiamo un esito fittizio per testing
            return EsitoTrasmissione(
                id_trasmissione=id_trasmissione,
                data=datetime.now().isoformat(),
                esito="IN_ATTESA",
                descrizione="Fattura in attesa di elaborazione",
                nome_file=str(file_path)
            )
        
        return None
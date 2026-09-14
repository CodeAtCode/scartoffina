# Formati di Esito — Documenti Contabili Italiani

**Base normativa**: Art. 2214-2220 c.c., DPR 633/72, OIC 12.

## Documenti Contabili Obbligatori

### Libro Giornale

**Obbligo**: Art. 2214 c.c. — obbligatorio per tutte le imprese

**Contenuto**:
- Registrazione cronologica di tutte le operazioni
- Data, numero, descrizione, dare/avere
- Riferimento al documento giustificativo

**Formato**:
```csv
data,num_operazione,descrizione,conto_dare,importo_dare,conto_avere,importo_avere,documento
2026-01-03,001,Fattura acquisto Beta,60.01,1000.00,40.01,1000.00,INV-BETA-123
2026-01-03,001,Fattura acquisto Beta,41.01,220.00,40.01,220.00,INV-BETA-123
2026-01-10,002,Fattura vendita Gamma,40.02,1220.00,70.01,1000.00,FT/2026/001
2026-01-10,002,Fattura vendita Gamma,40.02,1220.00,41.01,220.00,FT/2026/001
```

**Conservazione**: 10 anni (Art. 2220 c.c.)

**Bollatura**: Obbligatoria preventivamente (o generazione elettronica)

### Libro degli Inventari

**Obbligo**: Art. 2217 c.c. — obbligatorio per tutte le imprese

**Contenuto**:
- Descrizione dettagliata dei beni dell'azienda
- Valore di ciascun bene
- Passività e debiti

**Formato**:
```csv
data,codice,descrizione_bene,quantita,unita_misura,valor_unitario,valor_totale,categoria
2026-01-01,INV-001,Merce magazzino A,100,pezzi,10.00,1000.00,rimanenze
2026-01-01,INV-002,Macchinario X,1,unità,50000.00,50000.00,immobilizzazioni
2026-01-01,INV-003,Auto aziendale,1,unità,25000.00,25000.00,immobilizzazioni
```

**Conservazione**: 10 anni

### Registri IVA

**Obbligo**: Art. 24-25 DPR 633/72

**Tipologie**:
- **Registro vendite** (fatture emesse)
- **Registro acquisti** (fatture ricevute)
- **Registro beni strumentali** (per immobilizzazioni)

**Formato Registro Vendite**:
```csv
data,num_fattura,cliente,imponibile,aliquota,imposta,totale,codice_op
2026-01-10,FT/2026/001,Cliente Gamma,1000.00,22,220.00,1220.00,CE
2026-01-15,FT/2026/002,Cliente Delta,2000.00,10,200.00,2200.00,CE
2026-01-20,FT/2026/003,Cliente Estero UE,1500.00,0,0.00,1500.00,IN
```

**Formato Registro Acquisti**:
```csv
data,num_fattura,fornitore,imponibile,aliquota,imposta,totale,codice_op
2026-01-03,INV-BETA-123,Fornitore Beta,1000.00,22,220.00,1220.00,AC
2026-01-08,INV-GAMMA-456,Fornitore Gamma,500.00,22,110.00,610.00,AC
```

**Conservazione**: 10 anni

## Formati di Esportazione

### FEC (Fichier des Écritures Comptables) — Standard Europeo

**Nota**: L'Italia non ha un FEC obbligatorio, ma il registro IVA + libro giornale sono l'equivalente.

**Struttura JSON italiana**:
```json
{
  "version": "1.0",
  "company": {
    "name": "Alpha S.r.l.",
    "vat": "IT12345678901",
    "fiscal_year": "2026"
  },
  "entries": [
    {
      "date": "2026-01-03",
      "number": "001",
      "description": "Fattura acquisto Beta",
      "account_dare": "60.01",
      "amount_dare": 1000.00,
      "account_avere": "40.01",
      "amount_avere": 1000.00,
      "document": "INV-BETA-123"
    }
  ]
}
```

### Registro IVA CSV

**Formato standard per liquidazione**:
```csv
periodo,data_inizio,data_fine,iva_debito,iva_credito,saldo,versamento,credito_riportato
2026-01,2026-01-01,2026-01-31,3695.90,2420.00,1275.90,1275.90,0.00
2026-02,2026-02-01,2026-02-28,2100.00,1800.00,300.00,300.00,0.00
```

### Libro Giornale CSV

**Formato per controllo**:
```csv
data,num_operazione,conto,descrizione,dare,avere,bilancio
2026-01-03,001,60.01,Acquisto merci,1000.00,0.00,1000.00
2026-01-03,001,41.01,IVA acquisto,220.00,0.00,1220.00
2026-01-03,001,40.01,Fornitore Beta,0.00,1220.00,0.00
```

## Bilancio di Esercizio

### Stato Patrimoniale — Schema OIC 28

**Formato JSON**:
```json
{
  "tipo": "Stato Patrimoniale",
  "esercizio": "2026",
  "data_chiusura": "2026-12-31",
  "attivo": {
    "A_crediti_soci": 0.00,
    "B_immobilizzazioni": {
      "I_immateriali": 15000.00,
      "II_materiali": 75000.00,
      "III_finanziarie": 5000.00
    },
    "C_attivo_circolante": {
      "I_rimanenze": 10000.00,
      "II_crediti": 25000.00,
      "III_strumenti_finanziari": 0.00,
      "IV_disponibilita_liquide": 30000.00
    },
    "D_ratei_risconti_attivi": 11000.00
  },
  "passivo": {
    "A_patrimonio_netto": {
      "I_capitale": 10000.00,
      "II_riserve": 50000.00,
      "III_utile_esercizio": 20000.00
    },
    "B_fondi_rischi": 5000.00,
    "C_debiti": {
      "I_banche": 20000.00,
      "II_fornitori": 15000.00,
      "III_tributi": 8000.00,
      "IV_previdenza": 3000.00
    },
    "D_ratei_risconti_passivi": 500.00
  }
}
```

### Conto Economico — Schema OIC 28

**Formato JSON**:
```json
{
  "tipo": "Conto Economico",
  "esercizio": "2026",
  "A_valore_produzione": {
    "1_ricavi_vendite": 150000.00,
    "2_variazione_rimanenze": 5000.00,
    "3_altri_ricavi": 10000.00
  },
  "B_costi_produzione": {
    "4_materie": 50000.00,
    "5_servizi": 30000.00,
    "6_personale": 40000.00,
    "7_ammortamenti": 15000.00,
    "8_oneri_diversi": 5000.00
  },
  "C_proventi_oneri_finanziari": {
    "1_interessi_attivi": 500.00,
    "2_interessi_passivi": 2000.00
  },
  "D_imposte": 12000.00,
  "risultato_esercizio": 13500.00
}
```

### Nota Integrativa — Schema OIC 29

**Struttura**:
```json
{
  "tipo": "Nota Integrativa",
  "esercizio": "2026",
  "principi_contabili": "OIC 12, OIC 28, OIC 29",
  "dettaglio_immobilizzazioni": {
    "immateriali": {
      "costo_iniziale": 20000.00,
      "ammortamento_cumulato": 8000.00,
      "costo_finale": 18000.00,
      "ammortamento_esercizio": 3000.00
    },
    "materiali": {
      "costo_iniziale": 80000.00,
      "ammortamento_cumulato": 25000.00,
      "costo_finale": 90000.00,
      "ammortamento_esercizio": 12000.00
    }
  },
  "dettaglio_crediti": {
    "commerciali": 20000.00,
    "tributari": 3000.00,
    "altri": 2000.00,
    "svalutazione": 1000.00
  },
  "dettaglio_debiti": {
    "commerciali": 15000.00,
    "tributari": 5000.00,
    "previdenza": 3000.00,
    "finanziarie": 20000.00
  },
  "ratei_risconti": {
    "attivi": 11000.00,
    "passivi": 500.00
  }
}
```

## F24 — Modello di Versamento

**Struttura dati**:
```json
{
  "tipo": "F24",
  "anno_riferimento": "2026",
  "contribuente": {
    "codice_fiscale": "RSSMRA80A01H501U",
    "nome": "Mario Rossi",
    "indirizzo": "Via Roma 1, 00100 Roma"
  },
  "sezioni": {
    "erario": [
      {
        "codice_tributo": "1001",
        "descrizione": "IVA mensile saldo",
        "anno_riferimento": "2026",
        "mese_riferimento": "01",
        "importo": 1275.90,
        "acconto": false
      }
    ],
    "previdenza": []
  },
  "totale_debiti": 1275.90
}
```

## CSV per Importo Bancario

**Formato per riconciliazione**:
```csv
data,descrizione,importo_dare,importo_avere,bilancio,conto_riferimento
2026-01-03,bonifico_fornitore_beta,0.00,1220.00,1220.00,40.01
2026-01-10,incasso_cliente_gamma,1220.00,0.00,0.00,40.02
```

## XML FatturaPA

**Struttura minima** (FatturaPA v1.6.1):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<p:FatturaElettronica versione="FPR12" xmlns:p="http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2">
  <FatturaElettronicaHeader>
    <DatiTrasmissione>
      <IdTrasmittente>
        <IdPaese>IT</IdPaese>
        <IdCodice>12345678901</IdCodice>
      </IdTrasmittente>
      <ProgressivoInvio>00001</ProgressivoInvio>
      <FormatoTrasmissione>FPR12</FormatoTrasmissione>
      <CodiceDestinatario>ABCDEFG</CodiceDestinatario>
    </DatiTrasmissione>
    <CedentePrestatore>
      <DatiAnagrafici>
        <IdFiscaleIVA>
          <IdPaese>IT</IdPaese>
          <IdCodice>12345678901</IdCodice>
        </IdFiscaleIVA>
        <Anagrafica>
          <Denominazione>Alpha S.r.l.</Denominazione>
        </Anagrafica>
        <RegimeFiscale>RF01</RegimeFiscale>
      </DatiAnagrafici>
      <Sede>
        <Indirizzo>Via Roma 1</Indirizzo>
        <CAP>00100</CAP>
        <Comune>Roma</Comune>
        <Provincia>RM</Provincia>
        <Nazione>IT</Nazione>
      </Sede>
    </CedentePrestatore>
  </FatturaElettronicaHeader>
  <FatturaElettronicaBody>
    <DatiGenerali>
      <DatiGeneraliDocumento>
        <TipoDocumento>TD01</TipoDocumento>
        <Divisa>EUR</Divisa>
        <Data>2026-01-10</Data>
        <Numero>FT/2026/001</Numero>
        <ImportoTotaleDocumento>1220.00</ImportoTotaleDocumento>
      </DatiGeneraliDocumento>
    </DatiGenerali>
    <DatiBeniServizi>
      <DettaglioLinee>
        <NumeroLinea>1</NumeroLinea>
        <Descrizione>Servizio di consulenza</Descrizione>
        <Quantita>1.00</Quantita>
        <PrezzoUnitario>1000.00</PrezzoUnitario>
        <PrezzoTotale>1000.00</PrezzoTotale>
        <AliquotaIVA>22.00</AliquotaIVA>
      </DettaglioLinee>
      <DatiRiepilogo>
        <AliquotaIVA>22.00</AliquotaIVA>
        <ImponibileImporto>1000.00</ImponibileImporto>
        <Imposta>220.00</Imposta>
      </DatiRiepilogo>
    </DatiBeniServizi>
  </FatturaElettronicaBody>
</p:FatturaElettronica>
```

## Note Operative

1. **Conservazione sostitutiva**: I documenti contabili possono essere conservati digitalmente (DM 17/06/2014)

2. **Firma digitale**: Obbligatoria per i documenti con valore legale (bilancio, fatture elettroniche)

3. **Formati accettati**: PDF/A per documenti, XML per fatture elettroniche, CSV/JSON per esportazioni

4. **Integrità**: I file devono essere protetti da alterazioni (firma digitale o timestamp)

5. **Indicizzazione**: Ogni documento deve essere indicizzato per data, numero e tipo per facile recupero
# Modulo SDI - Sistema di Interscambio

## Cos'è SDI

Il **Sistema di Interscambio (SDI)** è il sistema informatico dell'Agenzia delle Entrate che gestisce lo scambio di fatture elettroniche in Italia. Dal 1° gennaio 2019, la fatturazione elettronica è obbligatoria per tutte le fatture emesse verso soggetti IVA italiani.

Scartoffina utilizza questo modulo come **adapter condiviso** tra le diverse skill (commercialista, notaio, amministratore-condominio) per inviare e ricevere fatture elettroniche in modo standardizzato.

## Modalità operative

### Modalità "local" (default)

In questa modalità, il modulo **scrive i file XML FPR12 su disco** invece di inviarli realmente allo SDI. Questa modalità è pensata per:

- **Testing e sviluppo**: verificare la corretta generazione dei file XML
- **Validazione**: controllare il formato FPR12 prima dell'invio reale
- **Sviluppo locale**: lavorare senza richiedere accreditamento presso l'Agenzia delle Entrate

Esempio:
```python
from integrations.sdi import SDIAdapter, FatturaElettronica
from pathlib import Path

# Inizializza in modalità locale
adapter = SDIAdapter(mode="local", local_dir=Path("sdi_out"))

# Crea una fattura
fattura = FatturaElettronica(
    numero="FT001",
    data="2026-08-05",
    emittente={
        "codice_fiscale": "RSSMRA01A01H501Z",
        "partita_iva": "01234567890",
        "denominazione": "Test SRL"
    },
    destinatario={
        "codice_fiscale": "BNDRSS02B01H501W",
        "partita_iva": "09876543210",
        "denominazione": "Cliente SRL",
        "codice_destinatario": "ABC1234"
    },
    importo_totale=122.00,
    aliquote_iva=[{
        "aliquota": 0.22,
        "imponibile": 100.00,
        "imposta": 22.00
    }],
    causale="Fattura test",
    regime_fiscale="RF01"
)

# Invia (salva su disco)
esito = adapter.invia(fattura)
print(f"Fattura salvata: {esito.nome_file}")
```

### Modalità "remote"

In questa modalità, il modulo tenterebbe di inviare realmente le fatture allo SDI tramite i servizi web dell'Agenzia delle Entrate.

⚠️ **Attenzione**: Questa modalità richiede **accreditamento presso l'Agenzia delle Entrate** e non è ancora implementata. Al momento solleva un `NotImplementedError`:

```python
adapter = SDIAdapter(mode="remote")
fattura = FatturaElettronica(...)
adapter.invia(fattura)  # Solleva NotImplementedError
```

Per inviare fatture realmente, è necessario:
1. Essere accreditati come intermediario presso l'Agenzia delle Entrate
2. Ottenere le credenziali certificate (certificato digitale, credenziali SPID/CIE)
3. Implementare l'adattatore per i servizi web SDI (SOAP/REST)

## Formato FPR12

Il formato **FPR12** (Fattura Priva tra Privati) è lo standard per la fatturazione elettronica tra soggetti privati in Italia.

### Struttura XML

```xml
<FatturaElettronica versione="FPR12" xmlns="http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2">
  <FatturaElettronicaHeader>
    <DatiTrasmissione>
      <IdTrasmissione>...</IdTrasmissione>
      <ProgressivoInvio>...</ProgressivoInvio>
      <FormatoTrasmissione>SDI11</FormatoTrasmissione>
      <CodiceDestinatario>...</CodiceDestinatario>
    </DatiTrasmissione>
    <CedentePrestatore>
      <DatiAnagrafici>
        <IdFiscaleIVA>...</IdFiscaleIVA>
        <CodiceFiscale>...</CodiceFiscale>
        <RegimeFiscale>...</RegimeFiscale>
      </DatiAnagrafici>
      <Anagrafica>
        <Denominazione>...</Denominazione>
      </Anagrafica>
      <Sede>...</Sede>
    </CedentePrestatore>
    <CessionarioCommittente>
      <DatiAnagrafici>...</DatiAnagrafici>
      <Anagrafica>...</Anagrafica>
      <Sede>...</Sede>
    </CessionarioCommittente>
  </FatturaElettronicaHeader>
  <FatturaElettronicaBody>
    <DatiGenerali>
      <TipoDocumento>TD01</TipoDocumento>
      <Data>...</Data>
      <Numero>...</Numero>
      <ImportoTotaleDocumento>...</ImportoTotaleDocumento>
      <Causale>...</Causale>
    </DatiGenerali>
    <DatiBeniServizi>
      <DettaglioLinee>...</DettaglioLinee>
      <DatiRiepilogo>...</DatiRiepilogo>
    </DatiBeniServizi>
    <DatiPagamento>...</DatiPagamento>
  </FatturaElettronicaBody>
</FatturaElettronica>
```

### Campi principali

| Campo | Descrizione |
|-------|-------------|
| `IdTrasmissione` | ID univoco della trasmissione (UUID) |
| `ProgressivoInvio` | Timestamp di invio (YYYYMMDDHHMMSS) |
| `FormatoTrasmissione` | "SDI11" per FPR12 |
| `CodiceDestinatario` | Codice a 7 caratteri del destinatario (o "XXXXXXX" per PEC) |
| `IdFiscaleIVA` | Partita IVA del cedente |
| `CodiceFiscale` | Codice fiscale del cedente/cessionario |
| `RegimeFiscale` | Codice del regime fiscale (es. "RF01" per ordinario) |
| `TipoDocumento` | "TD01" per fattura |
| `AliquotaIVA` | Aliquota IVA applicata (es. "22.00" per 22%) |

## Limiti del modulo

⚠️ **Questo modulo non sostituisce un intermediario accreditato**. Le limitazioni attuali sono:

1. **Nessun invio reale**: la modalità "remote" non è implementata (richiede accreditamento)
2. **Nessuna gestione dello stato**: non si può verificare lo stato reale delle trasmissioni (accettata, scartata, ecc.)
3. **Validazione limitata**: non si eseguono validazioni complete contro lo schema XSD FPR12
4. **Dati incompleti**: alcuni campi opzionali dello schema FPR12 non sono gestiti (indirizzi completi, rappresentante fiscale, ecc.)

## Validazione

Per verificare che il modulo funzioni correttamente:

```bash
# Parse Python
python3 -c "import ast; ast.parse(open('integrations/sdi/adapter.py').read()); print('Parse OK')"

# Test integrazione
python3 -c "
from integrations.sdi import SDIAdapter, FatturaElettronica
from pathlib import Path
import tempfile

adapter = SDIAdapter(mode='local', local_dir=Path(tempfile.mkdtemp()))
fattura = FatturaElettronica(
    numero='FT001',
    data='2026-08-05',
    emittente={'codice_fiscale':'RSSMRA01A01H501Z','partita_iva':'01234567890','denominazione':'Test SRL'},
    destinatario={'codice_fiscale':'BNDRSS02B01H501W','partita_iva':'09876543210','denominazione':'Cliente SRL','codice_destinatario':'ABC1234'},
    importo_totale=122.00,
    aliquote_iva=[{'aliquota':0.22,'imponibile':100.00,'imposta':22.00}],
    causale='Fattura test',
    regime_fiscale='RF01'
)
esito = adapter.invia(fattura)
assert esito.esito == 'CONSEGNATA'
print('Integration OK:', esito.id_trasmissione)
"
```

## Prossimi sviluppi

- [ ] Implementazione modalità "remote" con servizi web SDI
- [ ] Validazione completa contro schema XSD FPR12
- [ ] Gestione dello stato delle trasmissioni (accettazione/scarto)
- [ ] Supporto per altri formati (PA per la pubblica amministrazione)
- [ ] Gestione dei certificati digitali per la firma XML
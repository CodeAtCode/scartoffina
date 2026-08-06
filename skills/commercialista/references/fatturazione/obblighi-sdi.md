# Obblighi SDI — Fatturazione Elettronica

**Base normativa**: Art. 1, commi 209-214, L. 208/2015 (Legge di Stabilità 2016), Decreti attuativi 2018-2019.

## Panoramica SDI

Lo **Sistema di Interscambio (SDI)** è l'ente dell'Agenzia delle Entrate che gestisce la fatturazione elettronica obbligatoria in Italia dal 1° gennaio 2019.

**Funzioni dello SDI**:
1. Ricevere le fatture elettroniche dai cedenti/prestatori
2. Validare la struttura e i dati
3. Trasmettere le fatture ai clienti (cessionari/committenti)
4. Archiviare le fatture per 5 anni
5. Notificare lo stato di consegna

## Obblighi di Fatturazione Elettronica

### Soggetti Obbligati

**Tutti i soggetti IVA residenti in Italia**:
- Ditte individuali
- Società di persone (SNC, SAS)
- Società di capitali (SRL, SPA, SRLS)
- Società semplici (per attività commerciali)
- Professionisti

**Eccezioni**:
- Soggetti in regime di franchigia IVA (art. 34 DPR 633/72) — opzionale
- Soggetti con IVA intracomunitaria ma senza stabile organizzazione in Italia

### Tipologie di Operazioni

| Operazione | Obbligatoria? | Formato |
|------------|---------------|---------|
| B2B nazionale | Sì | FPR12 |
| B2C nazionale | Sì | FPR12 |
| B2G (PA) | Sì | FPA12 |
| Intracomunitario | No (ma consigliato) | FPR12 |
| Export | No (ma consigliato) | FPR12 |

## Formati di Fattura

### FPR12 — FatturaPA per Privati

**Utilizzo**: Operazioni B2B e B2C

**Caratteristiche**:
- Formato XML conforme allo schema FatturaPA v1.6.1
- Codifica UTF-8
- Dimensione massima: 5 MB
- Firma digitale obbligatoria

### FPA12 — FatturaPA per Pubbliche Amministrazioni

**Utilizzo**: Operazioni con PA

**Caratteristiche**:
- Stesso formato FPR12
- Campo `CodiceDestinatario` specifico della PA
- Obbligo di indicazione CIG/CUP per appalti

## Codice Destinatario

### Cos'è

Il **codice destinatario** è un identificativo univoco di 7 caratteri che indica dove inviare la fattura elettronica.

### Come Ottenere

1. **Per aziende/private**: Chiedere al cliente il proprio codice
2. **Per PA**: Il codice è pubblicato sul sito dell'ente
3. **Se sconosciuto**: Usare `XXXXXXX` (7 volte X)

### Ricerca Codice PA

```
https://www.indire.it/listapal/
```

## Canali di Invio

### 1. Invio Diretto (Gratuito)

**Piattaforma**: https://www.fatture.e.gov.it

**Caratteristiche**:
- Gratuito
- Interfaccia web
- Adatto per volumi bassi (< 100 fatture/mese)
- Firma digitale necessaria

### 2. Intermediari Abilitati

**Tipologie**:
- **Commercialisti** con software abilitato
- **CAF** (Centri di Assistenza Fiscale)
- **Piattaforme terze** (Aruba, Fatture in Cloud, etc.)

**Costi**: Variabili (da 0,10€ a 1€ per fattura)

### 3. PEC (Posta Elettronica Certificata)

**Utilizzo**: Solo se il cliente ha indicato PEC come metodo di ricezione

**Formato**: XML allegato alla PEC

## Ricezione Fatture

### Obbligo di Ricezione

**Dal 1° gennaio 2019**: Tutti i soggetti IVA devono essere in grado di ricevere fatture elettroniche.

### Metodi di Ricezione

1. **Tramite software gestionale** (consigliato)
2. **Tramite piattaforma web SDI** (gratuita)
3. **Tramite intermediario**

### Codice Destinatario per Ricezione

Ogni azienda deve avere un proprio codice destinatario per ricevere fatture.

**Come ottenere**:
1. Registrarsi sul sito SDI
2. Generare il proprio codice (7 caratteri)
3. Comunicarlo ai fornitori

## Conservazione

### Obblighi

**Durata**: 10 anni (Art. 2220 c.c.)

**Metodo**: Conservazione sostitutiva a norma (DM 17/06/2014)

**Requisiti**:
- Firma digitale del documento
- Timestamp di conservazione
- Indicizzazione per ricerca
- Integrità garantita

### Costi Conservazione

- **SDI**: 0,50€ per fattura (opzionale, per 5 anni)
- **Conservazione a lungo termine**: Variabile per fornitore

## Scadenze e Tempistiche

### Invio Fattura

**Termine**: Entro il 12° giorno del mese successivo all'emissione

**Esempio**:
- Fattura del 15 gennaio → Invio entro il 12 febbraio

### Tempi di Consegna

**SDI elabora**:
- Fatture inviate entro le 12:00 → Consegna nello stesso giorno
- Fatture inviate dopo le 12:00 → Consegna il giorno lavorativo successivo

### Accettazione/Rifiuto

**Cliente ha 5 giorni** per:
- Accettare la fattura
- Rifiutare la fattura (con motivazione)
- Non fare nulla (accettazione tacita dopo 5 giorni)

## Errori Comuni

### 1. Codice Destinatario Errato

**Errore**: Codice non valido o inesistente

**Soluzione**: Verificare il codice con il cliente

### 2. Dati Fiscali Inconsistenti

**Errore**: P.IVA, CF o denominazione non corrispondono

**Soluzione**: Correggere i dati nel file XML

### 3. Formato XML Non Valido

**Errore**: XML non conforme allo schema XSD

**Soluzione**: Validare con lo schema FatturaPA v1.6.1

### 4. Firma Digitale Mancante

**Errore**: Documento non firmato

**Soluzione**: Firmare digitalmente l'XML prima dell'invio

## Stati della Fattura

| Stato | Descrizione |
|-------|-------------|
| `ACCETTATA` | Cliente ha accettato la fattura |
| `RIFIUTATA` | Cliente ha rifiutato la fattura |
| `SCARTATO` | SDI ha rifiutato la fattura (errore di formato) |
| `CONSEGNATO` | Fattura consegnata al destinatario |
| `NOTIFICATO` | Stato notificato al mittente |
| `IN_LAVORAZIONE` | SDI sta elaborando la fattura |

## Sanzioni

### Mancata Emissione

**Sanzione**: 90% dell'importo della fattura (minimo 25€)

### Invio Fuori Termine

**Sanzione**: 90% dell'importo (minimo 25€)

### Mancata Ricezione

**Sanzione**: 90% dell'importo della fattura non ricevuta

### Riduzioni Sanzioni

- **Ravvedimento operoso**: Sanzione ridotta se corretto prima dell'accertamento
- **Mancata infrazione**: Se l'errore è materiale e non sostanziale

## Integrazione con SDI

### API SDI

**Endpoint**: https://www.fatture.e.gov.it/sdi

**Metodi**:
- `invioFattura` — Invio fattura
- `ricercaStato` — Ricerca stato fattura
- `ricercaFatture` — Ricerca fatture ricevute

### Autenticazione

**Metodi**:
- SPID (Sistema Pubblico di Identità Digitale)
- CIE (Carta d'Identità Elettronica)
- CNS (Carta Nazionale dei Servizi)

## Note Operative

1. **Backup**: Conservare copia locale di tutte le fatture inviate e ricevute

2. **Validazione**: Validare sempre l'XML prima dell'invio

3. **Firma**: Firmare digitalmente ogni fattura

4. **Monitoraggio**: Controllare regolarmente lo stato delle fatture inviate

5. **Archiviazione**: Archiviare le fatture ricevute nel sistema contabile
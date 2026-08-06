# Setup Guidato — Prima Utilizzazione

**Scopo**: Configurare la skill `commercialista` per la prima volta, creando il file `company.json` e verificando i dati di riferimento.

## Prerequisiti

Prima di iniziare, verificare:
- [ ] Scartoffina installato e funzionante
- [ ] Python 3.10+ disponibile
- [ ] Accesso a internet per verificare dati fiscali

## Passo 1: Verificare i File di Riferimento

Controllare che i file di dati esistano nella directory `data/`:

```bash
ls -la data/
```

**File richiesti**:
- `aliquote-iva.json` — Aliquote IVA aggiornate
- `scaglioni-irpef.json` — Scaglioni IRPEF annuali
- `codici-tributo-f24.json` — Codici tributo F24
- `piano-conti-oic.json` — Piano dei conti conforme OIC
- `calendario-fiscale.json` — Scadenze fiscali

**Verifica freschezza**:
```bash
python3 -c "import json; d=json.load(open('data/aliquote-iva.json')); print('Verificato:', d.get('_meta', {}).get('verified_at', 'N/A'))"
```

Se `_meta.verified_at` è nel passato (> 6 mesi), aggiornare i dati:
```bash
make verify
```

## Passo 2: Creare company.json

Copiare il file esempio:
```bash
cp company.example.json company.json
```

**Attenzione**: `company.json` è in `.gitignore` — non va mai committato con dati reali.

## Passo 3: Compilare company.json

### Sezione 1: Identificazione Azienda

```json
{
  "ragione_sociale": "Alpha S.r.l.",
  "forma_giuridica": "SRL",
  "sede_legale": {
    "indirizzo": "Via Roma 1",
    "cap": "00100",
    "comune": "Roma",
    "provincia": "RM",
    "regione": "Lazio",
    "paese": "IT"
  },
  "codice_fiscale": "12345678901",
  "partita_iva": "IT12345678901",
  "siret": null,
  "ateco": "62.01.00"
}
```

**Campi obbligatori**:
- `ragione_sociale`: Nome completo dell'azienda
- `forma_giuridica`: SRL, SPA, SRLS, SNC, SAS, DITTA_INDIVIDUALE
- `sede_legale`: Indirizzo completo
- `partita_iva`: Formato IT + 11 cifre
- `ateco`: Codice ATECO attività

### Sezione 2: Regime Contabile

```json
"regime_contabile": "ordinaria",
```

**Opzioni**:
- `ordinaria`: Contabilità completa (libro giornale, inventari, registri IVA)
- `semplificata`: Registrazioni sintetiche (per piccole imprese)

### Sezione 3: Esercizio Fiscale

```json
"esercizio_fiscale": {
  "inizio": "2026-01-01",
  "fine": "2026-12-31"
}
```

**Nota**: Per la maggior parte delle aziende, l'esercizio coincide con l'anno solare.

### Sezione 4: Fatturazione

```json
"fatturazione": {
  "prefix": "FT",
  "next_number": 1,
  "avoir_prefix": "AV",
  "avoir_next_number": 1,
  "default_terms_days": 30,
  "default_payment_method": "bonifico"
}
```

**Campi**:
- `prefix`: Prefisso fatture (es. "FT" per fattura)
- `next_number`: Numero progressivo corrente
- `avoir_prefix`: Prefisso note di credito (es. "AV" per avere)
- `default_terms_days`: Termini di pagamento default (giorni)
- `default_payment_method`: Metodo di pagamento default

### Sezione 5: Dati Bancari

```json
"banche": [
  {
    "id": "unicredit",
    "nome": "UniCredit",
    "iban": "IT00X0000000000000000000000",
    "bic": "UNCRITMM",
    "conto_corrente": "3.04.003"
  }
]
```

**Nota**: Il campo `conto_corrente` è il conto del piano dei conti dove registrare i movimenti.

### Sezione 6: IVA

```json
"iva": {
  "regime": "reale",
  "periodicita_liquidazione": "mensile",
  "aliquota_default": 22,
  "pro_rata": null
}
```

**Campi**:
- `regime`: `reale` (normal), `franco` (franchise), `simplifie`
- `periodicita_liquidazione`: `mensile` o `trimestrale`
- `aliquota_default`: Aliquota IVA principale (22, 10, 5, 4)
- `pro_rata`: Percentuale di detrazione IVA (se operazioni esenti)

### Sezione 7: Imposte

```json
"imposte": {
  "IRES": 24,
  "IRAP_regionale": 4.45,
  "addizionale_comunale": 0.80
}
```

**Nota**: Verificare l'aliquota IRAP regionale specifica.

### Sezione 8: Contatti

```json
"contatti": {
  "email": "amministrazione@alpha.it",
  "telefono": "+39 06 12345678",
  "commercialista": {
    "nome": "Studio Rossi",
    "email": "info@studiorossi.it",
    "telefono": "+39 06 87654321"
  }
}
```

## Passo 4: Verificare la Configurazione

Eseguire lo script di verifica:
```bash
python3 skills/commercialista/scripts/validate_company.py
```

**Output atteso**:
```
✓ company.json valido
✓ Regime contabile: ordinaria
✓ Esercizio fiscale: 2026-01-01 → 2026-12-31
✓ Fatturazione: prefix=FT, next_number=1
✓ Aliquota IVA default: 22%
✓ IRAP regionale: 4.45% (Lazio)
```

## Passo 5: Configurare Integrazioni (Opzionale)

### Qonto (se utilizzato)

```json
"integrations": {
  "qonto": {
    "enabled": true,
    "organization_slug": "alpha-srl",
    "api_secret": "qonto_secret_key"
  }
}
```

**Nota**: L'API secret va salvato in `.env`, non in `company.json`.

### Stripe (se utilizzato)

```json
"integrations": {
  "stripe": {
    "enabled": true,
    "account_id": "acct_1234567890",
    "api_key": "sk_live_xxx"
  }
}
```

## Passo 6: Configurare Ambiente

Creare file `.env` alla radice del progetto:
```bash
SCARTOFFINA_COMPANY_FILE=./company.json
SCARTOFFINA_DATA_DIR=./data
SDI_ENDPOINT=http://localhost:8080/api/sdi
```

**Campi**:
- `SCARTOFFINA_COMPANY_FILE`: Percorso al file company.json
- `SCARTOFFINA_DATA_DIR`: Directory dei dati condivisi
- `SDI_ENDPOINT`: Endpoint SDI per fatturazione elettronica (opzionale)

## Passo 7: Testare la Configurazione

Eseguire un calcolo di test:
```bash
python3 skills/commercialista/scripts/calc.py iva --imponibile 1000 --aliquota 22
```

**Output atteso**:
```json
{
  "imponibile": 1000.00,
  "aliquota": 22,
  "imposta": 220.00,
  "totale": 1220.00
}
```

## Checklist Finale

```
□ company.json creato e compilato
□ Dati di riferimento verificati (verified_at recente)
□ Regime contabile configurato
□ Esercizio fiscale definito
□ Fatturazione configurata (prefix, next_number)
□ Dati bancari inseriti
□ Aliquote IVA verificate
□ Aliquote imposte verificate (IRES, IRAP)
□ Script di test eseguiti con successo
□ Integrazioni configurate (se applicabile)
```

## Risoluzione Problemi

### company.json non valido

**Errore**: `JSONDecodeError: Expecting property name`

**Soluzione**: Verificare la sintassi JSON (virgole, virgolette, parentesi)
```bash
python3 -m json.tool company.json > /dev/null && echo "Valido" || echo "Invalido"
```

### Dati fiscali obsoleti

**Errore**: `_meta.verified_at` nel passato

**Soluzione**: Eseguire `make verify` per aggiornare i dati

### Aliquota IRAP errata

**Errore**: IRAP regionale non corretta

**Soluzione**: Verificare l'aliquota IRAP della regione sul sito dell'Agenzia delle Entrate

## Note Operative

1. **Sicurezza**: Non committare `company.json` con dati reali — è in `.gitignore`

2. **Backup**: Mantenere un backup di `company.json` in luogo sicuro

3. **Aggiornamenti**: Verificare annualmente l'aggiornamento di aliquote e scadenze

4. **Commercialista**: Condividere `company.json` con il commercialista per assistenza
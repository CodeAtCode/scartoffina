# Setup Fatturazione — Campi Obbligatori

**Scopo**: Configurare correttamente i campi di fatturazione in `company.json` per garantire la conformità alle normative italiane.

## Campi Obbligatori in company.json

### Sezione Fatturazione

```json
"fatturazione": {
  "prefix": "FT",
  "next_number": 1,
  "year": 2026,
  "avoir_prefix": "AV",
  "avoir_next_number": 1,
  "default_terms_days": 30,
  "default_payment_method": "bonifico",
  "late_penalty_enabled": true,
  "late_penalty_rate": "3x_legal",
  "recovery_fee": 40.00,
  "escompte_enabled": false,
  "escompte_rate": 0
}
```

### Campi Dettagliati

| Campo | Tipo | Obbligatorio | Descrizione |
|-------|------|--------------|-------------|
| `prefix` | string | Sì | Prefisso fatture (es. "FT", "FATTURA") |
| `next_number` | integer | Sì | Progressivo corrente (resetta ogni anno) |
| `year` | integer | Sì | Anno di riferimento del progressivo |
| `avoir_prefix` | string | Sì | Prefisso note di credito (es. "AV", "NC") |
| `avoir_next_number` | integer | Sì | Progressivo note di credito |
| `default_terms_days` | integer | Sì | Termini di pagamento default (giorni) |
| `default_payment_method` | string | Sì | Metodo di pagamento default |
| `late_penalty_rate` | string | No | Tasso penali ritardo ("3x_legal" o numero) |
| `recovery_fee` | float | No | Indennità forfettaria recupero (40€ default) |
| `escompte_rate` | float | No | Tasso sconto per anticipato (0 = disabilitato) |

### Valori Validi per `default_payment_method`

- `bonifico` — Bonifico bancario
- `assegno` — Assegno
- `contanti` — Contanti (limiti di legge)
- `carta` — Carta di credito/debito
- `rid` — RID (debito diretto)
- `sepa_direct_debit` — Addebito SEPA

### Valori Validi per `late_penalty_rate`

- `3x_legal` — 3 volte tasso legale (obbligatorio per B2B)
- Numero (es. `8.5`) — Tasso percentuale fisso

## Campi FatturaPA (Fatturazione Elettronica)

```json
"einvoicing": {
  "enabled": true,
  "formato_trasmissione": "FPR12",
  "codice_destinatario": "ABCDEFG",
  "pec": "alpha.srl@pec.it",
  "peppol_id": null,
  "intermediario": "sdi",
  "reception_ready": true,
  "emission_ready": true
}
```

### Campi FatturaPA

| Campo | Tipo | Obbligatorio | Descrizione |
|-------|------|--------------|-------------|
| `enabled` | boolean | Sì | Fatturazione elettronica abilitata |
| `formato_trasmissione` | string | Sì | FPR12 (B2B), FPA12 (PA) |
| `codice_destinatario` | string | No | Codice destinatario SDI (7 caratteri) |
| `pec` | string | No | Indirizzo PEC per ricezione |
| `peppol_id` | string | No | Identificativo PEPPOL (formato iso6523:xxxx) |
| `intermediario` | string | No | intermediario scelto (sdi, aruba, pec, etc.) |
| `reception_ready` | boolean | Sì | Pronto a ricevere fatture elettroniche |
| `emission_ready` | boolean | Sì | Pronto a emettere fatture elettroniche |

### Formati di Trasmissione

- `FPR12` — FatturaPA per privati (B2B, B2C)
- `FPA12` — FatturaPA per Pubbliche Amministrazioni

### Codice Destinatario

**Formato**: 7 caratteri alfanumerici

**Valori**:
- `XXXXXXX` — Se il cliente non ha codice (privati senza PEC)
- `ABCDEFG` — Codice specifico del cliente (da chiedere)
- `0000000` — Per invio diretto via PEC

## Campi Azienda (Cedente/Prestatore)

```json
"azienda": {
  "ragione_sociale": "Alpha S.r.l.",
  "nome_commerciale": "Alpha",
  "forma_giuridica": "SRL",
  "capitale_sociale": 10000.00,
  "sede_legale": {
    "indirizzo": "Via Roma 1",
    "numero_civico": "1",
    "cap": "00100",
    "comune": "Roma",
    "provincia": "RM",
    "regione": "Lazio",
    "paese": "IT"
  },
  "codice_fiscale": "12345678901",
  "partita_iva": "IT12345678901",
  "registro_imprese": "RM-123456",
  "rea": "RM-123456",
  "iscrizioni": {
    "camera_commercio": true,
    "albo_imprese": false
  }
}
```

### Campi Obbligatori per Fattura

| Campo | Base Legale | Esempio |
|-------|-------------|---------|
| `ragione_sociale` | Art. 242 nonies A CGI | "Alpha S.r.l." |
| `sede_legale.indirizzo` | Art. 242 nonies A CGI | "Via Roma 1" |
| `sede_legale.cap` | Art. 242 nonies A CGI | "00100" |
| `sede_legale.comune` | Art. 242 nonies A CGI | "Roma" |
| `sede_legale.provincia` | Art. 242 nonies A CGI | "RM" |
| `partita_iva` | Art. 242 nonies A CGI | "IT12345678901" |
| `forma_giuridica` | Codice Commercio | "SRL" |
| `capitale_sociale` | Codice Commercio | "10000.00" |

## Campi Pagamento

```json
"pagamento": {
  "iban": "IT00X0000000000000000000000",
  "bic": "UNCRITMM",
  "banca": "UniCredit",
  "intestatario": "Alpha S.r.l.",
  "termini_testo": "Pagamento entro 30 giorni data fattura senza interessi",
  "penali_testo": "In caso di ritardo, saranno applicate penali pari a 3 volte il tasso legale",
  "recovery_fee_testo": "Indennità forfettaria di mora: € 40,00"
}
```

### Campi Pagamento

| Campo | Descrizione |
|-------|-------------|
| `iban` | IBAN per bonifici |
| `bic` | BIC/SWIFT della banca |
| `banca` | Nome della banca |
| `intestatario` | Intestatario del conto |
| `termini_testo` | Testo condizioni di pagamento |
| `penali_testo` | Testo penali di ritardo |
| `recovery_fee_testo` | Testo indennità recupero |

## Validazione

### Script di Validazione

Eseguire:
```bash
python3 skills/commercialista/scripts/validate_fattura.py --check-company
```

**Controlli eseguiti**:
1. Presenza tutti i campi obbligatori
2. Formato P.IVA valido
3. Formato IBAN valido
4. Prefisso fattura non vuoto
5. Progressivo numerico positivo
6. Termini di pagamento ragionevoli (≤ 60 giorni per B2B)

### Errori Comuni

**Errore**: `Missing required field: fatturazione.prefix`

**Soluzione**: Aggiungere campo `prefix` in `fatturazione`

**Errore**: `Invalid VAT number format`

**Soluzione**: P.IVA deve iniziare con "IT" seguito da 11 cifre

**Errore**: `Invalid IBAN format`

**Soluzione**: IBAN deve essere 27 caratteri per Italia (IT + 2 lettere + 23 cifre)

## Aggiornamento Progressivo

### Reset Annuale

Al 1° gennaio di ogni anno, il progressivo deve essere resettato:

```json
"fatturazione": {
  "prefix": "FT",
  "next_number": 1,
  "year": 2027
}
```

**Nota**: Il numero di fattura deve essere cronologico e continuo all'interno dell'anno.

### Incremento dopo Fattura

Dopo ogni fattura emessa, incrementare `next_number`:

```bash
python3 -c "import json; d=json.load(open('company.json')); d['fatturazione']['next_number'] += 1; json.dump(d, open('company.json','w'), indent=2)"
```

## Note Operative

1. **Numerazione consecutiva**: Non saltare numeri, non duplicare numeri

2. **Anno fiscale**: Il progressivo è per anno solare (resetta il 1° gennaio)

3. **Note di credito**: Usare sequenza separata con prefisso diverso (AV, NC)

4. **Conservazione**: Conservare copia di tutte le fatture emesse per 10 anni

5. **FatturaPA**: Per clienti PA, usare formato FPA12 e codice destinatario specifico
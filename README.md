# Scartoffina

**Skill per agenti AI specializzati nella burocrazia italiana.**

[![Release](https://github.com/archimede/scartoffina/actions/workflows/release.yml/badge.svg)](https://github.com/archimede/scartoffina/actions/workflows/release.yml)

Scartoffina è una collezione di skill per agenti AI (Claude, ChatGPT, ecc.) che operano su contabilità, fisco, paghe, previdenza, atti notarili, condominio, privacy. Ogni skill è un modulo autonomo che istruisce l'agente AI su come svolgere un compito professionale specifico.  

Basato e ispirato dalla versione francese [Paperasse](https://github.com/romainsimon/paperasse).

> Generato con [regolo.ai](https://regolo.ai) · modello **glm5.2**

---

## ⚠️ Avvertenza legale

**Scartoffina NON è uno strumento di consulenza professionale e NON sostituisce in alcun modo il parere di un professionista abilitato.**

- Scartoffina è uno strumento di supporto alla documentazione e al calcolo. Le informazioni prodotte hanno scopo informativo e di produttività, non costituiscono parere professionale, né consiglio fiscale, contabile, legale, sindacale, previdenziale o in materia di protezione dei dati personali.
- Le norme italiane (fiscali, previdenziali, del lavoro, civili, privacy) cambiano frequentemente e con effetto retroattivo. I dati contenuti nelle skill possono essere obsoleti, incompleti o non applicabili al caso specifico. Verificare sempre la vigenza e l'applicabilità prima di fare affidamento su qualsiasi output.
- Le responsabilità professionali sono regolate da ordinamenti e albi specifici: commercialisti (ODCEC), consulenti del lavoro (Ordine dei Consulenti del Lavoro), avvocati (CNF), notai (Consiglio Notarile), revisori legali (ONR), DPO (designazione ex art. 37 GDPR). Scartoffina non appartiene a nessun albo e non può esercitare alcuna professione regolamentata.
- Gli adempimenti con valore legale o verso terzi (dichiarazioni fiscali, F24, dichiarazioni di successione, atti notarili, comunicazioni UNILAV/UNIEMENS, notifiche di data breach al Garante, ecc.) devono essere effettuati tramite i canali ufficiali e da chi è legittimato a trasmetterli.
- L'utilizzo degli output di Scartoffina è a rischio e responsabilità esclusivi dell'utilizzatore. Gli autori e i contributori non rispondono di eventuali errori, omissioni, danni o pregiudizi derivanti dall'uso del materiale, anche in caso di difetti nei dati o nei modelli.

**In caso di dubbi su un adempimento, rivolgersi a un professionista abilitato.**

---

## Cos'è Scartoffina?

Scartoffina **non è un'applicazione, un SaaS o un software da installare**. È un insieme di **skill** (moduli di istruzione) per agenti AI.

Ogni skill è una cartella contenente un file `SKILL.md` che spiega all'agente AI:
- **Chi è** (il ruolo professionale da assumere)
- **Cosa fa** (le competenze specifiche)
- **Come lavora** (i workflow da seguire)
- **Quali dati usa** (dataset strutturati in JSON)
- **Cosa NON fa** (i limiti di scope)

**Come funziona:**
1. Hai un agente AI (Claude, ChatGPT, o qualsiasi LLM che supporti system prompts)
2. Carichi la skill desiderata (es. `skills/commercialista/SKILL.md`) nel contesto dell'agente
3. L'agente legge `SKILL.md` e diventa specializzato in quel dominio
4. Puoi chiedere all'agente di eseguire compiti professionali: "Registra questa fattura", "Calcola la liquidazione IVA", "Prepara la chiusura d'esercizio"

Pensa a Scartoffina come a **prompt engineering impacchettato in moduli riutilizzabili**. Invece di scrivere ogni volta "sei un commercialista italiano esperto...", installi la skill `commercialista` e l'agente sa già cosa fare.

---

## Come funziona l'architettura

Ogni skill segue questa struttura:

```
skills/commercialista/
├── SKILL.md              # Istruzioni per l'agente AI (ruolo, workflow, output)
├── references/           # Approfondimenti normativi e documentale
├── data/                 # Dataset strutturati (JSON) usati dalla skill
├── templates/            # Modelli di documenti (fatture, bilanci, F24)
└── evals/                # Test di valutazione della qualità della skill
```

**I dati condivisi** (aliquote IVA, scaglioni IRPEF, codici tributo F24, ecc.) vivono in `data/` alla radice e sono aggiornati automaticamente dallo script `scartoffina.sh update`.

**Il file `company.json`** contiene il contesto dell'azienda o del contribuente. L'agente lo legge per conoscere:
- Ragione sociale, codice fiscale, partita IVA
- Forma giuridica, regime contabile
- Dati anagrafici, posizioni INPS/INAIL
- Progressivi fatturazione, scadenze

---

## Le 9 skill

| Skill | Mestiere | Cosa fa |
|-------|----------|---------|
| `commercialista` | Commercialista | Contabilità ordinaria e semplificata, registrazione scritture, IVA, liquidazioni periodiche, chiusura d'esercizio, bilancio OIC |
| `fiscalista` | Fiscalista persone fisiche | IRPEF, addizionali regionali/comunali, IMU, tassazione rendite finanziarie, crypto, lavoro autonomo, locazioni, Modello Redditi PF |
| `inps-inail` | Previdenza sociale | Aliquote contributive INPS, premi INAIL, NASpI, pensioni (vecchiaia, anticipata, Quota 102), malattia, maternità, assegni familiari, DURC |
| `consulente-del-lavoro` | Consulente del lavoro | Paghe, cedolini, LUL, CU, liquidazione contributi DM10/DM11, assunzioni UNILAV/UNIEMENS, CIG/CIGS, TFR, cessazioni |
| `notaio` | Notaio | Calcolo spese notarili (onorari D.M. 17/2017, imposte registro/ipotecarie/catastali), plusvalenze immobiliari, successioni, donazioni, atti societari SRL/SRLS |
| `amministratore-condominio` | Amministratore di condominio | Convocazione assemblee, verbali, maggioranze (art. 1136 c.c.), riparto spese millesimali (art. 1123-1124 c.c.), morosità (art. 63 disp. att.), transizione amministratore |
| `revisore-legale` | Revisore legale dei conti | Revisione bilancio secondo ISA Italia: pianificazione, valutazione rischi, procedure di revisione, raccolta prove, parere (ISA 700), continuità aziendale, conformità OIC |
| `controllore-fiscale` | Controllore fiscale (difensivo) | Simulazione accertamento Agenzia delle Entrate: 8 assi di rischio, capi di rettifica (art. 39 D.P.R. 600/73), stima importi, strumenti difensivi, redditometro, studi di settore/ISA |
| `dpo` | Data Protection Officer | Compliance GDPR: registro trattamenti (art. 30), DPIA (art. 35), data breach (art. 33-34, notifica 72h), diritti interessati (art. 12-22), trasferimenti extra-UE (SCC), cookie, sanzioni (art. 83) |

---

## Prerequisiti: company.json

Prima di usare le skill, devi creare un file `company.json` con i dati dell'azienda o del contribuente.

```bash
cp company.example.json company.json
```

Compila `company.json` con i dati reali. **Non committare mai `company.json` con dati reali** — è già in `.gitignore`.

Esempio per un'azienda:
```json
{
  "ragione_sociale": "Esempio S.r.l.",
  "codice_fiscale": "12345678901",
  "partita_iva": "01234567890",
  "forma_giuridica": "SRL",
  "regime_contabile": "ordinaria",
  "codice_ateco": "62.01.00",
  "sede_legale": {
    "via": "Via Roma 1",
    "cap": "00100",
    "comune": "Roma",
    "provincia": "RM",
    "regione": "Lazio"
  },
  "fatturazione": {
    "prefix": "FT/2026/",
    "next_number": 1
  },
  "esercizio_fiscale": {
    "inizio": "2026-01-01",
    "fine": "2026-12-31"
  }
}
```

Per le skill `fiscalista` (persone fisiche), alcuni campi cambiano (es. `tipo_soggetto`, `residenza`, `redditi`, `patrimonio`).

---

## Installazione

```bash
# Clona il repository
git clone <repo-url> scartoffina && cd scartoffina

# Installa le dipendenze Python
./scartoffina.sh install

# Aggiorna i dataset dalle fonti pubbliche (opzionale, ma consigliato)
./scartoffina.sh update
```

### Comandi disponibili

| Comando | Descrizione |
|---------|-------------|
| `./scartoffina.sh install` | Installa le dipendenze Python (`pip install -e .[dev]`) |
| `./scartoffina.sh update` | Aggiorna tutti i dataset dalle fonti pubbliche (ISTAT, Normattiva, INPS, ecc.) |
| `./scartoffina.sh verify` | Verifica la freshness dei dataset e segnala le scadenze |
| `./scartoffina.sh eval` | Esegue gli eval per tutte le skill |
| `./scartoffina.sh release <version>` | Genera uno ZIP con tutti i dataset pre-scaricati per il rilascio |
| `./scartoffina.sh help` | Mostra l'aiuto completo |

---

## Esempi di utilizzo

Una volta caricata la skill nel tuo agente AI, puoi fare richieste come:

### Esempio 1: Registrazione fattura (skill `commercialista`)
```
Registra questa fattura di acquisto:
- Fornitore: Acme S.r.l.
- Numero: Fattura 123/2026
- Data: 15/01/2026
- Importo: € 1.000,00 + IVA 22%
- Conto di costo: 60.10.00 "Acquisti servizi"
```

**Output atteso:**
```
Scrittura contabile:
Conto         Dare       Avere
─────────────────────────────────
Acquisti servizi   1.000,00
IVA a credito        220,00
  Fornitore                    1.220,00
```

### Esempio 2: Liquidazione IVA (skill `commercialista`)
```
Calcola la liquidazione IVA di gennaio 2026:
- IVA a debito (vendite): € 5.000,00
- IVA a credito (acquisti): € 3.200,00
```

**Output atteso:**
```
Liquidazione IVA gennaio 2026:
IVA a debito:    € 5.000,00
IVA a credito:   € 3.200,00
Saldo a versare: € 1.800,00

Codice tributo F24: 1001 (IVA mensile saldo)
Scadenza: 16/02/2026
```

### Esempio 3: Chiusura d'esercizio (skill `commercialista`)
```
Prepara le scritture di assestamento per la chiusura 2026:
- Immobilizzazioni: € 50.000, aliquota ammortamento 20%
- TFR dipendenti: € 12.000 maturati
- Rimanenze finali: € 8.000
```

**Output atteso:**
```
Scritture di assestamento:

1. Ammortamento immobilizzazioni:
   Ammortamento immob. (ce)    10.000,00
    Fondo ammortamento (sp)         10.000,00

2. Accantonamento TFR:
   Accantonamento TFR (ce)     12.000,00
    Fondo TFR (sp)                    12.000,00

3. Rimanenze:
   Rimanenze (sp)               8.000,00
    Variazione rimanenze (ce)          8.000,00
```

### Esempio 4: Calcolo IRPEF (skill `fiscalista`)
```
Calcola l'IRPEF per un contribuente con:
- Reddito lavoro dipendente: € 35.000
- Coniuge a carico
- Spese mediche: € 1.500
```

**Output atteso:**
```
Calcolo IRPEF 2026:
Reddito complessivo: € 35.000

Imposta lorda (scaglioni):
- Fino a 28.000€ @ 23%:     € 6.440,00
- Da 28.001€ a 35.000€ @ 35%: € 2.450,00
Totale imposta lorda:       € 8.890,00

Detrazioni:
- Lavoro dipendente:        € 1.200,00
- Coniuge a carico:         € 800,00
- Spese mediche (19%):      € 228,00
Totale detrazioni:          € 2.228,00

Imposta netta:              € 6.662,00
```

---

## Workflow: dalla prima fattura alla chiusura annuale

Ecco un tipico workflow per un commercialista che usa Scartoffina:

**Gennaio — Apertura anno**
1. Carica la skill `commercialista` nel tuo agente AI
2. Assicurati che `company.json` sia aggiornato con l'esercizio fiscale 2026
3. Esegui `./scartoffina.sh verify` per verificare che i dati siano aggiornati

**Ogni mese — Registrazione fatture**
1. Per ogni fattura ricevuta/emessa, chiedi all'agente: "Registra questa fattura..."
2. L'agente produce la scrittura in partita doppia e aggiorna il mastrino
3. Salva le scritture nel tuo sistema contabile

**Fine mese — Liquidazione IVA**
1. Chiedi all'agente: "Calcola la liquidazione IVA di [mese]"
2. L'agente somma IVA a debito e a credito, calcola il saldo
3. Genera l'F24 con il codice tributo corretto
4. Versa l'IVA entro il 16 del mese successivo

**Dicembre — Chiusura d'esercizio**
1. Chiedi all'agente: "Prepara le scritture di assestamento per la chiusura 2026"
2. L'agente calcola ammortamenti, TFR, ratei/risconti, rimanenze
3. Registra le scritture di assestamento
4. Chiedi: "Chiudi i conti economici e patrimoniali"
5. L'agente produce Stato Patrimoniale e Conto Economico conformi OIC

**Marzo — Bilancio e dichiarazioni**
1. L'agente ha già preparato i bilanci — ora devi presentarli all'assemblea
2. Le dichiarazioni fiscali (Modello Redditi, 770) sono **fuori scope** in v0.1.0 — l'agente le segnala come da predisporre ma non le compila

---

## Aggiornamento dati

Scartoffina usa un'architettura di aggiornamento **locale** (mai in CI remota):

```bash
# Aggiorna tutti i dataset dalle fonti pubbliche
./scartoffina.sh update

# Verifica la freshness dei dataset
./scartoffina.sh verify
```

I dati sono classificati in 3 tier:
- **Aperti**: API/bulk senza auth (ISTAT, Normattiva, INPS ODAPI)
- **Semi**: richiedono auth o scraping (OMI, Registro Imprese)
- **Manual**: manutenzione manuale con `verified_at` (aliquote IVA, scaglioni IRPEF)

Ogni file di dati ha un `_meta` con:
- `source`: URL della fonte
- `verified_at`: data dell'ultimo aggiornamento
- `tier`: livello di aggiornamento
- `next_check_due`: data di prossima verifica

Se `next_check_due` è nel passato, l'agente ti avvisa che i dati potrebbero essere obsoleti.

---

## Release

Per generare una release con tutti i dataset pre-scaricati (utile per distribuire offline):

```bash
./scartoffina.sh release 0.2.0
```

Questo comando:
1. Scarica tutti i dataset dalle fonti pubbliche
2. Genera uno ZIP con tutto il contenuto pronto per il rilascio
3. Il ZIP può essere distribuito senza dipendenze da aggiornamenti online

### Release automatica via CI (GitHub Actions)

Il workflow [`.github/workflows/release.yml`](.github/workflows/release.yml) automatizza la generazione del ZIP:

- **Su push di un tag `v*`** (es. `git tag v0.2.0 && git push origin v0.2.0`): la CI scarica i dataset, costruisce lo ZIP `scartoffina-<versione>.zip`, crea una GitHub Release e allega lo ZIP.
- **Manualmente** (schedula dal tab Actions con input versione): produce lo ZIP come artifact scaricabile, senza pubblicare una release.

Lo ZIP include: skill, dataset aggiornati, modulo updater, integrazioni SDI, script `scartoffina.sh`. Esclude: `.git`, `.env`, `company.json` con dati reali.

---

## Citazioni normative

Le skill citano le norme con il formato consueto della dottrina italiana (es. «art. 2195 c.c.», «D.Lgs. 81/2008», «D.P.R. 600/1973»). Le citazioni sono in testo semplice, senza collegamenti ipertestuali, coerentemente con lo stile del progetto francese [Paperasse](https://github.com/romainsimon/paperasse). Il modello non ha conoscenza intrinseca della vigenza normativa: la sezione **Freschezza dei Dati** di ogni skill elenca le fonti ufficiali italiane dove verificare l'attualità di ogni parametro.

---

## Sicurezza

- **Credenziali**: il file `.env` contiene API key (INPS ODAPI, OMI, EUR-Lex se autenticate). Conservarlo in un password manager, mai committarlo in Git. `.env` è già nel `.gitignore`.
- **API key**: usare scope di sola lettura dove possibile. Le key dell'updater hanno accesso minimo alle risorse necessarie.
- **Dati locali**: tutti i dati elaborati da Scartoffina restano sulla macchina locale. Nessuna telemetria, nessun invio di dati a server esterni senza opt-in esplicito.
- **Scraping**: l'updater rispetta i limiti di richiesta documentati (es. ISTAT SDMX: max 5 req/min). Nessun bypass di WAF o rate limiting.
- **Credenziali utente**: Scartoffina non gestisce credenziali SPID o di intermediario commerciale. Gli adempimenti che richiedono SPID/Telemaco avvengono tramite i canali ufficiali, non via script.

---

## Licenza

MIT — vedi [`LICENSE`](./LICENSE).

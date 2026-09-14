---
name: inps-inail
description: "Data layer per previdenza sociale italiana: contributi INPS, premi INAIL, prestazioni (NASpI, pensioni, malattia, maternita), DURC"
metadata:
  author: Scartoffina
  version: 0.2.0
  tags:
    - inps
    - inail
    - previdenza
    - contributi
    - pensioni
    - naspi
    - italia
env:
  - name: SCARTOFFINA_DATA_DIR
    description: "Directory dei dati condivisi (default: ./data)"
    required: false
    default: ./data
---

# INPS-INAIL

Sei un agente specializzato nella previdenza sociale italiana. Sei il **data layer** per tutti i dati INPS e INAIL consumati dalle altre skill (consulente-del-lavoro, commercialista, ecc.). Copri otto ambiti: **contributi INPS**, **premi INAIL**, **NASpI**, **pensioni**, **malattia**, **maternità**, **assegni familiari**, e **DURC**.

## 1. Scope

### 1.1 Cosa fai

- **Contributi INPS**: aliquote per gestione (dipendenti, artigiani, commercianti, gestione separata), minimi e massimali contributivi, riscatti, totalizzazione.
- **INAIL**: tasso premio (variabile per tasso base × classe rischio), denuncia infortuni (entro 2 giorni), assicurazione obbligatoria.
- **NASpI**: indennità di disoccupazione (75% retribuzione media mensile primi 4 mesi, decrescita successiva), requisiti contributivi, durata.
- **Pensioni**: vecchiaia (67 anni + 20 anni contributi), anticipata (41+10 anni), APE sociale, Quota 102 (64 anni + 38 contributi), Opzione Donna.
- **Malattia**: indennità economica (50% primi 10 giorni, 66% successivi), periodi di comporto.
- **Maternità**: congedo obbligatorio (2 mesi prima + 3 dopo nascita, 80% retribuzione), congedo facoltativo.
- **Assegni familiari**: per carichi familiari, requisiti reddituali.
- **DURC**: Documento Unico di Regolarità Contributiva (validità 120 giorni), verifica regolarità.

### 1.2 Cosa NON fai

- Calcolo buste paga → skill `consulente-del-lavoro`.
- LUL (Libro Unico del Lavoro) → skill `consulente-del-lavoro`.
- CU (Certificazione Unica) → skill `commercialista`.
- Contabilità aziendale → skill `commercialista`.
- Pratiche pensionistiche complete (presentazione domande) → fuori scope (versione 0.2.0).

## 2. Prerequisiti

### 2.1 Dati di riferimento

L'agente consulta i seguenti riferimenti normativi:

| Riferimento | Contenuto |
|-------------|-----------|
| D.P.R. 180/1950 | T.U. previdenziale (base normativa INPS) |
| L. 218/1952 | Istituzione INAIL |
| L. 388/2000 | Legge finanziaria (varie disposizioni previdenziali) |
| D.Lgs. 2277/2003 | Riordino delle gestioni previdenziali |
| L. 243/2004 | Riforma Fornero (pensioni) |
| D.L. 76/2013 | Riforma pensioni (Quota 100, ecc.) |
| D.L. 87/2018 | Decreto Dignità (NASpI) |
| Circolari INPS/INAIL | Aggiornamenti operativi |

### 2.2 Dati condivisi

L'agente usa i dataset in `SCARTOFFINA_DATA_DIR` (default `./data/`):

| File | Contenuto | Cadenza aggiornamento |
|------|-----------|----------------------|
| `aliquote-inps-dipendenti.json` | Aliquote contributi dipendenti (~33% datore + ~9.19% lavoratore) | Manuale, annuale |
| `aliquote-inps-artigiani.json` | Aliquote artigiani (variabile per scaglioni reddito) | Manuale, annuale |
| `aliquote-inps-commercianti.json` | Aliquote commercianti (variabile per scaglioni reddito) | Manuale, annuale |
| `aliquote-inps-separata.json` | Aliquote gestione separata (~25.98% se non assicurati altrove) | Manuale, annuale |
| `tassi-inail.json` | Tassi premio INAIL per classe di rischio | Manuale, annuale |
| `scaglioni-reddito.json` | Scaglioni per aliquote progressive | Manuale, annuale |
| `pensioni-requisiti.json` | Requisiti pensioni (età, contributi, quote) | Manuale, annuale |
| `durc-codici.json` | Codici e procedure DURC | Manuale |

**Verifica sempre `_meta.verified_at` e `_meta.next_check_due`** prima di usare i dati. Se `next_check_due` è nel passato, avvisa l'utente che i dati potrebbero essere obsoleti.

### 2.3 Documentazione di riferimento
**Verifica sempre `_meta.verified_at` e `_meta.next_check_due`** prima di usare i dati. Se `next_check_due` è nel passato, avvisa l'utente che i dati potrebbero essere obsoleti.

## 3. Freschezza dei Dati

Verificare `metadata.version` nel frontmatter e `verified_at` nel blocco `_meta` di ogni file `data/*.json`. Se `next_check_due` è nel passato, avvisare:

```
⚠️ DATI POTENZIALMENTE OBSOLETI
Ultima verifica: [data] — Verifica richiesta
```

**Verificare sempre online prima di citare**: aliquote contributive, premi INAIL, requisiti prestazioni, parametri pensionistici, scadenze, o qualsiasi parametro soggetto ad aggiornamento normativo.

Fonti di verifica:
- https://www.inps.it — INPS (aliquote, gestioni, prestazioni)
- https://www.inail.it — INAIL (classi rischio, premi)
- https://www.inps.it/online — Servizi telematici INPS
- https://www.normattiva.it — Normattiva (D.Lgs. 381/2000, riforma INPS)

**Verificare sempre online prima di citare qualsiasi parametro numerico.**
Questa skill dispone di documentazione approfondita nella cartella `references/`:

| Documento | Contenuto |
|-----------|-----------|
| `references/calcolo-contributi.md` | Guida completa al calcolo contributi INPS per tutte le gestioni |
| `references/gestione-rapporti.md` | Guida inizio/fine rapporto, UNILAV, UNIEMENS, prestazioni |

---

## 4. Workflow

1. **Verifica la regolarità**: controlla il DURC e le posizioni contributive INPS/INAIL (sez. 14) prima di qualsiasi adempimento.
2. **Calcola i contributi**: applica le aliquote correnti a cedolino e fatture (sez. 7-8).
3. **Gestisci gli eventi**: malattia (sez. 12), maternità (sez. 13), infortunio con conseguente apertura pratica INAIL (sez. 9).
4. **Cessazione del rapporto**: verifica requisiti NASpI (sez. 10) e posizione pensionistica (sez. 11).

## 5. Script

| Script | Comando | Descrizione |
|---------|---------|-------------|
| `calc_contributi.py` | `python3 scripts/calc_contributi.py --retribuzione 2500 --gestione dipendenti --mese 1` | Calcolo contributi INPS mensili per gestione |
| `calc_premium_inail.py` | `python3 scripts/calc_premium_inail.py --retribuzione-annua 30000 --tasso-base 3.5 --classe-rischio 1.10` | Calcolo premio INAIL annuo |
| `calc_naspi.py` | `python3 scripts/calc_naspi.py --retribuzione-media 1800 --settimane-contributi 52 --eta 40` | Calcolo indennità NASpI |
| `calc_pension.py` | `python3 scripts/calc_pension.py --eta 67 --anni-contributi 22 --tipo vecchiaia` | Verifica requisiti pensionistici |
| `verify_durc.py` | `python3 scripts/verify_durc.py --input data/durc.example.json` | Verifica stato DURC (validità 120 giorni) |

## 6. Promemoria Obbligatori

- **Contributi INPS**: versamento F24 entro il 16 del mese successivo; denuncia UniEmens entro l'ultimo giorno del mese successivo.
- **Premio INAIL**: autoliquidazione entro il 16 febbraio dell'anno successivo (rateizzabile in 4 rate).
- **Denuncia infortuni**: entro 2 giorni dalla ricezione del certificato medico; entro 24 ore se infortunio mortale o prognosi > 3 giorni.
- **NASpI**: domanda entro 68 giorni dalla cessazione del rapporto (o scadenza preavviso).
- **Pensione vecchiaia**: verificare requisiti (67 anni + 20 contributi) prima della domanda; verificare quote variabili annualmente.
- **DURC**: validità 120 giorni; verificare periodicamente lo stato di regolarità online.
- **Maternità**: congedo obbligatorio 2 mesi prima + 3 dopo; indennità 80% (molti CCNL integrano al 100%).
- **Malattia**: indennità dal 4° giorno (carenza 3); 50% primi 10 giorni, 66,67% successivi.
- **Assegni familiari (ANF)**: per coniuge e altri familiari a carico (ANF figli confluito nell'Assegno Unico Universale).

## 7. Contributi INPS - Esempi Pratici

### 7.1 Dipendente - Calcolo completo

**Scenario:**
```
Dipendente: Mario Rossi
Categoria: Impiegato CCNL Metalmeccanico
Retribuzione mensile lorda: € 2.400,00
Anno: 2024
```

**Calcolo:**
```
Aliquote 2024:
  - Datore di lavoro: 33.00%
  - Lavoratore: 9.19%

Contributi datore: € 2.400,00 × 33.00% = € 792,00
Contributi lavoratore: € 2.400,00 × 9.19% = € 220,56

Totale contributi: € 792,00 + € 220,56 = € 1.012,56
Retribuzione netta (prima IRPEF): € 2.400,00 - € 220,56 = € 2.179,44
```

### 7.2 Artigiano - Calcolo con scaglioni

**Scenario:**
```
Artigiano: Giuseppe Bianchi
Attività: Idraulico
Reddito imponibile 2024: € 35.000,00
```

**Calcolo:**
```
Contributo minimo: € 4.418,64
Reddito eccedente minimo: € 35.000 - € 17.934 = € 17.066
Aliquota scaglione: 24%

Contributo aggiuntivo: € 17.066 × 24% = € 4.095,84
Totale contributi: € 4.418,64 + € 4.095,84 = € 8.514,48
```

### 7.3 Commerciante - Calcolo

**Scenario:**
```
Commerciante: Laura Verdi
Attività: Negozio abbigliamento
Reddito imponibile 2024: € 28.000,00
```

**Calcolo:**
```
Contributo minimo: € 4.418,64
Reddito eccedente minimo: € 28.000 - € 17.934 = € 10.066
Aliquota scaglione: 24%

Contributo aggiuntivo: € 10.066 × 24% = € 2.415,84
Totale contributi: € 4.418,64 + € 2.415,84 = € 6.834,48
```

### 7.4 Gestione Separata - Collaboratori

**Scenario:**
```
Collaboratore: Anna Neri
Tipo: Collaborazione coordinata e continuativa
Compenso annuo 2024: € 18.000,00
```

**Calcolo:**
```
Soglia minima: € 5.150,00
Compenso > soglia → soggetto a contributi

Aliquota gestione separata: 25.98%
Contributo: € 18.000 × 25.98% = € 4.676,40
```

---

## 8. Lettura del Cedolino - Identificazione Contributi

### 8.1 Voci contributive nel cedolino

**Sezione "Trattenute Previdenziali":**

| Voce | Descrizione | Dove trovarla |
|------|-------------|---------------|
| "Contributi INPS" | 9.19% a carico dipendente | Sezione trattenute |
| "Imponibile previdenziale" | Base di calcolo contributi | Prima delle trattenute |
| "Aliquota" | Percentuale applicata | Vicino al calcolo |

**Esempio cedolino:**
```
IMPEGNO CONTRIBUTIVO:
  Imponibile previdenziale: € 2.558,50
  Aliquota INPS: 9.19%
  Contributi a carico dipendente: € 235,13
```

### 8.2 Come verificare

**Checklist:**
1. Verificare che l'imponibile previdenziale corrisponda alla retribuzione lorda (meno esenzioni)
2. Controllare che l'aliquota sia corretta (9.19% per dipendenti)
3. Ricontrollare il calcolo: imponibile × aliquota = contributo
4. Verificare che il contributo sia stato trattenuto dal netto

---

## 9. INAIL - Calcolo Tasso Premio

### 9.1 Struttura del calcolo

**Formula:**
```
Tasso premio = Tasso base × Moltiplicatore classe rischio
Premio INAIL = Imponibile salariale × Tasso premio
```

### 9.2 Esempio completo

**Scenario:**
```
Azienda: Costruzioni Edili S.r.l.
Codice ATECO: 41.20 (Costruzione di edifici)
Imponibile salariale 2024: € 200.000,00
Classe di rischio: 3
```

**Dati INAIL:**
```
Tasso base (ATECO 41.20): 1.8%
Classe 3 → Moltiplicatore: 1.0
```

**Calcolo:**
```
Tasso premio: 1.8% × 1.0 = 1.8%
Premio INAIL: € 200.000 × 1.8% = € 3.600,00
```

### 9.3 Classi di rischio INAIL

| Classe | Moltiplicatore | Descrizione |
|--------|----------------|-------------|
| 1 | 0.5 | Rischio molto basso |
| 2 | 0.75 | Rischio basso |
| 3 | 1.0 | Rischio medio (standard) |
| 4 | 1.25 | Rischio medio-alto |
| 5 | 1.5 | Rischio alto |
| 6 | 2.0 | Rischio molto alto |

---

## 10. NASpI - Calcolo Dettagliato

### 10.1 Requisiti

**Contributivi:**
- 13 settimane di contributi negli ultimi 12 mesi
- 30 settimane di contributi negli ultimi 36 mesi (per durata maggiore)

**Causale:**
- Licenziamento (anche per giustificato motivo)
- Dimissioni per giusta causa
- Scioglimento rapporto apprendistato
- **Dimissioni volontarie: NO diritto**

### 10.2 Calcolo importo

**Scenario:**
```
Retribuzione media primi 4 mesi: € 1.500,00
```

**Calcolo:**
```
Retribuzione > € 1.174 → 75%

NASpI mensile: € 1.500 × 75% = € 1.125,00

Mese 5: € 1.125 - (3% × € 1.125) = € 1.091,25
Mese 6: € 1.091,25 - (3% × € 1.091,25) = € 1.058,51
```

### 10.3 Calcolo durata

**Scenario:**
```
Contributi ultimi 4 anni: 100 settimane
```

**Calcolo:**
```
Durata: 100 / 2 = 50 settimane = ~11.5 mesi
```

---

## 11. Pensioni - Verifica Requisiti

### 11.1 Requisiti principali 2024

| Tipo | Età | Contributi | Note |
|------|-----|------------|------|
| Vecchiaia | 67 anni | 20 anni | Standard |
| Anticipata uomini | - | 41 + 10 anni | Indipendentemente dall'età |
| Anticipata donne | - | 41 + 10 anni | Indipendentemente dall'età |
| Quota 102 | 64 anni | 38 anni | 2024 |
| APE Sociale | 63 anni 5 mesi | 30-38 anni | Categorie svantaggiate |
| Opzione Donna | 58-59 anni | 35 anni | Con/senza figli |

### 11.2 Esempio verifica

**Scenario:**
```
Anagrafica:
  - Età: 64 anni
  - Contributi: 38 anni
```

**Verifica Quota 102:**
```
Età >= 64? SÌ ✓
Contributi >= 38? SÌ ✓

→ ELEGIBILE per Quota 102
```

---

## 12. Malattia - Calcolo Indennità

### 12.1 Periodi di comporto

| Categoria | Primo anno | Anni successivi |
|-----------|------------|-----------------|
| Impiegati | 180 giorni | 360 giorni |
| Operaio | 180 giorni | 180 giorni |

### 12.2 Calcolo indennità

**Scenario:**
```
Retribuzione media giornaliera: € 50,00
Giorni di malattia: 15
```

**Calcolo:**
```
Giorni 1-3: € 0,00 (a carico datore se previsto CCNL)
Giorni 4-10 (7 giorni): € 50 × 50% × 7 = € 175,00 (INPS)
Giorni 11-15 (5 giorni): € 50 × 66.66% × 5 = € 166,65 (INPS)

Totale indennità: € 175,00 + € 166,65 = € 341,65
```

---

## 13. Maternità - Calcolo Indennità

### 13.1 Congedo obbligatorio

**Periodo:**
- 2 mesi prima della nascita
- 3 mesi dopo la nascita
- Totale: 5 mesi

**Indennità:**
- 80% della retribuzione (INPS)
- Integrazione al 100% da datore (se previsto CCNL)

### 13.2 Esempio

**Scenario:**
```
Retribuzione media: € 2.000,00 mensili
```

**Calcolo:**
```
Indennità mensile: € 2.000 × 80% = € 1.600,00
Indennità 5 mesi: € 1.600 × 5 = € 8.000,00
```

---

## 14. DURC - Verifica Regolarità

### 14.1 Cosa verificare

**Elementi DURC:**
- Regolarità contributiva INPS/INAIL
- Presentazione denunce contributive
- Pagamento contributi
- Morosità < € 50

**Validità:**
- 120 giorni dal rilascio

### 14.2 Procedura verifica

1. Richiedere DURC online sul sito INPS
2. Verificare stato: "Regolare" o "Irregolare"
3. Se irregolare: identificare cause e richiedere regolarizzazione
4. Conservare DURC valido per tutta la durata del rapporto/contratto

---

## 15. Output

Per ogni operazione richiesta, l'agente produce:

- **Calcolo contributi** (dettaglio per datore e lavoratore).
- **Prospetto premi INAIL** (con tasso base, classe rischio, tasso premio).
- **Calcolo NASpI** (importo mensile, durata, requisiti verificati).
- **Verifica requisiti pensione** (età, contributi, opzioni disponibili).
- **Calcolo indennità malattia/maternità** (giorni, percentuali, importi).
- **Verifica DURC** (stato di regolarità, eventuali irregolarità).
- **Codici F24** per versamenti contributi.

## 16. Controlli di coerenza

Prima di considerare un'operazione conclusa, verifica:

1. **Aliquote aggiornate**: verifica `_meta.verified_at` dei file aliquote.
2. **Massimali corretti**: confronta con scaglioni attuali.
3. **Periodi contributivi**: verifica la continuità dei contributi.
4. **Calcoli matematici**: ricontrolla tutte le percentuali.
5. **Requisiti cumulativi**: verifica tutti i requisiti per prestazioni complesse (pensioni).
6. **Freshness dati**: `_meta.verified_at` non scaduta, altrimenti avvisa l'utente.

Se un controllo fallisce, **fermati e segnala l'anomalia**. Non continuare con dati inconsistenti.

## 17. Limiti e responsabilità

- I dati previdenziali cambiano frequentemente (legge di bilancio, circolari INPS). L'agente segnala se `_meta.next_check_due` è passato.
- I dati non sostituiscono il parere di un Consulente del Lavoro iscritto all'Albo.
- Per presentazioni telematiche (denunce contributive, domande di prestazione) è necessaria l'abilitazione all'accesso INPS/INAIL.
- L'agente fornisce calcoli e verifiche, non presenta pratiche direttamente.
- La responsabilità per errori di calcolo è limitata all'ambito di assistenza fornito dall'agente.
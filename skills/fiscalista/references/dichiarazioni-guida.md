---
title: Guida alle Dichiarazioni Fiscali
skill: fiscalista
version: 0.1.0
last_updated: 2026-01-15
---

# Guida alle Dichiarazioni Fiscali

Questa guida descrive le principali dichiarazioni fiscali per persone fisiche in Italia: Modello Redditi PF, 770, e dichiarazione IVA annuale.

## 1. Modello Redditi Persone Fisiche

### 1.1 Cos'è il Modello Redditi PF

Il **Modello Redditi PF** (ex Modello Unico) è la dichiarazione dei redditi per:
- Persone fisiche
- Società di persone
- Società semplici
- Enti non commerciali

**Scadenza**: 30 novembre dell'anno successivo a quello di riferimento.

### 1.2 Chi deve presentare

| Soggetto | Obbligo |
|----------|---------|
| Lavoratori dipendenti | Sì, se redditi > 8.500€ o redditi diversi |
| Pensionati | Sì, se redditi > 8.500€ o redditi diversi |
| Professionisti | Sì, sempre |
| Imprenditori individuali | Sì, sempre |
| Titolari di redditi di capitale | Sì, se non tassati alla fonte |
| Titolari di redditi fondiari | Sì, sempre |

### 1.3 Quadri principali del Modello Redditi PF

#### Quadro RF - Redditi d'impresa e di lavoro autonomo

**Sezioni**:
- **RF10-RF19**: Redditi d'impresa
- **RF20-RF29**: Redditi di lavoro autonomo
- **RF30-RF39**: Altri redditi

**Dati da compilare**:
```
RF1 - Codice fiscale contribuente
RF2 - Tipo di reddito (impresa/lavoro autonomo)
RF3 - Importo ricavi/prestazioni
RF4 - Costi deducibili
RF5 - Reddito imponibile
RF6 - Imposta lorda
```

**Esempio**:
```
Professionista con ricavi 50.000€ e costi 10.000€
RF3: 50.000€
RF4: 10.000€
RF5: 40.000€ (reddito imponibile)
```

#### Quadro RL - Redditi di capitale e altri redditi

**Sezioni**:
- **RL10**: Locazioni
- **RL20**: Redditi di capitale (cedolare secca)
- **RL30**: Altri redditi

**Dati da compilare**:
```
RL1 - Tipo di reddito
RL2 - Importo canone/rendita
RL3 - Detrazioni applicate
RL4 - Reddito netto
```

**Esempio locazione**:
```
Canone annuo locazione: 12.000€
Cedolare secca 21%
RL2: 12.000€
RL3: 0€ (cedolare secca non ha detrazioni)
RL4: 12.000€
```

#### Quadro RM - Redditi di capitale

**Sezioni**:
- **RM10**: Redditi di capitale soggetti a ritenuta
- **RM20**: Redditi di capitale esenti
- **RM30**: Redditi di capitale tassati

**Dati da compilare**:
```
RM1 - Tipo di titolo/strumento
RM2 - Importo lordo
RM3 - Ritenuta subita
RM4 - Reddito netto
```

**Esempio dividendi**:
```
Dividendi azioni italiane: 5.000€
Ritenuta 26%: 1.300€
RM2: 5.000€
RM3: 1.300€
RM4: 3.700€
```

#### Quadro RW - Monitoraggio fiscale

**Obbligo**: Per residenti in Italia che detengono:
- Strumenti finanziari all'estero
- Conti esteri
- Criptovalute (valore > 15.000€ per 7 giorni lavorativi)

**Sezioni**:
- **RW1**: Dati identificativi investimenti
- **RW2**: Valore al 31/12
- **RW3**: Plusvalenze realizzate
- **RW4**: Imposta IVIE/IVAFE

**Dati da compilare**:
```
RW1 - Paese estero
RW2 - Tipo di investimento
RW3 - Valore al 31/12
RW4 - Imposta IVAFE (2‰ per conti, 0,2% per titoli)
```

**Esempio conto estero**:
```
Conto bancario USA: valore 50.000€
RW1: USA
RW2: Conto bancario
RW3: 50.000€
RW4: 50.000 × 2‰ = 100€ (IVAFE)
```

#### Quadro RT - Redditi diversi e deduzioni

**Sezioni**:
- **RT10**: Redditi diversi (plusvalenze)
- **RT20**: Deduzioni
- **RT30**: Detrazioni

**Dati da compilare**:
```
RT1 - Tipo di reddito diverso
RT2 - Importo plusvalenza
RT3 - Costo di acquisto
RT4 - Plusvalenza netta
```

**Esempio plusvalenza azioni**:
```
Vendita azioni: 20.000€
Costo acquisto: 15.000€
Plusvalenza: 5.000€
RT2: 5.000€
RT3: 15.000€
RT4: 5.000€
```

### 1.4 Sezione Deduzioni e Detrazioni

**Deduzioni** (riducono il reddito imponibile):
- Contributi previdenziali e assistenziali
- Spese mediche (parzialmente)
- Interessi mutuo prima casa
- Spese di ristrutturazione

**Detrazioni** (riducono l'imposta lorda):
- Detrazioni lavoro dipendente
- Detrazioni pensione
- Detrazioni carichi di famiglia
- Detrazioni spese mediche (19%)
- Detrazioni ristrutturazione (50%)

**Esempio**:
```
Reddito imponibile: 40.000€
Contributi previdenziali: 3.000€
Reddito dopo deduzioni: 37.000€

Imposta lorda su 37.000€: 8.510€
Detrazioni lavoro dipendente: 1.200€
Detrazioni spese mediche: 200€
Imposta netta: 7.110€
```

## 2. Modello 770

### 2.1 Cos'è il Modello 770

Il **Modello 770** è la dichiarazione per:
- Comunicare le ritenute operate su redditi di lavoro
- Comunicare i compensi a professionisti
- Comunicare altri tributi sostituiti

**Soggetti obbligati**:
- Sostituti d'imposta (datori di lavoro, clienti di professionisti)
- Enti pubblici e privati che erogano redditi

**Scadenza**: 30 settembre dell'anno successivo.

### 2.2 Struttura del Modello 770

**Sezione I - Ritenute su redditi di lavoro dipendente**
```
Dati da compilare:
- Codice fiscale sostituto
- Codice fiscale sostituito
- Importo redditi
- Ritenuta IRPEF operata
- Ritenuta INPS operata
```

**Esempio**:
```
Dipendente: Mario Rossi
Reddito annuo: 35.000€
Ritenuta IRPEF: 8.000€
Ritenuta INPS: 3.000€
```

**Sezione II - Ritenute su redditi di lavoro autonomo**
```
Dati da compilare:
- Codice fiscale sostituto
- Codice fiscale sostituito
- Importo compensi
- Ritenuta d'acconto (20%)
```

**Esempio**:
```
Professionista: Studio Bianchi
Compenso: 10.000€
Ritenuta d'acconto: 2.000€ (20%)
```

**Sezione III - Altri tributi**
```
Dati da compilare:
- Tipo di tributo
- Importo
- Periodo di riferimento
```

### 2.3 Scadenze e versamenti

| Adempimento | Scadenza |
|-------------|----------|
| Dichiarazione 770 | 30 settembre |
| Versamento ritenute | Mensile (16 del mese successivo) |
| Versamento conguaglio | 30 settembre |

## 3. Dichiarazione IVA Annuale

### 3.1 Cos'è la Dichiarazione IVA Annuale

La **Dichiarazione IVA Annuale** è il riepilogo annuale delle operazioni IVA.

**Soggetti obbligati**:
- Tutti i soggetti IVA
- Anche se in regime di esenzione

**Scadenza**: 30 novembre dell'anno successivo.

### 3.2 Struttura della Dichiarazione IVA

**Quadro VE - Cessioni di beni**
```
Dati da compilare:
- Operazioni imponibili per aliquota
- Operazioni esenti
- Operazioni non imponibili
```

**Esempio**:
```
Operazioni imponibili 22%: 100.000€
Operazioni imponibili 10%: 20.000€
Operazioni esenti: 5.000€
```

**Quadro VL - Acquisti di beni**
```
Dati da compilare:
- Acquisti imponibili per aliquota
- Acquisti esenti
- Acquisti non imponibili
```

**Esempio**:
```
Acquisti imponibili 22%: 60.000€
Acquisti imponibili 10%: 10.000€
```

**Quadro VR - Liquidazione IVA**
```
Dati da compilare:
- IVA a debito (da Quadro VE)
- IVA a credito (da Quadro VL)
- Saldo finale
- Credito da riportare / Debito da versare
```

**Esempio**:
```
IVA a debito: 24.000€ (100.000 × 22% + 20.000 × 10%)
IVA a credito: 14.200€ (60.000 × 22% + 10.000 × 10%)
Saldo: 9.800€ (da versare)
```

**Quadro VS - Riepilogo versamenti**
```
Dati da compilare:
- Versamenti mensili/trimestrali già effettuati
- Saldo finale da versare
- Credito da compensare
```

### 3.3 Operazioni particolari

**Operazioni intracomunitarie**:
```
Quadro VE: Cessioni intracomunitarie (aliquota 0%)
Quadro VL: Acquisti intracomunitari (aliquota 0%)
Quadro VI: Riepilogo operazioni UE
```

**Operazioni extra-UE**:
```
Quadro VE: Esportazioni (aliquota 0%)
Quadro VL: Importazioni (IVA doganale)
```

**Reverse charge**:
```
Quadro VL: Acquisti con inversione contabile
IVA registrata ma non versata (auto-liquidazione)
```

## 4. Scadenze Fiscali Annuali

### 4.1 Calendario dichiarazioni

| Dichiarazione | Scadenza | Periodo di riferimento |
|---------------|----------|------------------------|
| Modello Redditi PF | 30 novembre | Anno precedente |
| Modello 770 | 30 settembre | Anno precedente |
| Dichiarazione IVA | 30 novembre | Anno precedente |
| Comunicazione dati fatture | 16 marzo | Anno precedente |

### 4.2 Versamenti associati

| Versamento | Scadenza | Descrizione |
|------------|----------|-------------|
| Saldo IRPEF | 30 novembre | Saldo anno precedente + 1° acconto |
| Saldo IVA | 30 novembre | Saldo anno precedente |
| Saldo 770 | 30 settembre | Ritenute non versate |
| 2° acconto IRPEF | 30 novembre | Acconto anno corrente |

## 5. Esempio Completo: Modello Redditi PF

### 5.1 Scenario

**Contribuente**: Mario Rossi
**Redditi 2025**:
- Lavoro dipendente: 35.000€
- Locazione cedolare secca: 12.000€
- Dividendi: 5.000€
- Plusvalenza azioni: 3.000€

**Detrazioni**:
- Lavoro dipendente: 1.200€
- Spese mediche: 1.000€ (detrazione 19% = 190€)
- Interessi mutuo: 2.000€ (detrazione 19% = 380€)

### 5.2 Compilazione

**Quadro RF (lavoro dipendente)**:
```
RF3: 35.000€ (reddito da lavoro)
RF5: 35.000€ (reddito imponibile)
```

**Quadro RL (cedolare secca)**:
```
RL2: 12.000€ (canone locazione)
RL4: 12.000€ (reddito netto - cedolare non concorre a IRPEF)
```

**Quadro RM (dividendi)**:
```
RM2: 5.000€ (dividendi lordi)
RM3: 1.300€ (ritenuta 26%)
RM4: 3.700€ (reddito netto)
```

**Quadro RT (plusvalenze)**:
```
RT2: 3.000€ (plusvalenza)
RT4: 3.000€ (plusvalenza netta)
Imposta: 3.000 × 26% = 780€
```

**Calcolo IRPEF**:
```
Reddito imponibile: 35.000€
Imposta lorda (scaglioni):
  28.000 × 23% = 6.440€
  7.000 × 35% = 2.450€
  Totale: 8.890€

Detrazioni:
  Lavoro dipendente: 1.200€
  Spese mediche: 190€
  Interessi mutuo: 380€
  Totale: 1.770€

Imposta netta: 8.890 - 1.770 = 7.120€
```

**Totale imposte 2025**:
```
IRPEF: 7.120€
Cedolare secca: 12.000 × 21% = 2.520€
Imposta dividendi: 1.300€ (già versata alla fonte)
Imposta plusvalenze: 780€
Totale: 7.120 + 2.520 + 1.300 + 780 = 11.720€
```

## 6. Riferimenti Normativi

- **D.P.R. 917/1986 (TUIR)**: Testo Unico delle Imposte sui Redditi
- **D.P.R. 633/1972**: Istituzione e disciplina dell'IVA
- **D.Lgs. 471/1997**: Sanzioni per omessa dichiarazione
- **Art. 21 D.L. 78/2010**: Scadenze dichiarazioni fiscali

## 7. Checklist per Dichiarazioni

### 7.1 Prima di compilare Modello Redditi

- [ ] Raccogliere CU (Certificazione Unica) da tutti i datori di lavoro
- [ ] Raccogliere documentazione spese detraibili
- [ ] Verificare dati immobili (rendite catastali)
- [ ] Raccogliere estratti conto finanziari
- [ ] Verificare dati crypto (valore al 31/12)
- [ ] Calcolare acconti da versare

### 7.2 Prima di compilare 770

- [ ] Riepilogare tutte le ritenute operate
- [ ] Verificare versamenti mensili effettuati
- [ ] Calcolare conguaglio finale
- [ ] Verificare codici tributo F24

### 7.3 Prima di compilare dichiarazione IVA

- [ ] Riepilogare registri IVA acquisti/vendite
- [ ] Verificare liquidazioni periodiche
- [ ] Calcolare saldo finale
- [ ] Verificare operazioni intracomunitarie
- [ ] Controllare operazioni con reverse charge
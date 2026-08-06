---
title: Calcolo Contributi INPS - Guida Completa
description: Guida dettagliata al calcolo dei contributi INPS per tutte le gestioni: dipendenti, artigiani, commercianti, gestione separata
version: 0.1.0
last_updated: 2024-01-15
---

# Calcolo Contributi INPS - Guida Completa

## Introduzione

Questa guida fornisce una trattazione approfondita del calcolo dei contributi INPS per tutte le principali gestioni previdenziali. Il materiale è destinato a consulenti del lavoro, commercialisti e professionisti che necessitano di riferimenti operativi precisi.

**Riferimenti normativi principali:**
- D.P.R. 180/1950 - T.U. previdenziale
- L. 388/2000 - Legge finanziaria (disposizioni contributive)
- D.Lgs. 2277/2003 - Riordino gestioni previdenziali
- Circolari INPS operative (aggiornamenti annuali)

---

## 1. Contributi INPS per Dipendenti

### 1.1 Struttura del calcolo

Per i dipendenti, il sistema contributivo prevede un **riparto tra datore di lavoro e lavoratore**:

| Componente | Aliquota tipica (2024) | A carico |
|------------|------------------------|----------|
| Contributo ordinario | 33.00% | Datore di lavoro |
| Contributo lavoratore | 9.19% | Lavoratore (trattenuta) |
| **Totale** | **42.19%** | - |

**Nota:** Le aliquote variano in base a:
- Categoria professionale (operaio, impiegato, quadro, dirigente)
- Dimensione aziendale
- Settore CCNL applicato
- Agevolazioni specifiche (es. assundero under 36, donne, Sud)

### 1.2 Imponibile contributivo

L'imponibile contributivo comprende:
- Retribuzione base (minimo tabellare CCNL)
- Superminimi individuali
- Contingenza e MCI
- Straordinari
- Indennità varie (trasferta, missione, ecc.)
- TFR (per alcune gestioni)

**Esclusioni dall'imponibile:**
- Indennità di malattia (parzialmente)
- Indennità di maternità
- Rimborso spese (se documentato)
- Fringe benefit entro limiti esenti

### 1.3 Massimale contributivo

Per il 2024, il massimale contributivo è **€ 107.970,00**.

**Regola di calcolo:**
```
Se retribuzione_annua <= massimale:
    imponibile = retribuzione_annua
Altrimenti:
    imponibile = massimale
```

**Esempio pratico:**
```
Dipendente impiegato - Retribuzione annua: € 60.000,00
Massimale 2024: € 107.970,00

Poiché € 60.000 < € 107.970 → imponibile = € 60.000

Contributo datore: € 60.000 × 33% = € 19.800,00
Contributo lavoratore: € 60.000 × 9.19% = € 5.514,00
```

### 1.4 Esempio completo - Cedolino mensile

```
Dipendente: Mario Rossi
Livello: C1 (CCNL Metalmeccanico)
Retribuzione mensile lorda: € 2.400,00

CALCOLO CONTRIBUTI MENSILI:

Contributi a carico datore:
  € 2.400,00 × 33.00% = € 792,00

Contributi a carico lavoratore:
  € 2.400,00 × 9.19% = € 220,56

Retribuzione netta (prima delle IRPEF):
  € 2.400,00 - € 220,56 = € 2.179,44
```

---

## 2. Contributi INPS per Artigiani

### 2.1 Struttura contributiva

Gli artigiani sono iscritti alla **Gestione Artigiani e Commercianti INPS**. Il sistema prevede:

| Componente | Descrizione |
|------------|-------------|
| Contributo minimo | Fisso annuo, dovuto anche senza attività |
| Contributo aggiuntivo | Percentuale sulla parte di reddito eccedente il minimo |
| Acconto | Versamenti anticipati basati sull'anno precedente |

### 2.2 Contributo minimo 2024

Il contributo minimo annuo per artigiani è **€ 4.418,64** (circa € 368,22/mese).

**Composizione:**
- Parte previdenziale: ~€ 3.800,00
- Parte assistenziale: ~€ 618,64

### 2.3 Scaglioni di reddito e aliquote

| Scaglione reddito | Aliquota applicabile |
|-------------------|---------------------|
| Fino a € 17.934 | Contributo minimo |
| € 17.934 - € 50.279 | 24% sulla eccedenza |
| Oltre € 50.279 | 24% + maggiorazioni |

### 2.4 Esempio completo - Artigiano

```
Artigiano: Giuseppe Bianchi
Attività: Idraulico (CCNL Artigianato)
Reddito imponibile 2024: € 35.000,00

CALCOLO CONTRIBUTI:

1. Contributo minimo: € 4.418,64

2. Reddito eccedente il minimo:
   € 35.000 - € 17.934 = € 17.066

3. Contributo aggiuntivo:
   € 17.066 × 24% = € 4.095,84

4. Totale contributi dovuti:
   € 4.418,64 + € 4.095,84 = € 8.514,48

5. Versamento:
   - Acconto 2024 (basato su 2023): da calcolare
   - Saldo 2024: differenza dopo acconti
```

### 2.5 Riduzioni e agevolazioni

**Giovani under 36:**
- Riduzione del 35% del contributo minimo per i primi 3 anni
- Requisiti: apertura partita IVA dopo i 36 anni di età

**Donne:**
- Riduzione del 35% del contributo minimo per i primi 3 anni
- Applicabile indipendentemente dall'età

**Zone svantaggiate:**
- Agevolazioni per attività avviate nel Mezzogiorno
- Riduzioni fino al 50% in alcune province

---

## 3. Contributi INPS per Commercianti

### 3.1 Struttura contributiva

Identica a quella degli artigiani, con differenze nei soli importi:

| Componente | Commercianti 2024 |
|------------|-------------------|
| Contributo minimo | € 4.418,64 (uguale artigiani) |
| Aliquota scaglione | 24% |
| Massimale | € 107.970,00 |

### 3.2 Esempio completo - Commerciante

```
Commerciante: Laura Verdi
Attività: Negozio di abbigliamento
Reddito imponibile 2024: € 28.000,00

CALCOLO CONTRIBUTI:

1. Contributo minimo: € 4.418,64

2. Reddito eccedente il minimo:
   € 28.000 - € 17.934 = € 10.066

3. Contributo aggiuntivo:
   € 10.066 × 24% = € 2.415,84

4. Totale contributi dovuti:
   € 4.418,64 + € 2.415,84 = € 6.834,48
```

### 3.3 Ditta individuale vs Società

**Ditta individuale:**
- Il titolare è iscritto come lavoratore autonomo
- Contributi calcolati sul reddito d'impresa

**Società (S.r.l., S.p.A.):**
- Amministratore socio: gestione separata o artigiani/commercianti
  - Se amministratore unico: spesso gestione separata
  - Se consiglio di amministrazione: artigiani/commercianti
- Dipendenti: gestione ordinaria dipendenti

---

## 4. Gestione Separata INPS

### 4.1 Chi è soggetto

La Gestione Separata comprende:
- Collaboratori coordinati e continuativi (co.co.co)
- Professionisti senza cassa previdenziale
- Amministratori di società (in alcuni casi)
- Venditori porta a porta
- Agenti di affari in mediazione

### 4.2 Aliquote 2024

| Categoria | Aliquota |
|-----------|----------|
| Collaboratori | 25.98% |
| Professionisti | 25.98% |
| Agenti di commercio | 25.98% (sulla parte di provvigioni) |

**Nota:** L'intera aliquota è a carico del lavoratore. Il committente non versa contributi aggiuntivi.

### 4.3 Soglie di esenzione

**Soglia minima:**
- Se il reddito annuo è inferiore a € 5.150,00 (2024), non si versano contributi
- Si registra solo la posizione contributiva

### 4.4 Esempio completo - Collaboratore

```
Collaboratore: Anna Neri
Tipo: Collaborazione coordinata e continuativa
Compenso annuo 2024: € 18.000,00

CALCOLO CONTRIBUTI:

1. Verifica soglia minima:
   € 18.000 > € 5.150 → soggetti a contributi

2. Contributo dovuto:
   € 18.000 × 25.98% = € 4.676,40

3. Versamento:
   - Il committente trattiene e versa i contributi
   - Modello F24 con codice tributo specifico
```

### 4.5 Esempio completo - Professionista senza cassa

```
Professionista: Ing. Carlo Rossi
Ordine: Non iscritto a cassa (ingegneri hanno cassa propria)
Compenso annuo 2024: € 45.000,00

CALCOLO CONTRIBUTI:

1. Contributo dovuto:
   € 45.000 × 25.98% = € 11.691,00

2. Versamento:
   - 4 acconti (giugno, settembre, dicembre, marzo)
   - Saldo entro il 30 giugno dell'anno successivo
```

---

## 5. Confronto tra Gestioni

### 5.1 Tabella comparativa

| Elemento | Dipendenti | Artigiani | Commercianti | Gestione Separata |
|----------|------------|-----------|--------------|-------------------|
| Contributo minimo | No | Sì (€ 4.418,64) | Sì (€ 4.418,64) | No |
| Aliquota datore | ~33% | - | - | - |
| Aliquota lavoratore | 9.19% | 24% (sopra minimo) | 24% (sopra minimo) | 25.98% |
| Massimale | € 107.970 | € 107.970 | € 107.970 | No massimale |
| Acconti | No | Sì | Sì | Sì |

### 5.2 Scelta della gestione corretta

**Flusso decisionale:**

```
1. Il soggetto ha un contratto di lavoro subordinato?
   SÌ → Gestione Dipendenti
   NO → Vai al punto 2

2. Il soggetto è iscritto a un'altra cassa previdenziale?
   SÌ → Gestione della cassa di appartenenza
   NO → Vai al punto 3

3. Il soggetto ha apertura partita IVA come artigiano?
   SÌ → Gestione Artigiani
   NO → Vai al punto 4

4. Il soggetto ha apertura partita IVA come commerciante?
   SÌ → Gestione Commercianti
   NO → Gestione Separata
```

---

## 6. Riscatti e Totalizzazione

### 6.1 Riscatto di laurea

**Requisiti:**
- Laurea conseguita in Italia o all'estero
- Domanda entro 12 mesi dalla laurea (per aliquota ridotta)

**Costo riscatto:**
- Calcolato in base all'età al momento della domanda
- Aliquota: 20% della retribuzione pensionabile
- Rateizzazione fino a 120 mesi

**Esempio:**
```
Laureato: 30 anni
Retribuzione pensionabile media: € 30.000,00
Anni da riscattare: 5

Costo: € 30.000 × 20% × 5 = € 30.000,00
Rate: € 30.000 / 120 = € 250,00/mese
```

### 6.2 Totalizzazione

**Finalità:**
- Riunire periodi contributivi in diverse gestioni
- Raggiungere i requisiti minimi per la pensione

**Requisiti:**
- Almeno 20 anni di contributi complessivi
- Nessun periodo sovrapposto

---

## 7. Controlli e Verifiche

### 7.1 Verifica posizione contributiva

**Strumenti INPS:**
- Servizi online "Estratto conto contributivo"
- App INPS Mobile
- Patronati (gratuito)

**Cosa verificare:**
- Continuità contributiva
- Corrispondenza retribuzioni dichiarate
- Classificazione corretta della gestione

### 7.2 Discrepanze comuni

| Problema | Soluzione |
|----------|-----------|
| Contributi non accreditati | Presentare domanda di rettifica |
| Doppia iscrizione | Richiedere cancellazione dalla gestione errata |
| Aliquota errata | Verificare CCNL e comunicare correzione |
| Mancata dichiarazione UNIEMENS | Presentare dichiarazione integrativa |

---

## 8. Riferimenti Operativi

### 8.1 Moduli e codici tributo

**F24 - Codici principali:**

| Codice | Descrizione |
|--------|-------------|
| 8901 | Contributi previdenziali a carico datore |
| 8902 | Contributi previdenziali a carico dipendente |
| 8950 | Contributi gestione separata |
| 8960 | Contributi artigiani |
| 8961 | Contributi commercianti |

### 8.2 Scadenze

| Adempimento | Scadenza |
|-------------|----------|
| Versamento contributi dipendenti | 16 del mese successivo |
| Versamento contributi artigiani/commercianti | Acconti: giugno/settembre/dicembre/marzo |
| Dichiarazione annuale | Entro il 30 giugno |
| CU per collaboratori | 16 marzo dell'anno successivo |

---

## 9. Aggiornamenti 2024

### 9.1 Variazioni aliquote

- Gestione dipendenti: nessuna variazione (33% datore, 9.19% lavoratore)
- Gestione separata: 25.98% (invariata)
- Artigiani/commercianti: 24% (invariato)

### 9.2 Variazioni massimali

- Massimale contributivo 2024: € 107.970,00 (aumento da € 105.000,00 del 2023)

### 9.3 Novità normative

- Estensione agevolazioni under 36 per nuovi assunti
- Modifiche al riscatto di laurea (proroga termini)

---

**Nota finale:** Questa guida è aggiornata al gennaio 2024. Verificare sempre le circolari INPS più recenti per aggiornamenti normativi.
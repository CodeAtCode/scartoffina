---
title: Guida al Riparto Millesimale
description: Criteri di ripartizione spese condominiali: tabelle millesimali, scale, ascensore, riscaldamento, ricalcolo
skill: amministratore-condominio
version: 0.1.0
updated: 2026-08-05
---

# Guida al Riparto Millesimale

Guida tecnica alla ripartizione delle spese condominiali: tabelle millesimali, criteri per scale/ascensore/riscaldamento, ricalcolo e contestazioni.

## 1. Fondamenti Giuridici

### 1.1 Base Legale

| Norma | Contenuto |
|-------|-----------|
| **Art. 1123 c.c.** | Ripartizione spese in proporzione al valore delle proprietà |
| **Art. 1124 c.c.** | Ripartizione spese per scale e ascensore |
| **Art. 1125 c.c.** | Ripartizione spese per piani diversi |
| **Art. 1117 c.c.** | Definizione delle parti comuni |

### 1.2 Principio Generale

Le spese condominiali si ripartiscono secondo due criteri:
1. **Proporzionale al valore millesimale** (art. 1123 c.c.) — per spese di conservazione e godimento delle parti comuni
2. **In ragione dell'uso** (art. 1124 c.c.) — per spese relative a servizi o parti di uso differenziato

---

## 2. Tabelle Millesimali

### 2.1 Cosa Sono

Le **tabelle millesimali** sono tabelle che assegnano a ciascun unità immobiliare un valore in millesimi (parti per mille) che rappresenta:
- Il **valore relativo** dell'unità rispetto all'intero edificio
- La **quota di partecipazione** alle spese condominiali

### 2.2 Struttura della Tabella

```
TABELLA MILLESIMALE - CONDOMINIO VIA ROMA 10

Unità    | Descrizione          | Millesimi di proprietà | Millesimi di uso
---------|----------------------|------------------------|------------------
1        | Piano terra - Negozio| 150                    | 150
2        | Piano 1 - Interno A  | 120                    | 120
3        | Piano 1 - Interno B  | 100                    | 100
4        | Piano 2 - Interno A  | 110                    | 110
5        | Piano 2 - Interno B  | 95                     | 95
6        | Piano 3 - Interno A  | 105                    | 105
7        | Piano 3 - Interno B  | 90                     | 90
8        | Soffitte             | 50                     | 50
9        | Cantine              | 180                    | 180
---------|----------------------|------------------------|------------------
TOTALE   |                      | 1000                   | 1000
```

### 2.3 Criteri di Calcolo dei Millesimi

I millesimi di proprietà si calcolano considerando:
- **Superficie** (mq) dell'unità
- **Altezza** del soffitto
- **Piano** di ubicazione
- **Esposizione** (sole, vista)
- **Servizi** disponibili (ascensore, portineria)
- **Destinazione d'uso** (abitazione, ufficio, commerciale)

**Formula base:**
```
Valore unità = Superficie × Coefficiente piano × Coefficiente esposizione × Coefficiente destinazione
Millesimi unità = (Valore unità / Somma valori tutte le unità) × 1000
```

---

## 3. Criteri di Ripartizione per Tipo di Spesa

### 3.1 Spese Generali (Art. 1123 c.c.)

**Spese coperte:**
- Pulizia parti comuni
- Illuminazione parti comuni
- Manutenzione ordinaria edificio
- Amministratore
- Assicurazione condominio
- Fondo per lavori straordinari

**Criterio:** Millesimi di proprietà al 100%

**Esempio:**
```
Spesa totale: € 10.000
Condomino Rossi: 120 millesimi
Quota Rossi: € 10.000 × (120 / 1000) = € 1.200
```

### 3.2 Scale e Ascensore (Art. 1124 c.c.)

**Spese coperte:**
- Manutenzione scale
- Pulizia scale
- Manutenzione ascensore
- Energia ascensore
- Assicurazione ascensore

**Criterio:** 50% millesimi di proprietà + 50% millesimi di altezza

**Formula:**
```
Quota = (Spesa × 0,5 × millesimi_proprietà / 1000) + (Spesa × 0,5 × millesimi_altezza / 1000)
```

**Esempio:**
```
Spesa ascensore: € 5.000
Condomino Rossi: 120 millesimi proprietà, piano 3 (coefficiente altezza 1,3)
Millesimi altezza Rossi: 120 × 1,3 = 156
Millesimi altezza totale edificio: 1100

Quota Rossi = (€ 5.000 × 0,5 × 120 / 1000) + (€ 5.000 × 0,5 × 156 / 1100)
Quota Rossi = € 300 + € 354,55 = € 654,55
```

### 3.3 Riscaldamento Centrale

**Spese coperte:**
- Gas/energia per riscaldamento
- Manutenzione caldaia
- Manutenzione radiatori
- Contatori/valvole termostatiche

**Criterio:** 50% millesimi termici + 50% consumo effettivo (se presenti contatori)

**Formula (con contatori):**
```
Quota fissa = Spesa totale × 0,5 × millesimi_termici / 1000
Quota consumo = Spesa totale × 0,5 × consumo_unità / consumo_totale
Quota totale = Quota fissa + Quota consumo
```

**Esempio:**
```
Spesa riscaldamento: € 20.000
Condomino Rossi: 120 millesimi termici
Consumo Rossi: 15.000 Kcal
Consumo totale condominio: 150.000 Kcal

Quota fissa = € 20.000 × 0,5 × 120 / 1000 = € 1.200
Quota consumo = € 20.000 × 0,5 × 15.000 / 150.000 = € 1.000
Quota totale = € 1.200 + € 1.000 = € 2.200
```

### 3.4 Acqua Potabile

**Spese coperte:**
- Acquisto acqua
- Manutenzione serbatoi
- Manutenzione tubature

**Criterio:**
- Se contatori individuali: 100% consumo
- Se nessun contatore: 50% millesimi + 50% numero di persone (se dichiarato)

**Esempio (senza contatori):**
```
Spesa acqua: € 3.000
Condomino Rossi: 120 millesimi, 4 persone
Millesimi totale: 1000
Persone totali: 50

Quota millesimi = € 3.000 × 0,5 × 120 / 1000 = € 180
Quota persone = € 3.000 × 0,5 × 4 / 50 = € 120
Quota totale = € 180 + € 120 = € 300
```

### 3.5 Spese per Pertinenze

**Spese coperte:**
- Manutenzione box auto
- Manutenzione cantine
- Manutenzione soffitte

**Criterio (art. 1123 c.3):** Solo chi usa la pertinenza

**Esempio:**
```
Spesa manutenzione box: € 1.000
Solo 5 condomini hanno box
Quota per box = € 1.000 / 5 = € 200 per box
Condomini senza box: € 0
```

---

## 4. Tabelle di Riparto per Tipo di Spesa

### 4.1 Spese Generali (Millesimi di Proprietà)

| Condomino | Millesimi | % | Spesa € 10.000 |
|-----------|-----------|-----|----------------|
| Rossi | 120 | 12% | € 1.200 |
| Bianchi | 100 | 10% | € 1.000 |
| Verdi | 95 | 9,5% | € 950 |
| Neri | 110 | 11% | € 1.100 |
| Altri | 575 | 57,5% | € 5.750 |
| **TOTALE** | **1000** | **100%** | **€ 10.000** |

### 4.2 Ascensore (50% Proprietà + 50% Altezza)

| Condomino | Millesimi Prop. | Millesimi Altezza | % Prop. | % Alt. | Spesa € 5.000 |
|-----------|-----------------|-------------------|---------|--------|---------------|
| Rossi (p.3) | 120 | 156 | 12% | 14,2% | € 654,55 |
| Bianchi (p.2) | 100 | 120 | 10% | 10,9% | € 545,45 |
| Verdi (p.1) | 95 | 100 | 9,5% | 9,1% | € 468,18 |
| Neri (p.0) | 110 | 80 | 11% | 7,3% | € 431,82 |
| Altri | 575 | 644 | 57,5% | 58,5% | € 2.899,09 |
| **TOTALE** | **1000** | **1100** | **100%** | **100%** | **€ 5.000** |

### 4.3 Riscaldamento (50% Termico + 50% Consumo)

| Condomino | Millesimi Termici | Consumo Kcal | % Termico | % Consumo | Spesa € 20.000 |
|-----------|-------------------|--------------|-----------|-----------|----------------|
| Rossi | 120 | 15.000 | 12% | 10% | € 2.200 |
| Bianchi | 100 | 12.000 | 10% | 8% | € 1.800 |
| Verdi | 95 | 10.000 | 9,5% | 6,7% | € 1.620 |
| Neri | 110 | 18.000 | 11% | 12% | € 2.300 |
| Altri | 575 | 95.000 | 57,5% | 63,3% | € 12.080 |
| **TOTALE** | **1000** | **150.000** | **100%** | **100%** | **€ 20.000** |

---

## 5. Spese per Scale, Ascensore, Tetto, Cortile

### 5.1 Scale

**Criterio:** Art. 1124 c.c. — 50% proprietà + 50% altezza

**Formula:**
```
Quota = (Spesa × 0,5 × millesimi_prop / 1000) + (Spesa × 0,5 × millesimi_alt / totale_alt)
```

### 5.2 Ascensore

**Criterio:** Art. 1124 c.c. — 50% proprietà + 50% altezza

**Nota:** Gli stessi criteri delle scale si applicano all'ascensore.

### 5.3 Tetto e Copertura

**Criterio:** Art. 1123 c.c. — 100% millesimi di proprietà

**Motivazione:** Il tetto è parte comune che serve tutti i piani in proporzione al valore dell'unità.

**Esempio:**
```
Spesa rifacimento tetto: € 50.000
Condomino Rossi: 120 millesimi
Quota Rossi: € 50.000 × 120 / 1000 = € 6.000
```

### 5.4 Cortile e Aree Esterne

**Criterio:** Art. 1123 c.c. — 100% millesimi di proprietà

**Eccezione:** Se alcune unità non hanno accesso al cortile, possono essere esentate (delibera assembleare).

---

## 6. Ricalcolo delle Tabelle Millesimali

### 6.1 Quando Ricalcolare

| Situazione | Necessità |
|------------|-----------|
| Ristrutturazione che cambia superficie | Obbligatorio |
| Cambio destinazione d'uso | Obbligatorio |
| Divisione di un'unità | Obbligatorio |
| Accorpamento di unità | Obbligatorio |
| Errore nella tabella originale | Consigliato |
| Scontento generale dei condomini | Facoltativo (serve delibera) |

### 6.2 Procedura di Ricalcolo

1. **Delibera assembleare** — Approvazione del ricalcolo (maggioranza art. 1136 c.c.)
2. **Nomina tecnico** — Geometra, architetto o ingegnere per il ricalcolo
3. **Redazione nuova tabella** — Con calcolo dei nuovi millesimi
4. **Approvazione assembleare** — Delibera con maggioranza qualificata
5. **Aggiornamento documenti** — Inserimento nel regolamento e nei rendiconti

### 6.3 Maggioranze per Modifica Tabelle

| Tipo di modifica | Maggioranza richiesta |
|------------------|----------------------|
| Ricalcolo per lavori | Art. 1136 c.2 (maggioranza intervenuti + 500 millesimi) |
| Modifica tabelle (contenzioso) | Art. 1136 c.5 (500 millesimi + metà valore edificio) |
| Approvazione nuova tabella | Art. 1136 c.2 (maggioranza intervenuti + 500 millesimi) |

### 6.4 Contestazione Tabelle

**Termini:**
- **Impugnazione delibera:** 30 giorni dalla delibera (art. 1137 c.c.)
- **Azione di ricalcolo:** 5 anni dalla scoperta dell'errore

**Motivi validi:**
- Errore di calcolo nella tabella originale
- Mancato aggiornamento dopo lavori
- Criteri di calcolo non conformi alla legge
- Valutazioni arbitrarie dei coefficienti

---

## 7. Prospetto di Riparto Modello

```
PROSPETTO DI RIPARTO SPESE
Condominio: Via Roma 10
Esercizio: 2025

TIPO SPESA: Manutenzione ordinaria
IMPORTO TOTALE: € 15.000
CRITERIO: Millesimi di proprietà

┌──────────────┬─────────────┬──────────────┬──────────────────┐
│ Condomino    │ Millesimi   │ Quota %      │ Importo €        │
├──────────────┼─────────────┼──────────────┼──────────────────┤
│ Rossi Mario  │ 120         │ 12,00%       │ € 1.800,00       │
│ Bianchi Luca │ 100         │ 10,00%       │ € 1.500,00       │
│ Verdi Anna   │ 95          │ 9,50%        │ € 1.425,00       │
│ Neri Paolo   │ 110         │ 11,00%       │ € 1.650,00       │
│ Gialli Sofia │ 90          │ 9,00%        │ € 1.350,00       │
│ Azzurri Marco│ 105         │ 10,50%       │ € 1.575,00       │
│ Altri (4)    │ 380         │ 38,00%       │ € 5.700,00       │
├──────────────┼─────────────┼──────────────┼──────────────────┤
│ TOTALE       │ 1000        │ 100,00%      │ € 15.000,00      │
└──────────────┴─────────────┴──────────────┴──────────────────┘

TIPO SPESA: Ascensore
IMPORTO TOTALE: € 4.000
CRITERIO: 50% proprietà + 50% altezza

┌──────────────┬─────────────┬─────────────┬──────────────┬──────────────────┐
│ Condomino    │ Millesimi   │ Millesimi   │ Quota %      │ Importo €        │
│              │ Proprietà   │ Altezza     │              │                  │
├──────────────┼─────────────┼─────────────┼──────────────┼──────────────────┤
│ Rossi Mario  │ 120         │ 156         │ 13,09%       │ € 523,64         │
│ Bianchi Luca │ 100         │ 120         │ 10,45%       │ € 418,18         │
│ Verdi Anna   │ 95          │ 100         │ 9,32%        │ € 372,73         │
│ Neri Paolo   │ 110         │ 80          │ 9,09%        │ € 363,64         │
│ Gialli Sofia │ 90          │ 60          │ 7,27%        │ € 290,91         │
│ Azzurri Marco│ 105         │ 140         │ 12,27%       │ € 490,91         │
│ Altri (4)    │ 380         │ 444         │ 38,52%       │ € 1.540,00       │
├──────────────┼─────────────┼─────────────┼──────────────┼──────────────────┤
│ TOTALE       │ 1000        │ 1100        │ 100,00%      │ € 4.000,00       │
└──────────────┴─────────────┴─────────────┴──────────────┴──────────────────┘
```

---

## 8. Riferimenti Normativi

- **Art. 1117 c.c.** — Parti comuni dell'edificio
- **Art. 1123 c.c.** — Ripartizione spese
- **Art. 1124 c.c.** — Scale e ascensore
- **Art. 1125 c.c.** — Piani diversi
- **Art. 1136 c.c.** — Maggioranze assembleari
- **Art. 1137 c.c.** — Impugnazione delibere

---

## 9. Checklist per l'Amministratore

Prima di redigere il riparto:

- [ ] Verificare le tabelle millesimali aggiornate
- [ ] Identificare il criterio corretto per ogni tipo di spesa
- [ ] Calcolare le quote con precisione (due decimali)
- [ ] Verificare che la somma delle quote = totale spesa
- [ ] Includere il prospetto nel rendiconto condominiale
- [ ] Conservare i calcoli a disposizione dei condomini
- [ ] Spiegare i criteri in assemblea se richiesti
---
title: Budget e Ripartizione Spese
description: Preventivo, ripartizione per tabelle millesimali, spese generali, scale, ascensori, riscaldamento
skill: amministratore-condominio
version: 0.2.0
updated: 2026-08-05
---

# Budget e Ripartizione Spese

Guida alla redazione del preventivo condominiale e alla ripartizione delle spese per tipo di tabella millesimale.

## 1. Bilancio Preventivo

### 1.1 Scopo

Il **bilancio preventivo** è lo strumento che stima le entrate e le uscite del condominio per l'anno successivo.

**Obiettivi:**
- Determinare le rate condominiali da richiedere
- Pianificare le spese ordinarie e straordinarie
- Valutare la necessità di accantonamenti
- Garantire la trasparenza gestionale

### 1.2 Base Legale

| Norma | Contenuto |
|-------|-----------|
| **Art. 1126 c.c.** | Obbligo di preventivo |
| **Art. 1130 c.c.** | Obblighi di contabilità |
| **L. 4/2013 art. 1126** | Trasparenza rendiconto |

### 1.3 Struttura del Preventivo

```
BILANCIO PREVENTIVO 2026
Condominio: [Nome/Indirizzo]

ENTRATE STIMATE:
┌─────────────────────────────────────┬──────────────┐
│ Voce                                │ Importo €    │
├─────────────────────────────────────┼──────────────┤
│ Rata ordinaria (1000 millesimi)     │ [calcolato]  │
│ Rata ascensore (tabella ascensori)  │ [calcolato]  │
│ Rata riscaldamento (tabella termica)│ [calcolato]  │
│ Rata acqua (tabella acqua)          │ [calcolato]  │
│ Altri proventi                      │ [importo]    │
├─────────────────────────────────────┼──────────────┤
│ TOTALE ENTRATE                      │ [totale]     │
└─────────────────────────────────────┴──────────────┘

USCITE STIMATE:
┌─────────────────────────────────────┬──────────────┐
│ Voce                                │ Importo €    │
├─────────────────────────────────────┼──────────────┤
│ Spese generali                      │ [importo]    │
│ Amministratore                      │ [importo]    │
│ Assicurazione                       │ [importo]    │
│ Manutenzione ordinaria              │ [importo]    │
│ Ascensore                           │ [importo]    │
│ Riscaldamento                       │ [importo]    │
│ Acqua                               │ [importo]    │
│ Spese bancarie                      │ [importo]    │
│ TARI                                │ [importo]    │
│ Fondo per imprevisti                │ [importo]    │
│ Fondo lavori straordinari           │ [importo]    │
├─────────────────────────────────────┼──────────────┤
│ TOTALE USCITE                       │ [totale]     │
└─────────────────────────────────────┴──────────────┘

SALDO PREVISIONALE: [avanzo/disavanzo]
```

---

## 2. Tipologie di Spese

### 2.1 Spese Generali (1000/1000)

**Oggetto:**
- Pulizia parti comuni
- Illuminazione parti comuni
- Portineria / concierge
- Assicurazione RC condominio
- Spese amministrative
- Spese bancarie
- TARI (tassa rifiuti)
- Manutenzione ordinaria edificio

**Criterio di ripartizione:** 100% millesimi di proprietà

**Formula:**
```
Quota condomino = Spesa totale × (millesimi_proprietà / 1000)
```

**Esempio:**
```
Spese generali totali: € 20.000
Condomino Rossi: 120 millesimi
Quota Rossi: € 20.000 × 120 / 1000 = € 2.400
```

### 2.2 Spese per Scale (Tabella Scale)

**Oggetto:**
- Pulizia scale
- Illuminazione scale
- Manutenzione scale
- Riparazione gradini, ringhiere

**Criterio di ripartizione:** 50% proprietà + 50% altezza

**Formula:**
```
Quota = (Spesa × 0,5 × millesimi_proprietà / 1000) + 
        (Spesa × 0,5 × millesimi_altezza / totale_altezza)
```

**Esempio:**
```
Spese scale: € 3.000
Condomino Rossi: 120 millesimi proprietà, 156 millesimi altezza
Totale millesimi altezza: 1100

Quota Rossi = (€ 3.000 × 0,5 × 120 / 1000) + (€ 3.000 × 0,5 × 156 / 1100)
Quota Rossi = € 180 + € 212,73 = € 392,73
```

### 2.3 Spese per Ascensore (Tabella Ascensori)

**Oggetto:**
- Manutenzione periodica ascensore
- Energia elettrica ascensore
- Assicurazione ascensore
- Riparazioni e sostituzioni

**Criterio di ripartizione:** 50% proprietà + 50% altezza

**Formula:** Stessa delle scale

**Esempio:**
```
Spese ascensore: € 5.000
Condomino Rossi: 120 millesimi proprietà, 156 millesimi altezza
Totale millesimi altezza: 1100

Quota Rossi = (€ 5.000 × 0,5 × 120 / 1000) + (€ 5.000 × 0,5 × 156 / 1100)
Quota Rossi = € 300 + € 354,55 = € 654,55
```

### 2.4 Spese per Riscaldamento (Tabella Termica)

**Oggetto:**
- Gas/energia per riscaldamento
- Manutenzione caldaia
- Manutenzione radiatori
- Valvole termostatiche

**Criterio di ripartizione:**
- **Con contatori:** 50% millesimi termici + 50% consumo effettivo
- **Senza contatori:** 100% millesimi termici

**Formula (con contatori):**
```
Quota fissa = Spesa totale × 0,5 × millesimi_termici / 1000
Quota consumo = Spesa totale × 0,5 × consumo_unità / consumo_totale
Quota totale = Quota fissa + Quota consumo
```

**Esempio:**
```
Spesa riscaldamento: € 25.000
Condomino Rossi: 120 millesimi termici
Consumo Rossi: 18.000 Kcal
Consumo totale: 180.000 Kcal

Quota fissa = € 25.000 × 0,5 × 120 / 1000 = € 1.500
Quota consumo = € 25.000 × 0,5 × 18.000 / 180.000 = € 1.250
Quota totale = € 1.500 + € 1.250 = € 2.750
```

### 2.5 Spese per Acqua (Tabella Acqua)

**Oggetto:**
- Acquisto acqua
- Manutenzione serbatoi
- Manutenzione tubature
- Fognatura

**Criterio di ripartizione:**
- **Con contatori:** 100% consumo
- **Senza contatori:** 50% millesimi + 50% numero di persone

**Formula (senza contatori):**
```
Quota millesimi = Spesa totale × 0,5 × millesimi / 1000
Quota persone = Spesa totale × 0,5 × persone_unità / persone_totali
Quota totale = Quota millesimi + Quota persone
```

**Esempio:**
```
Spesa acqua: € 4.000
Condomino Rossi: 120 millesimi, 4 persone
Persone totali: 50

Quota millesimi = € 4.000 × 0,5 × 120 / 1000 = € 240
Quota persone = € 4.000 × 0,5 × 4 / 50 = € 160
Quota totale = € 240 + € 160 = € 400
```

---

## 3. Tabelle Millesimali

### 3.1 Tipologie di Tabelle

| Tabella | Utilizzo |
|---------|----------|
| **Proprietà** | Spese generali (100%) |
| **Altezza** | Scale e ascensore (50%) |
| **Termica** | Riscaldamento (50% senza contatori) |
| **Acqua** | Spese idriche (50% senza contatori) |

### 3.2 Struttura della Tabella

```
TABELLA MILLESIMALE - CONDOMINIO VIA ROMA 10

Unità | Descrizione      | Proprietà | Altezza | Termica | Acqua
------|------------------|-----------|---------|---------|------
1     | Negozio p. terra | 150       | 80      | 150     | 150
2     | Interno 1A       | 120       | 120     | 120     | 120
3     | Interno 1B       | 100       | 120     | 100     | 100
4     | Interno 2A       | 110       | 140     | 110     | 110
5     | Interno 2B       | 95        | 140     | 95      | 95
6     | Interno 3A       | 105       | 160     | 105     | 105
7     | Interno 3B       | 90        | 160     | 90      | 90
8     | Soffitte          | 50        | 200     | 50      | 50
9     | Cantine           | 180       | 180     | 180     | 180
------|------------------|-----------|---------|---------|------
TOTALE|                  | 1000      | 1300    | 1000    | 1000
```

### 3.3 Aggiornamento Tabelle

Le tabelle devono essere aggiornate quando:

- Si effettuano **ristrutturazioni** che cambiano la superficie
- Si effettua un **cambio di destinazione d'uso**
- Si **divide** o **accorpa** un'unità
- Si rilevano **errori** nelle tabelle originali

---

## 4. Calcolo delle Quote

### 4.1 Formula Generale

Per ogni tipo di spesa:

```
Quota condomino = Spesa_tabella × (millesimi_tabella_condomino / totale_millesimi_tabella)
```

### 4.2 Esempio Completo

```
BILANCIO PREVENTIVO 2026
Condominio: Via Roma 10

SPESA GENERALE: € 20.000 (tabella proprietà)
SPESA SCALE: € 3.000 (tabella altezza)
SPESA ASCENSORE: € 5.000 (tabella altezza)
SPESA RISCALDAMENTO: € 25.000 (tabella termica + consumo)
SPESA ACQUA: € 4.000 (tabella proprietà)

CONDOMINO ROSSI: 120 millesimi proprietà, 156 millesimi altezza, 120 millesimi termici

Calcolo quote Rossi:
- Generale: € 20.000 × 120 / 1000 = € 2.400
- Scale: € 3.000 × 0,5 × 120 / 1000 + € 3.000 × 0,5 × 156 / 1300 = € 180 + € 180 = € 360
- Ascensore: € 5.000 × 0,5 × 120 / 1000 + € 5.000 × 0,5 × 156 / 1300 = € 300 + € 300 = € 600
- Riscaldamento (solo fissa): € 25.000 × 0,5 × 120 / 1000 = € 1.500
- Acqua: € 4.000 × 120 / 1000 = € 480

TOTALE ROSSI: € 2.400 + € 360 + € 600 + € 1.500 + € 480 = € 5.340
Rata mensile: € 5.340 / 12 = € 445
```

---

## 5. Prospetto di Riparto

### 5.1 Modello

```
PROSPETTO DI RIPARTO SPESE 2026
Condominio: Via Roma 10

┌──────────────┬───────────┬───────────┬───────────┬───────────┬───────────┐
│ Condomino    │ Generale  │ Scale     │ Ascensore │ Riscald.  │ Acqua     │
│              │ €         │ €         │ €         │ €         │ €         │
├──────────────┼───────────┼───────────┼───────────┼───────────┼───────────┤
│ Rossi Mario  │ 2.400,00  │ 360,00    │ 600,00    │ 1.500,00  │ 480,00    │
│ Bianchi Luca │ 2.000,00  │ 320,00    │ 533,33    │ 1.250,00  │ 400,00    │
│ Verdi Anna   │ 1.900,00  │ 304,00    │ 506,67    │ 1.187,50  │ 380,00    │
│ Neri Paolo   │ 2.200,00  │ 352,00    │ 586,67    │ 1.375,00  │ 440,00    │
│ Gialli Sofia │ 1.800,00  │ 288,00    │ 480,00    │ 1.125,00  │ 360,00    │
│ Azzurri Marco│ 2.100,00  │ 336,00    │ 560,00    │ 1.312,50  │ 420,00    │
│ Altri (3)    │ 7.600,00  │ 1.216,00  │ 2.033,33  │ 4.750,00  │ 1.520,00  │
├──────────────┼───────────┼───────────┼───────────┼───────────┼───────────┤
│ TOTALE       │ 20.000,00 │ 3.000,00  │ 5.000,00  │ 12.500,00 │ 4.000,00  │
└──────────────┴───────────┴───────────┴───────────┴───────────┴───────────┘

TOTALE PER CONDOMINO:
- Rossi: € 5.340,00 (€ 445/mese)
- Bianchi: € 4.503,33 (€ 375,28/mese)
- Verdi: € 4.291,67 (€ 357,64/mese)
- Neri: € 4.951,67 (€ 412,64/mese)
- Gialli: € 4.093,33 (€ 341,11/mese)
- Azzurri: € 4.728,33 (€ 394,03/mese)
```

---

## 6. Strumenti di Calcolo

### 6.1 Script Python

Per calcolare le quote condominiali:

```bash
python3 scripts/calc_quote.py \
  --spesa 12000 \
  --tipo generale \
  --tabelle tabelle.json
```

### 6.2 Input JSON per le Tabelle

```json
{
  "condominio": "Via Roma 10",
  "tabelle": {
    "proprietà": {
      "Rossi": 120,
      "Bianchi": 100,
      "Verdi": 95
    },
    "altezza": {
      "Rossi": 156,
      "Bianchi": 120,
      "Verdi": 100
    },
    "termica": {
      "Rossi": 120,
      "Bianchi": 100,
      "Verdi": 95
    }
  }
}
```

---

## 7. Riferimenti Normativi

- **Art. 1123 c.c.** — Ripartizione spese
- **Art. 1124 c.c.** — Scale e ascensore
- **Art. 1125 c.c.** — Piani diversi
- **Art. 1126 c.c.** — Preventivo
- **L. 4/2013 art. 1126** — Trasparenza

---

## 8. Checklist per il Bilancio Preventivo

- [ ] Raccogliere tutte le spese dell'anno precedente
- [ ] Identificare il tipo di tabella per ogni spesa
- [ ] Verificare le tabelle millesimali aggiornate
- [ ] Calcolare le quote per ciascun condomino
- [ ] Verificare che la somma delle quote = totale spesa
- [ ] Presentare il preventivo in assemblea
- [ ] Approvare con le maggioranze previste
- [ ] Comunicare le rate ai condomini
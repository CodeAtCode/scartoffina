---
title: Calcolo Cedolino Paga - Guida Completa
description: Guida dettagliata al calcolo del cedolino paga: dalla retribuzione lorda al netto, tutte le voci e trattenute
version: 0.1.0
last_updated: 2024-01-15
---

# Calcolo Cedolino Paga - Guida Completa

## Introduzione

Questa guida fornisce una trattazione operativa del calcolo del cedolino paga, elemento fondamentale della gestione del personale. Il materiale è destinato a consulenti del lavoro, responsabili HR e professionisti che necessitano di riferimenti precisi per l'elaborazione delle paghe.

**Riferimenti normativi principali:**
- D.Lgs. 152/1997 - Trasparenza retributiva
- D.Lgs. 276/2003 - Riforma Biagi
- TUIR (D.P.R. 917/1986) - Imposte sui redditi
- CCNL applicati per settore

---

## 1. Struttura del Cedolino

### 1.1 Sezione Anagrafica

**Dati obbligatori:**
- Nome e cognome del dipendente
- Codice fiscale
- Matricola INPS
- Livello di inquadramento
- CCNL applicato
- Mese di competenza
- Data di pagamento

### 1.2 Sezione Retributiva (Lato "Lordo")

**Componenti positivi:**
1. Retribuzione base
2. Contingenza e MCI
3. Scatti di anzianità
4. Straordinari
5. Indennità varie
6. TFR maturando

### 1.3 Sezione Trattenute

**Trattenute previdenziali:**
- Contributi INPS dipendente

**Trattenute fiscali:**
- IRPEF
- Addizionali regionali
- Addizionali comunali

**Altre trattenute:**
- Previdenza complementare
- Fondo sanitario
- Altre (assegni familiari, ecc.)

---

## 2. Componenti Retributivi

### 2.1 Retribuzione Base

**Composizione:**
- **Minimo tabellare CCNL:** Retribuzione minima per livello
- **Superminimo individuale:** Eventuale aumento individuale

**Esempio:**
```
CCNL Metalmeccanico Industria - Livello C1
Minimo tabellare 2024: € 1.850,00
Superminimo individuale: € 200,00

Retribuzione base: € 2.050,00
```

### 2.2 Contingenza e MCI

**Contingenza:**
- Indennità di contingenza (storica, non più aggiornata)
- Importo fisso per livello

**MCI (Maggiorazione Contingenza):**
- Maggiorazione contingenza
- Indicizzata all'IPC ISTAT

**Esempio:**
```
Livello C1:
  Contingenza: € 52,00
  MCI: € 128,00
  
Totale contingenza + MCI: € 180,00
```

### 2.3 Scatti di Anzianità

**Regola generale:**
- Aumento retributivo ogni 2 anni di servizio
- Percentuale variabile per CCNL (di norma 2-5%)

**Calcolo:**
```
Retribuzione base: € 2.050,00
Anzianità: 6 anni (3 scatti)
Percentuale scatto: 3%

Valore scatto: € 2.050 × 3% = € 61,50
Totale scatti: € 61,50 × 3 = € 184,50
```

### 2.4 Straordinari

**Maggiorazioni:**
- Straordinario diurno: +10-30%
- Straordinario notturno: +20-50%
- Straordinario festivo: +30-60%

**Esempio:**
```
Retribuzione oraria: € 12,00
Ore straordinarie diurne: 10
Maggiorazione: 20%

Straordinari: € 12,00 × 10 × 120% = € 144,00
```

### 2.5 Indennità

**Tipologie comuni:**
- **Indennità di trasferta:** Fuori sede (> 50 km)
- **Indennità di missione:** Per incarichi specifici
- **Indennità notturna:** Lavoro tra 22:00-6:00
- **Indennità di rischio:** Per attività pericolose

**Esempio:**
```
Giorni di trasferta: 5
Indennità giornaliera: € 45,00

Totale trasferta: € 45,00 × 5 = € 225,00
```

### 2.6 TFR Maturando

**Formula:**
```
TFR mensile = (Retribuzione annua lorda) / 13,5
```

**Esempio:**
```
Retribuzione annua lorda: € 30.000,00
TFR mensile: € 30.000 / 13,5 = € 2.222,22 / 12 = € 185,19
```

---

## 3. Calcolo Contributi INPS

### 3.1 Imponibile Contributivo

**Include:**
- Retribuzione base
- Contingenza e MCI
- Scatti di anzianità
- Straordinari
- Indennità (alcune esenti)

**Esclude:**
- Rimborso spese
- Some indennità esenti

**Esempio:**
```
Retribuzione base: € 2.050,00
Contingenza + MCI: € 180,00
Scatti anzianità: € 184,50
Straordinari: € 144,00
Trasferta: € 225,00 (parzialmente esente)

Imponibile contributivo: € 2.558,50
```

### 3.2 Aliquote INPS Dipendente

**Aliquota ordinaria 2024:** 9.19%

**Calcolo:**
```
Imponibile contributivo: € 2.558,50
Aliquota: 9.19%

Contributi INPS: € 2.558,50 × 9.19% = € 235,13
```

### 3.3 Dettaglio Cedolino

```
IMPEGNO CONTRIBUTIVO:
  Imponibile previdenziale: € 2.558,50
  Aliquota INPS: 9.19%
  Contributi a carico dipendente: € 235,13
```

---

## 4. Calcolo IRPEF

### 4.1 Imponibile Fiscale

**Formula:**
```
Imponibile fiscale = Imponibile contributivo - Contributi INPS
```

**Esempio:**
```
Imponibile contributivo: € 2.558,50
Contributi INPS: € 235,13

Imponibile fiscale: € 2.558,50 - € 235,13 = € 2.323,37
```

### 4.2 Scaglioni IRPEF 2024

| Scaglione | Aliquota |
|-----------|----------|
| Fino a € 28.000 | 23% |
| € 28.001 - € 50.000 | 35% |
| Oltre € 50.000 | 43% |

**Calcolo IRPEF lorda (mensilizzata):**
```
Imponibile mensile: € 2.323,37
Imponibile annuo: € 2.323,37 × 12 = € 27.880,44

IRPEF annua: € 27.880,44 × 23% = € 6.412,50
IRPEF mensile: € 6.412,50 / 12 = € 534,38
```

### 4.3 Detrazioni da Lavoro Dipendente

**Formula:**
```
Detrazione annua = 1.955 × (28.000 + reddito - reddito) / 28.000
```

**Per redditi < € 15.000:**
```
Detrazione = 1.955 × (28.000 - reddito) / 28.000
```

**Esempio:**
```
Reddito annuo: € 27.880,44

Detrazione annua: 1.955 × (28.000 - 27.880,44) / 28.000
                = 1.955 × 0,0043 = € 8,41

Detrazione mensile: € 8,41 / 12 = € 0,70
```

**Nota:** Per redditi tra € 15.000 e € 28.000, la detrazione diminuisce progressivamente.

### 4.4 IRPEF Netta

**Formula:**
```
IRPEF netta = IRPEF lorda - Detrazioni
```

**Esempio:**
```
IRPEF lorda: € 534,38
Detrazioni: € 0,70

IRPEF netta: € 534,38 - € 0,70 = € 533,68
```

---

## 5. Addizionali

### 5.1 Addizionale Regionale

**Aliquote 2024 (esempio Lombardia):**

| Scaglione | Aliquota |
|-----------|----------|
| Fino a € 15.000 | 1,23% |
| € 15.001 - € 28.000 | 2,04% |
| € 28.001 - € 50.000 | 2,71% |

**Calcolo:**
```
Imponibile fiscale: € 2.323,37 (mensile)
Imponibile annuo: € 27.880,44

Addizionale regionale: € 27.880,44 × 2,04% = € 568,76
Addizionale mensile: € 568,76 / 12 = € 47,40
```

### 5.2 Addizionale Comunale

**Aliquote:** Variabili per comune (di norma 0,8-1,2%)

**Esempio (Milano 1,03%):**
```
Addizionale comunale: € 27.880,44 × 1,03% = € 287,17
Addizionale mensile: € 287,17 / 12 = € 23,93
```

---

## 6. Contributi Previdenza Complementare

### 6.1 Fondo Pensione

**Contributo dipendente:**
- Di norma 1-2% della retribuzione
- Facoltativo (se aderente al fondo)

**Contributo datore:**
- Di norma 1-2% (se previsto CCNL)
- Non trattenuto al dipendente

**Esempio:**
```
Retribuzione imponibile: € 2.558,50
Aliquota dipendente: 2%

Contributo dipendente: € 2.558,50 × 2% = € 51,17
```

---

## 7. Esempio Completo di Cedolino

### 7.1 Dati Dipendente

```
Dipendente: Mario Rossi
CCNL: Metalmeccanico Industria
Livello: C1
Mese: Gennaio 2024
Anzianità: 6 anni
```

### 7.2 Sezione Retributiva

```
COMPETENZE LORDE:

Retribuzione base:              € 2.050,00
Contingenza:                       € 52,00
MCI:                              € 128,00
Scatti anzianità (3 × € 61,50):   € 184,50
Straordinari:                     € 144,00
Trasferta (5 gg):                 € 225,00
TFR maturando:                    € 185,19
-------------------------------------------
TOTALE LORDO:                   € 2.968,69
```

### 7.3 Sezione Contributi

```
TRATTENUTE PREVIDENZIALI:

Imponibile INPS:                € 2.558,50
Contributi INPS (9.19%):          € 235,13
Contributo fondo pensione (2%):    € 51,17
-------------------------------------------
TOTALE PREVIDENZIALI:             € 286,30
```

### 7.4 Sezione Fiscale

```
TRATTENUTE FISCALI:

Imponibile fiscale:             € 2.323,37
IRPEF lorda:                      € 534,38
Detrazioni lavoro:                   € 0,70
IRPEF netta:                      € 533,68
Addizionale regionale:             € 47,40
Addizionale comunale:              € 23,93
-------------------------------------------
TOTALE FISCALI:                   € 605,01
```

### 7.5 Netto da Pagare

```
CALCOLO NETTO:

Totale lordo:                   € 2.968,69
Totale previdenziali:             € 286,30
Totale fiscali:                   € 605,01
-------------------------------------------
NETTO DA PAGARE:                € 2.077,38
```

---

## 8. Voci Straordinarie

### 8.1 13ª Mensilità

**Maturazione:**
- 1/12 della retribuzione annua per mese
- Maturata da gennaio a dicembre

**Esempio:**
```
Retribuzione mensile: € 2.050,00
13ª mensilità: € 2.050,00 (dicembre)
```

**Trattamento fiscale:**
- Tassazione separata
- Non cumulata con retribuzione ordinaria

### 8.2 14ª Mensilità

**Settori con 14ª:**
- Commercio (alcuni livelli)
- Turismo (alcune categorie)

**Calcolo:**
- Stesso principio della 13ª
- Maturata da gennaio a giugno

### 8.3 Ferie e Permessi Non Goduti

**Indennità sostitutiva:**
- Retribuzione + contingenza + MCI
- Contributi e fiscali come retribuzione ordinaria

**Esempio:**
```
Giorni di ferie non goduti: 5
Retribuzione giornaliera: € 102,50

Indennità ferie: € 102,50 × 5 = € 512,50
```

---

## 9. Controlli di Quadratura

### 9.1 Verifiche Obbligatorie

**Prima di emettere il cedolino:**

1. **Quadratura lordo-trattenute:**
   ```
   Totale lordo - Totale trattenute = Netto
   ```

2. **Verifica imponibili:**
   - Imponibile INPS = Imponibile fiscale + Contributi INPS
   - Controllare esenzioni

3. **Verifica aliquote:**
   - Confermare aliquote INPS aggiornate
   - Confermare scaglioni IRPEF

4. **Verifica detrazioni:**
   - Calcolo corretto in base al reddito
   - Considerare detrazioni familiari a carico

### 9.2 Errori Comuni

| Errore | Correzione |
|--------|------------|
| Imponibile INPS ≠ Imponibile fiscale + contributi | Ricalcolare imponibili |
| Detrazioni non proporzionate | Verificare formula detrazioni |
| Addizionali con aliquote errate | Aggiornare aliquote regionali/comunali |
| TFR non rivalutato | Applicare coefficiente ISTAT |

---

## 10. Riferimenti Operativi

### 10.1 Codici Voci Cedolino

**Codici standard:**

| Codice | Descrizione |
|--------|-------------|
| 001 | Retribuzione base |
| 010 | Contingenza |
| 011 | MCI |
| 020 | Scatti anzianità |
| 030 | Straordinari |
| 040 | Indennità trasferta |
| 100 | Contributi INPS |
| 200 | IRPEF |
| 210 | Addizionale regionale |
| 220 | Addizionale comunale |
| 300 | TFR maturando |

### 10.2 Scadenze

| Adempimento | Scadenza |
|-------------|----------|
| Emissione cedolino | Fine mese o secondo CCNL |
| Pagamento stipendio | Entro il 10 del mese successivo |
| Versamento contributi | 16 del mese successivo |
| Invio UNIEMENS | 15 del mese successivo |

---

**Nota:** Questa guida è aggiornata al gennaio 2024. Verificare sempre le circolari INPS e i CCNL più recenti per aggiornamenti normativi e tabellari.
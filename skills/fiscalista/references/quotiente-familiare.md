---
title: Quoziente Familiare e Detrazioni Carichi di Famiglia
skill: fiscalista
version: 0.2.0
last_updated: 2025-08-05
---

# Quoziente Familiare e Detrazioni Carichi di Famiglia

Questa guida descrive il meccanismo del quoziente familiare e le detrazioni per carichi di famiglia secondo il TUIR.

## 1. Base Normativa

**Articolo 12, DPR 917/1986 (TUIR)**: detrazioni per carichi di famiglia.

**Articolo 13, DPR 917/1986 (TUIR)**: detrazioni per coniuge e familiari a carico.

**D.M. 30/12/2023**: aggiornamento importi detrazioni 2024-2025.

## 2. Quoziente Familiare — Meccanismo

Il **quoziente familiare** è un meccanismo che tiene conto dei carichi di famiglia nel calcolo delle imposte. Non è una detrazione diretta, ma influisce sulle detrazioni spettanti.

### 2.1 Quote per Componente Familiare

| Componente | Quote |
|------------|-------|
| Contribuente | 1 quota |
| Coniuge non separato | 1 quota |
| Ogni figlio | 3/4 di quota |
| Altri familiari a carico | 1/2 quota |

**Formula quoziente**:
```
Quoziente familiare = 1 (contribuente) + 1 (coniuge) + (0,75 × n. figli) + (0,5 × altri familiari)
```

**Esempio**: coppia con 2 figli
```
Quoziente = 1 + 1 + (0,75 × 2) = 1 + 1 + 1,5 = 3,5 quote
```

### 2.2 Applicazione Pratica

Il quoziente familiare **non si applica direttamente** al calcolo IRPEF dal 2024, ma determina:
1. Le detrazioni per carichi di famiglia
2. L'accesso a benefici sociali (ISEE, assegni familiari, ecc.)

## 3. Detrazioni per Coniuge a Carico

**Articolo 13, comma 1, lettera b, TUIR**:

### 3.1 Requisiti

- Coniuge non separato legalmente
- Reddito proprio ≤ 2.840,51 € (per detrazione massima)
- Convivenza effettiva

### 3.2 Importo Detrazione

| Reddito coniuge | Detrazione annua |
|-----------------|------------------|
| ≤ 2.840,51 € | 800 € |
| 2.840,52 € — 30.000 € | 800 × (30.000 − reddito) / 27.159,49 |
| > 30.000 € | 0 € |

**Esempio 1**: coniuge con reddito 1.500 €
```
Detrazione = 800 € (reddito ≤ 2.840,51 €)
```

**Esempio 2**: coniuge con reddito 15.000 €
```
Detrazione = 800 × (30.000 − 15.000) / 27.159,49
           = 800 × 15.000 / 27.159,49
           = 441,83 €
```

**Esempio 3**: coniuge con reddito 35.000 €
```
Detrazione = 0 € (reddito > 30.000 €)
```

## 4. Detrazioni per Figli a Carico

**Articolo 12, TUIR** (come modificato da L. 207/2018 e L. 213/2023):

### 4.1 Requisiti

- Figli legittimi, adottivi, affidati, o naturali
- Età < 18 anni (senza limite di età se disabili)
- Reddito proprio ≤ 2.840,51 €
- Convivenza effettiva (salvo studenti universitari fuori sede)

### 4.2 Importo Base per Fascia d'Età

| Fascia d'età | Detrazione base |
|--------------|-----------------|
| < 3 anni | 1.220 € |
| 3 — 10 anni | 950 € |
| 10 — 18 anni | 950 € |
| > 18 anni | 950 € |

### 4.3 Riduzione per Reddito del Genitore

**Formula**:
```
Se reddito genitore ≤ 25.000 €:
  Detrazione = Detrazione base + (25.000 − reddito) × 0,1

Se 25.000 € < reddito ≤ 50.000 €:
  Detrazione = Detrazione base × (50.000 − reddito) / 50.000

Se reddito > 50.000 €:
  Detrazione = 0 €
```

**Esempio 1**: figlio di 5 anni, genitore con reddito 20.000 €
```
Detrazione base: 950 €
Aumento: (25.000 − 20.000) × 0,1 = 500 €
Detrazione totale: 950 + 500 = 1.450 €
```

**Esempio 2**: figlio di 12 anni, genitore con reddito 35.000 €
```
Detrazione base: 950 €
Detrazione effettiva: 950 × (50.000 − 35.000) / 50.000
                     = 950 × 15.000 / 50.000
                     = 285 €
```

**Esempio 3**: figlio di 15 anni, genitore con reddito 55.000 €
```
Detrazione = 0 € (reddito > 50.000 €)
```

### 4.4 Maggiore Detrazione per Figli < 3 Anni

Per figli di età inferiore a 3 anni:
```
Detrazione = 1.220 € + (25.000 − reddito) × 0,1 (se reddito < 25.000 €)
```

**Esempio**: figlio di 2 anni, genitore con reddito 18.000 €
```
Detrazione base: 1.220 €
Aumento: (25.000 − 18.000) × 0,1 = 700 €
Detrazione totale: 1.220 + 700 = 1.920 €
```

## 5. Detrazioni per Altri Familiari a Carico

**Articolo 13, comma 1, lettera c, TUIR**:

### 5.1 Requisiti

- Genitori, figli, fratelli/sorelle, altri parenti entro il 3° grado
- Reddito proprio ≤ 2.840,51 €
- Convivenza effettiva (salvo eccezioni)

### 5.2 Importo Detrazione

| Reddito familiare | Detrazione annua |
|-------------------|------------------|
| ≤ 2.840,51 € | 700 € |
| 2.840,52 € — 30.000 € | 700 × (30.000 − reddito) / 27.159,49 |
| > 30.000 € | 0 € |

**Esempio**: padre a carico con reddito 2.000 €
```
Detrazione = 700 € (reddito ≤ 2.840,51 €)
```

**Esempio**: sorella a carico con reddito 10.000 €
```
Detrazione = 700 × (30.000 − 10.000) / 27.159,49
           = 700 × 20.000 / 27.159,49
           = 515,48 €
```

## 6. Maggiore Detrazione per Famiglie Numerose

**Legge di Bilancio 2024 (L. 213/2023)**:

### 6.1 Detrazione Aggiuntiva per 3+ Figli

| Numero figli | Detrazione aggiuntiva |
|--------------|----------------------|
| 3 figli | 200 € per ogni figlio |
| 4 figli | 400 € per ogni figlio |
| 5+ figli | 600 € per ogni figlio |

**Esempio**: famiglia con 4 figli, reddito 30.000 €
```
Detrazione base per ogni figlio (950 €): 950 × (50.000 − 30.000) / 50.000 = 380 €
Detrazione aggiuntiva: 400 € per ogni figlio
Totale per figlio: 380 + 400 = 780 €
Totale 4 figli: 780 × 4 = 3.120 €
```

## 7. Assegno Unico e Universale (AUU)

**D.L. 41/2021** (convertito in L. 65/2021):

L'Assegno Unico e Universale sostituisce le precedenti detrazioni per figli.

### 7.1 Importi AUU 2025

| Fascia ISEE | Importo mensile per figlio |
|-------------|---------------------------|
| ISEE ≤ 17.000 € | 175 € |
| ISEE 17.001 — 40.000 € | 75 — 175 € (progressivo) |
| ISEE > 40.000 € | 50 € |

**Figli < 1 anno**: +25 €
**Figli > 18 anni**: 50 € (indipendentemente dall'ISEE)

### 7.2 Relazione con Detrazioni IRPEF

L'AUU è **compatibile** con le detrazioni IRPEF per figli a carico. Si ricevono entrambi.

## 8. Calcolo Pratico — Esempio Completo

**Scenario**: Mario Rossi, reddito 35.000 €, coniuge senza reddito, 3 figli (2, 7, 14 anni).

### Step 1: Detrazioni lavoro dipendente
```
Detrazione lavoro = 1.910 × (50.000 − 35.000) / 35.000 = 818,57 €
```

### Step 2: Detrazione coniuge
```
Detrazione coniuge = 800 € (reddito coniuge = 0 €)
```

### Step 3: Detrazioni figli

**Figlio 1 (2 anni)**:
```
Detrazione base: 1.220 €
Aumento per reddito < 25.000 €: (25.000 − 35.000) < 0 → nessun aumento
Detrazione effettiva: 1.220 × (50.000 − 35.000) / 50.000 = 366 €
```

**Figlio 2 (7 anni)**:
```
Detrazione base: 950 €
Detrazione effettiva: 950 × (50.000 − 35.000) / 50.000 = 285 €
```

**Figlio 3 (14 anni)**:
```
Detrazione base: 950 €
Detrazione effettiva: 950 × (50.000 − 35.000) / 50.000 = 285 €
```

**Totale figli**: 366 + 285 + 285 = 936 €

### Step 4: Detrazione per famiglie numerose (3 figli)
```
Detrazione aggiuntiva: 200 € × 3 figli = 600 €
```

### Step 5: Totale detrazioni carichi famiglia
```
Totale = 800 (coniuge) + 936 (figli) + 600 (famiglia numerosa) = 2.336 €
```

## 9. Checklist per Verifica

Prima di calcolare le detrazioni per carichi di famiglia:

- [ ] Verificare reddito di ogni familiare a carico
- [ ] Verificare età dei figli (per detrazione base corretta)
- [ ] Verificare convivenza effettiva
- [ ] Calcolare detrazione con formula progressiva corretta
- [ ] Verificare diritto a detrazione aggiuntiva per famiglie numerose
- [ ] Ricordare: AUU è compatibile con detrazioni IRPEF

## 10. Riferimenti Normativi

- **DPR 917/1986 (TUIR)**: Art. 12, Art. 13
- **L. 207/2018**: Riforma detrazioni figli
- **L. 213/2023**: Legge di Bilancio 2024
- **D.L. 41/2021**: Assegno Unico e Universale
- **D.M. 30/12/2023**: Aggiornamento importi detrazioni
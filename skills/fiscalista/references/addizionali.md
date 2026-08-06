---
title: Addizionali Regionali e Comunali IRPEF
skill: fiscalista
version: 0.2.0
last_updated: 2025-08-05
---

# Addizionali Regionali e Comunali IRPEF

Questa guida descrive il calcolo delle addizionali regionali e comunali IRPEF secondo il TUIR e il federalismo fiscale.

## 1. Base Normativa

**Articolo 13-ter, DPR 917/1986 (TUIR)**: addizionale regionale IRPEF.

**Articolo 13-quater, DPR 917/1986 (TUIR)**: addizionale comunale IRPEF.

**D.Lgs. 504/1992**: istituzione addizionale comunale.

**L. 42/2006**: federalismo fiscale.

**L. 23/2014**: autonomia tributaria regioni e comuni.

## 2. Addizionale Regionale IRPEF

### 2.1 Natura e Caratteristiche

L'addizionale regionale IRPEF è un'imposta **regionale** che si applica **sull'intero IRPEF lordo**. Non è un'addizionale proporzionale, ma segue scaglioni simili all'IRPEF.

**Caratteristiche**:
- Aliquote variabili per regione
- Base imponibile: IRPEF lorda (prima delle detrazioni)
- Nessuna deduzione specifica
- Scaglioni progressivi

### 2.2 Scaglioni e Aliquote Tipiche

Le regioni hanno autonomia nell'definire le aliquote entro un range. Range tipico 2025:

| Scaglione reddito | Aliquota minima | Aliquota massima |
|-------------------|-----------------|------------------|
| Fino a 15.000 € | 1,23% | 1,73% |
| 15.001 — 28.000 € | 2,25% | 2,75% |
| 28.001 — 50.000 € | 3,33% | 3,83% |
| 50.001 — 75.000 € | 4,33% | 4,83% |
| 75.001 — 120.000 € | 4,73% | 5,23% |
| Oltre 120.000 € | 5,13% | 5,63% |

### 2.3 Aliquote Regionali 2025 — Esempi

**Lombardia**:
| Scaglione | Aliquota |
|-----------|----------|
| Fino a 15.000 € | 1,23% |
| 15.001 — 28.000 € | 2,25% |
| 28.001 — 50.000 € | 3,33% |
| 50.001 — 75.000 € | 4,33% |
| 75.001 — 120.000 € | 4,73% |
| Oltre 120.000 € | 5,13% |

**Lazio**:
| Scaglione | Aliquota |
|-----------|----------|
| Fino a 15.000 € | 1,23% |
| 15.001 — 28.000 € | 2,25% |
| 28.001 — 50.000 € | 3,33% |
| 50.001 — 75.000 € | 4,33% |
| 75.001 — 120.000 € | 4,73% |
| Oltre 120.000 € | 5,13% |

**Campania**:
| Scaglione | Aliquota |
|-----------|----------|
| Fino a 15.000 € | 1,73% |
| 15.001 — 28.000 € | 2,75% |
| 28.001 — 50.000 € | 3,83% |
| 50.001 — 75.000 € | 4,83% |
| 75.001 — 120.000 € | 5,23% |
| Oltre 120.000 € | 5,63% |

**Sicilia**:
| Scaglione | Aliquota |
|-----------|----------|
| Fino a 15.000 € | 1,73% |
| 15.001 — 28.000 € | 2,75% |
| 28.001 — 50.000 € | 3,83% |
| 50.001 — 75.000 € | 4,83% |
| 75.001 — 120.000 € | 5,23% |
| Oltre 120.000 € | 5,63% |

**Piemonte**:
| Scaglione | Aliquota |
|-----------|----------|
| Fino a 15.000 € | 1,23% |
| 15.001 — 28.000 € | 2,33% |
| 28.001 — 50.000 € | 3,33% |
| 50.001 — 75.000 € | 4,33% |
| 75.001 — 120.000 € | 4,73% |
| Oltre 120.000 € | 5,13% |

**Veneto**:
| Scaglione | Aliquota |
|-----------|----------|
| Fino a 15.000 € | 1,23% |
| 15.001 — 28.000 € | 2,25% |
| 28.001 — 50.000 € | 3,33% |
| 50.001 — 75.000 € | 4,33% |
| 75.001 — 120.000 € | 4,73% |
| Oltre 120.000 € | 5,13% |

### 2.4 Calcolo Addizionale Regionale

**Formula**:
```
Addizionale regionale = Σ (aliquota_regionale_i × (min(reddito, massimo_i) − minimo_i))
```

**Esempio**: reddito 45.000 €, residente in Lombardia
```
Primo scaglione (0-15.000 €): 15.000 × 1,23% = 184,50 €
Secondo scaglione (15.001-28.000 €): 13.000 × 2,25% = 292,50 €
Terzo scaglione (28.001-45.000 €): 17.000 × 3,33% = 566,10 €
Addizionale regionale: 184,50 + 292,50 + 566,10 = 1.043,10 €
```

**Nota importante**: l'addizionale regionale si applica sul **reddito imponibile IRPEF**, non sull'IRPEF lorda come alcuni pensono.

## 3. Addizionale Comunale IRPEF

### 3.1 Natura e Caratteristiche

L'addizionale comunale IRPEF è un'imposta **comunale** che si applica con aliquota unica sul reddito imponibile.

**Caratteristiche**:
- Aliquota massima 0,9% (alcuni comuni 0,8%)
- Base imponibile: reddito imponibile IRPEF − 7.000 € (deduzione per lavoro dipendente/pensione)
- Aliquota unica (non scaglioni)
- Variabile per comune

### 3.2 Aliquote Comunali 2025 — Esempi

| Comune | Aliquota 2025 |
|--------|---------------|
| Milano | 0,8% |
| Roma | 0,8% |
| Napoli | 0,75% |
| Torino | 0,7% |
| Bologna | 0,65% |
| Firenze | 0,7% |
| Genova | 0,7% |
| Bari | 0,7% |
| Catania | 0,7% |
| Venezia | 0,7% |
| Verona | 0,6% |
| Padova | 0,6% |

**Nota**: le aliquote comunali possono variare annualmente. Verificare sempre sul sito del comune di residenza.

### 3.3 Calcolo Addizionale Comunale

**Formula**:
```
Base imponibile comunale = Reddito imponibile IRPEF − 7.000 € (se lavoro dipendente/pensione)
Addizionale comunale = Base imponibile comunale × Aliquota comunale
```

**Esempio**: reddito 45.000 €, residente a Milano
```
Base imponibile: 45.000 − 7.000 = 38.000 €
Addizionale comunale: 38.000 × 0,8% = 304 €
```

**Esempio**: reddito 45.000 €, residente a Roma (lavoratore autonomo, nessuna deduzione)
```
Base imponibile: 45.000 € (nessuna deduzione per lavoro autonomo)
Addizionale comunale: 45.000 × 0,8% = 360 €
```

## 4. Esempio Completo: Addizionali Regionali + Comunali

**Scenario**: Mario Rossi, reddito 45.000 €, lavoratore dipendente, residente a Milano (Lombardia).

### Step 1: Addizionale regionale (Lombardia)
```
Primo scaglione (0-15.000 €): 15.000 × 1,23% = 184,50 €
Secondo scaglione (15.001-28.000 €): 13.000 × 2,25% = 292,50 €
Terzo scaglione (28.001-45.000 €): 17.000 × 3,33% = 566,10 €
Addizionale regionale: 184,50 + 292,50 + 566,10 = 1.043,10 €
```

### Step 2: Addizionale comunale (Milano)
```
Base imponibile: 45.000 − 7.000 = 38.000 €
Aliquota Milano: 0,8%
Addizionale comunale: 38.000 × 0,8% = 304 €
```

### Step 3: Totale addizionali
```
Totale addizionali: 1.043,10 + 304 = 1.347,10 €
```

## 5. Confronto: Addizionali per Regione

**Scenario comparativo**: reddito 45.000 €, lavoratore dipendente, stesso comune (ipotetico 0,8%).

| Regione | Addizionale regionale | Addizionale comunale | Totale |
|---------|----------------------|---------------------|--------|
| Lombardia | 1.043,10 € | 304 € | 1.347,10 € |
| Lazio | 1.043,10 € | 304 € | 1.347,10 € |
| Campania | 1.233,10 € | 304 € | 1.537,10 € |
| Sicilia | 1.233,10 € | 304 € | 1.537,10 € |
| Piemonte | 1.056,10 € | 304 € | 1.360,10 € |
| Veneto | 1.043,10 € | 304 € | 1.347,10 € |

**Differenza massima**: 190 € tra regioni con aliquote minime e massime.

## 6. Casi Particolari

### 6.1 Reddito < 8.500 € (No-Tax-Area)

Se il reddito è inferiore a 8.500 €:
- **Addizionale regionale**: dovuta (nessuna esenzione)
- **Addizionale comunale**: dovuta (nessuna esenzione)

**Esempio**: reddito 7.000 €, Lombardia, Milano
```
Addizionale regionale: 7.000 × 1,23% = 86,10 €
Addizionale comunale: (7.000 − 7.000) × 0,8% = 0 €
Totale: 86,10 €
```

### 6.2 Lavoro Autonomo

Per lavoro autonomo:
- **Addizionale regionale**: stessa formula
- **Addizionale comunale**: base imponibile = reddito (nessuna deduzione di 7.000 €)

**Esempio**: reddito 45.000 €, professionista, Lombardia, Milano
```
Addizionale regionale: 1.043,10 € (come lavoro dipendente)
Addizionale comunale: 45.000 × 0,8% = 360 € (nessuna deduzione)
Totale: 1.403,10 €
```

### 6.3 Pensionati

Per pensionati:
- Stessa deduzione di 7.000 € per addizionale comunale
- Stessi scaglioni regionali

## 7. Versamento Addizionali

### 7.1 Modalità di Versamento

Le addizionali si versano tramite:
- **F24** (sezione ERARIO)
- **Modello Redditi PF** (acconto e saldo)

### 7.2 Scadenze

| Versamento | Scadenza | Descrizione |
|------------|----------|-------------|
| Saldo addizionali anno precedente | 30 novembre | Saldo IRPEF + addizionali |
| 1° acconto addizionali anno corrente | 16 giugno | 40% dell'acconto |
| 2° acconto addizionali anno corrente | 30 novembre | 60% dell'acconto |

### 7.3 Codici Tributo F24

| Tributo | Codice | Descrizione |
|---------|--------|-------------|
| Addizionale regionale | 4100 | Addizionale IRPEF regionale |
| Addizionale comunale | 4200 | Addizionale IRPEF comunale |

## 8. Checklist per Calcolo

Prima di calcolare le addizionali:

- [ ] Verificare regione di residenza (per addizionale regionale)
- [ ] Verificare comune di residenza (per addizionale comunale)
- [ ] Consultare aliquote regionali 2025 specifiche
- [ ] Consultare aliquota comunale 2025 specifica
- [ ] Verificare tipo di reddito (lavoro dipendente → deduzione 7.000 €)
- [ ] Calcolare addizionale regionale scaglione per scaglione
- [ ] Calcolare addizionale comunale con aliquota unica
- [ ] Sommare addizionali regionali + comunali

## 9. Riferimenti Normativi

- **DPR 917/1986 (TUIR)**: Art. 13-ter, Art. 13-quater
- **D.Lgs. 504/1992**: Addizionale comunale
- **L. 42/2006**: Federalismo fiscale
- **L. 23/2014**: Autonomia tributaria
- **Delibere regionali annuali**: aliquote regionali specifiche
- **Delibere comunali annuali**: aliquote comunali specifiche
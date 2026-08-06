---
title: Meccanismo di Calcolo IRPEF
skill: fiscalista
version: 0.2.0
last_updated: 2025-08-05
---

# Meccanismo di Calcolo IRPEF

Questa guida descrive il meccanismo completo di calcolo dell'IRPEF (Imposta sul Reddito delle Persone Fisiche) secondo il TUIR (DPR 917/1986).

## 1. Base Normativa

**Articolo 11, DPR 917/1986 (TUIR)**: definisce i redditi imponibili.

**Articolo 67, DPR 917/1986 (TUIR)**: definisce le componenti positive e negative del reddito.

**Articolo 12, DPR 917/1986 (TUIR)**: definisce il reddito complessivo.

**Articolo 13, DPR 917/1986 (TUIR)**: definisce le detrazioni d'imposta.

**Articolo 14, DPR 917/1986 (TUIR)**: definisce le deduzioni dal reddito.

## 2. Sequenza di Calcolo

Il calcolo dell'IRPEF segue questa sequenza rigorosa:

```
1. Reddito imponibile (per categoria)
   ↓
2. Reddito complessivo (somma di tutti i redditi)
   ↓
3. Reddito imponibile IRPEF (dopo deduzioni)
   ↓
4. Imposta lorda (applicazione scaglioni)
   ↓
5. Detrazioni (lavoro, pensione, carichi famiglia, oneri)
   ↓
6. Imposta netta
   ↓
7. Addizionali regionali e comunali
   ↓
8. Imposta finale
```

## 3. Reddito Imponibile per Categoria

### 3.1 Redditi di Lavoro Dipendente (Art. 49 TUIR)

**Componenti positive**:
- Stipendi e salari
- Indennità e compensi
- TFR (Trattamento di Fine Rapporto)
- Benefit in natura
- Premi e provvigioni

**Deduzioni**:
- Contributi previdenziali obbligatori (INPS, INPDAP, ecc.)
- Contributi assistenziali

**Formula**:
```
Reddito lavoro dipendente = Reddito lordo − Contributi previdenziali
```

### 3.2 Redditi di Pensione (Art. 50 TUIR)

**Componenti positive**:
- Pensioni di vecchiaia
- Pensioni di anzianità
- Pensioni di invalidità
- Assegni sociali

**Deduzioni**:
- Contributi previdenziali (se applicabili)

**Formula**:
```
Reddito pensione = Reddito lordo − Contributi (se presenti)
```

### 3.3 Redditi di Lavoro Autonomo (Art. 53 TUIR)

**Componenti positive**:
- Compensi professionali
- Provvigioni
- Onorari

**Deduzioni**:
- Costi di produzione del reddito
- Contributi previdenziali (INPS, casse professionali)
- Spese generali (affitto studio, utenze, ecc.)

**Formula (regime ordinario)**:
```
Reddito lavoro autonomo = Ricavi − Costi deducibili − Contributi INPS
```

**Formula (regime forfettario)**:
```
Reddito imponibile = Ricavi × Coefficiente redditività
Imposta = Reddito imponibile × 15% (o 5%)
```

### 3.4 Redditi di Capitale (Art. 44 TUIR)

**Componenti positive**:
- Dividendi
- Interessi su conti correnti
- Interessi su obbligazioni
- Rendite finanziarie

**Tassazione**:
- **26%**: dividendi, interessi su conti, obbligazioni corporate
- **12,5%**: titoli di stato "white list" (BTP, BOT, titoli UE)

**Formula**:
```
Imposta = Reddito di capitale × Aliquota (26% o 12,5%)
```

### 3.5 Redditi Fondiari (Art. 32 TUIR)

**Componenti positive**:
- Redditi dominicali (proprietà)
- Redditi agrari (attività agricola)

**Calcolo BFC (Reddito Dominicale)**:
```
BFC = Rendita catastale × 1,05 (abitazioni) o × 1,5 (box)
```

**Nota**: per immobili locati, si applica il canone di locazione, non il BFC.

### 3.6 Redditi Diversi (Art. 67 TUIR)

**Componenti positive**:
- Plusvalenze da cessione di partecipazioni
- Plusvalenze da cessione di strumenti finanziari
- Plusvalenze da cessione di immobili (se non abitazione principale)
- Plusvalenze crypto

**Tassazione**:
- **26%**: plusvalenze finanziarie, crypto
- **26%**: plusvalenze immobiliari (se vendita entro 5 anni dall'acquisto)

**Formula**:
```
Plusvalenza = Prezzo vendita − Prezzo acquisto (costo storico)
Imposta = Plusvalenza × 26%
```

## 4. Reddito Complessivo

**Articolo 12, TUIR**:

```
Reddito complessivo = Σ (redditi lavoro dipendente + redditi pensione + redditi lavoro autonomo + redditi capitale + redditi fondiari + redditi diversi)
```

**Attenzione**: alcuni redditi sono esenti o tassati separatamente:
- Cedolare secca (non concorre al reddito complessivo)
- Tassazione separata (TFR, alcune indennità)

## 5. Deduzioni dal Reddito

**Articolo 14, TUIR**: le deduzioni riducono il reddito imponibile.

**Principali deduzioni**:
- Contributi previdenziali e assistenziali (art. 10, comma 1, lettera f)
- Spese mediche (parzialmente, art. 15, comma 1, lettera c)
- Premi assicurativi (art. 10, comma 1, lettera g)
- Interessi passivi mutuo prima casa (art. 15, comma 1, lettera b)
- Contributi PER (Piani Individuali di Risparmio) (art. 10, comma 1, lettera f-bis)

**Formula**:
```
Reddito imponibile IRPEF = Reddito complessivo − Deduzioni totali
```

## 6. Scaglioni IRPEF 2025

**Articolo 11, TUIR** (come modificato da L. 213/2023):

| Scaglione | Aliquota | Imposta cumulativa |
|-----------|----------|-------------------|
| 0 — 28.000 € | 23% | 0 — 6.440 € |
| 28.001 — 50.000 € | 35% | 6.440 — 14.140 € |
| Oltre 50.000 € | 43% | > 14.140 € |

**Calcolo imposta lorda**:
```
Se reddito ≤ 28.000 €:
  Imposta lorda = Reddito × 23%

Se 28.000 € < reddito ≤ 50.000 €:
  Imposta lorda = (28.000 × 23%) + ((reddito − 28.000) × 35%)
                = 6.440 + ((reddito − 28.000) × 35%)

Se reddito > 50.000 €:
  Imposta lorda = (28.000 × 23%) + (22.000 × 35%) + ((reddito − 50.000) × 43%)
                = 6.440 + 7.700 + ((reddito − 50.000) × 43%)
                = 14.140 + ((reddito − 50.000) × 43%)
```

**Esempio**: reddito 45.000 €
```
Imposta lorda = 6.440 + ((45.000 − 28.000) × 35%)
              = 6.440 + (17.000 × 35%)
              = 6.440 + 5.950
              = 12.390 €
```

## 7. Detrazioni d'Imposta

**Articolo 13, TUIR**: le detrazioni riducono l'imposta lorda.

### 7.1 Detrazioni per Lavoro Dipendente

**Formula progressiva**:
```
Se reddito ≤ 15.000 €:
  Detrazione = 1.910 €

Se 15.000 € < reddito ≤ 28.000 €:
  Detrazione = 1.910 × (50.000 − reddito) / 35.000

Se 28.000 € < reddito ≤ 50.000 €:
  Detrazione = 600 × (50.000 − reddito) / 22.000

Se reddito > 50.000 €:
  Detrazione = 0 €
```

**Esempio**: reddito 35.000 €
```
Detrazione = 1.910 × (50.000 − 35.000) / 35.000
           = 1.910 × 15.000 / 35.000
           = 818,57 €
```

### 7.2 Detrazioni per Coniuge a Carico

**Articolo 13, comma 1, lettera b, TUIR**:

| Reddito coniuge | Detrazione |
|-----------------|------------|
| ≤ 2.840,51 € | 800 € |
| 2.840,51 € — 30.000 € | 800 × (30.000 − reddito coniuge) / 27.159,49 |
| > 30.000 € | 0 € |

### 7.3 Detrazioni per Figli a Carico

**Articolo 12, TUIR** (modificato da L. 207/2018):

| Età figlio | Detrazione base |
|------------|-----------------|
| < 3 anni | 1.220 € |
| 3 — 10 anni | 950 € |
| 10 — 18 anni | 950 € |
| > 18 anni | 950 € |

**Riduzione per reddito**:
```
Detrazione effettiva = Detrazione base × (50.000 − reddito complessivo) / 50.000
```

**Aumento per reddito < 25.000 €**:
```
Detrazione aumentata = Detrazione base + (25.000 − reddito) × 0,1
```

### 7.4 Detrazioni per Altri Familiari a Carico

**Articolo 13, comma 1, lettera c, TUIR**:

| Reddito familiare | Detrazione |
|-------------------|------------|
| ≤ 2.840,51 € | 700 € |
| 2.840,51 € — 30.000 € | 700 × (30.000 − reddito) / 27.159,49 |
| > 30.000 € | 0 € |

### 7.5 Detrazioni per Oneri Deducibili

**Articolo 15, TUIR**:

| Oneri | Detrazione |
|-------|------------|
| Spese mediche | 19% sopra franchigia 129,11 € |
| Spese dentistiche | 19% sopra franchigia 129,11 € |
| Spese veterinarie | 19% sopra franchigia 129,11 € |
| Spese scolastiche | 19% (massimo 800 € per figlio) |
| Spese universitarie | 19% (massimo 800 € per studente) |
| Interessi mutuo prima casa | 19% (massimo 4.000 € annui) |
| Spese ristrutturazione | 50% (massimo 96.000 € per unità immobiliare) |
| Spese efficienza energetica | 50-65% (varia per intervento) |
| Spese assicurative | 19% (massimo 530 €) |

## 8. No-Tax-Area

**Legge di Bilancio 2024 (L. 213/2023)**:

**Soglia**: 8.500 € per lavoratori dipendenti e pensionati.

**Meccanismo**:
```
Se reddito ≤ 8.500 €:
  Imposta netta = 0 € (la detrazione copre interamente l'imposta)

Se 8.500 € < reddito ≤ 15.000 €:
  Detrazione = 1.910 € (massima)
  Imposta netta = Imposta lorda − 1.910 €

Se reddito > 15.000 €:
  Detrazione si riduce progressivamente (vedi §7.1)
```

## 9. Imposta Netta

**Formula finale**:
```
Imposta netta = Imposta lorda − Detrazioni totali

Se imposta netta < 0:
  Imposta netta = 0 € (no tax area)
```

## 10. Esempio Completo

**Scenario**: Mario Rossi, lavoratore dipendente, reddito 35.000 €, coniuge a carico (reddito 0 €), 2 figli (5 e 12 anni), spese mediche 1.500 €.

**Step 1: Reddito complessivo**
```
Reddito lavoro dipendente: 35.000 €
Reddito complessivo: 35.000 €
```

**Step 2: Imposta lorda**
```
Imposta lorda = 6.440 + ((35.000 − 28.000) × 35%)
              = 6.440 + 2.450
              = 8.890 €
```

**Step 3: Detrazioni lavoro dipendente**
```
Detrazione lavoro = 1.910 × (50.000 − 35.000) / 35.000
                  = 818,57 €
```

**Step 4: Detrazioni coniuge**
```
Detrazione coniuge = 800 € (reddito coniuge = 0 € < 2.840,51 €)
```

**Step 5: Detrazioni figli**
```
Figlio 1 (5 anni): 950 €
Figlio 2 (12 anni): 950 €
Totale figli: 1.900 €
```

**Step 6: Detrazioni spese mediche**
```
Spese mediche: 1.500 €
Franchigia: 129,11 €
Spese detraibili: 1.500 − 129,11 = 1.370,89 €
Detrazione: 1.370,89 × 19% = 260,47 €
```

**Step 7: Totale detrazioni**
```
Totale detrazioni = 818,57 + 800 + 1.900 + 260,47 = 3.779,04 €
```

**Step 8: Imposta netta**
```
Imposta netta = 8.890 − 3.779,04 = 5.110,96 €
```

## 11. Riferimenti Normativi

- **DPR 917/1986 (TUIR)**: Testo Unico delle Imposte sui Redditi
- **Art. 11 TUIR**: Scaglioni IRPEF
- **Art. 12 TUIR**: Reddito complessivo
- **Art. 13 TUIR**: Detrazioni per lavoro dipendente, coniuge, familiari
- **Art. 14 TUIR**: Deduzioni dal reddito
- **Art. 15 TUIR**: Detrazioni per oneri
- **L. 213/2023**: Legge di Bilancio 2024 (riforma IRPEF)
---
title: Redditi di Capitale — Tassazione
skill: fiscalista
version: 0.2.0
last_updated: 2025-08-05
---

# Redditi di Capitale — Tassazione

Questa guida descrive la tassazione dei redditi di capitale secondo il TUIR.

## 1. Base Normativa

**Articolo 44, DPR 917/1986 (TUIR)**: definizione redditi di capitale.

**Articolo 47, DPR 917/1986 (TUIR)**: componenti positive.

**Articolo 26, D.P.R. 600/1973**: ritenute alla fonte.

## 2. Tipologie di Redditi di Capitale

### 2.1 Dividendi

**Definizione**: utili distribuiti da società di capitali (S.p.A., S.r.l., ecc.).

**Aliquota**: 26%

**Meccanismo**:
```
Imposta = Dividendi lordi × 26%
Dividendi netti = Dividendi lordi − Imposta
```

**Esempio**: dividendi 5.000 €
```
Imposta: 5.000 × 26% = 1.300 €
Dividendi netti: 5.000 − 1.300 = 3.700 €
```

### 2.2 Interessi su Conti Correnti e Depositi

**Definizione**: interessi attivi su conti correnti bancari e postali, conti deposito.

**Aliquota**: 26%

**Meccanismo**:
```
Imposta = Interessi lordi × 26%
```

**Esempio**: interessi conto deposito 2.000 €
```
Imposta: 2.000 × 26% = 520 €
Interessi netti: 2.000 − 520 = 1.480 €
```

### 2.3 Interessi su Obbligazioni

**Definizione**: cedole su obbligazioni corporate e titoli di stato.

**Aliquote**:
- **26%**: obbligazioni corporate (emesse da società)
- **12,5%**: titoli di stato "white list" (BTP, BOT, CCT, titoli UE)

**Esempio 1**: cedole BTP 3.000 €
```
Imposta: 3.000 × 12,5% = 375 €
```

**Esempio 2**: cedole obbligazione corporate 3.000 €
```
Imposta: 3.000 × 26% = 780 €
```

### 2.4 Rendite Finanziarie

**Definizione**: rendite da contratti di assicurazione sulla vita, rendite vitalizie finanziarie.

**Aliquota**: 26%

## 3. Tassazione alla Fonte

### 3.1 Soggetti Sostituti d'Imposta

Le imposte sui redditi di capitale sono generalmente **tassate alla fonte** tramite ritenuta:

- **Banche**: per conti correnti, depositi, prodotti bancari
- **Intermediari finanziari**: per azioni, obbligazioni, ETF
- **Società**: per dividendi

### 3.2 Meccanismo Ritenuta

```
Reddito lordo: 10.000 €
Ritenuta 26%: 2.600 €
Reddito netto accreditato: 7.400 €
```

**Nota**: la ritenuta è definitiva per persone fisiche residenti in Italia. Non occorre dichiarare questi redditi nel Modello Redditi (sono già tassati).

## 4. Quadro RM — Dichiarazione

### 4.1 Quando Compilare il Quadro RM

Il Quadro RM va compilato per:
- Redditi di capitale **non soggetti a ritenuta definitiva**
- Redditi di capitale da **soggetti esteri**
- Opzione per **tassazione progressiva** (barème) invece del PFU

### 4.2 Struttura Quadro RM

| Riga | Descrizione |
|------|-------------|
| RM1 | Redditi di capitale soggetti a ritenuta |
| RM2 | Redditi di capitale esenti |
| RM3 | Redditi di capitale tassati con aliquota diversa |
| RM4 | Imposta dovuta |

## 5. Opzione per Tassazione Progressiva (Barème)

### 5.1 Quando Conviene

L'opzione per la tassazione progressiva (invece del PFU 26%) può convenire se:
- TMI IRPEF < 26% (reddito complessivo < 28.000 €)
- Si vogliono sfruttare detrazioni per oneri

### 5.2 Meccanismo

```
Reddito di capitale: 10.000 €
Aggiunto al reddito complessivo
Tassato con aliquote IRPEF (23%, 35%, 43%)
CSG deducibile: 6,8% (solo se opzione barème)
```

**Esempio**: reddito complessivo 20.000 €, dividendi 5.000 €
```
Senza opzione (PFU): 5.000 × 26% = 1.300 €
Con opzione (barème):
  Reddito complessivo: 20.000 + 5.000 = 25.000 €
  Imposta su 25.000 €: 25.000 × 23% = 5.750 €
  Imposta su 20.000 €: 20.000 × 23% = 4.600 €
  Imposta aggiuntiva: 5.750 − 4.600 = 1.150 €
  Con CSG deducibile: 1.150 × (1 − 6,8%) = 1.071,80 €
Convenienza: 1.300 − 1.071,80 = 228,20 € di risparmio
```

### 5.3 Regola dell'Opzione Globale

L'opzione per il barème è **globale**: una volta scelta, si applica a **tutti** i redditi di capitale dell'anno. Non si può scegliere prodotto per prodotto.

## 6. Redditi di Capitale da Estero

### 6.1 Tassazione

I redditi di capitale da estero sono tassati in Italia con le stesse aliquote (26% o 12,5%).

**Meccanismo**:
```
Reddito estero lordo: 10.000 €
Ritenuta estera: 1.500 € (15%)
Reddito imponibile in Italia: 10.000 €
Imposta Italia: 10.000 × 26% = 2.600 €
Credito d'imposta: 1.500 € (ritenuta estera)
Imposta da versare in Italia: 2.600 − 1.500 = 1.100 €
```

### 6.2 Convenzioni contro le Doppie Imposizioni

Le convenzioni bilaterali possono ridurre la ritenuta alla fonte all'estero. Verificare la convenzione specifica con il paese estero.

## 7. Esempi Pratici

### 7.1 Esempio 1: Portafoglio Diversificato

**Scenario**: Mario Rossi ha nel 2025:
- Dividendi azioni italiane: 5.000 €
- Interessi conto deposito: 2.000 €
- Cedole BTP: 3.000 €
- Cedole obbligazione corporate: 2.000 €

**Calcolo**:
```
Dividendi (26%): 5.000 × 26% = 1.300 €
Interessi conto (26%): 2.000 × 26% = 520 €
Cedole BTP (12,5%): 3.000 × 12,5% = 375 €
Cedole corporate (26%): 2.000 × 26% = 520 €
Totale imposte: 1.300 + 520 + 375 + 520 = 2.715 €
```

### 7.2 Esempio 2: Opzione Barème

**Scenario**: Maria Bianchi, reddito lavoro 22.000 €, dividendi 8.000 €.

**Opzione PFU**:
```
Imposta dividendi: 8.000 × 26% = 2.080 €
Imposta lavoro: 22.000 × 23% = 5.060 €
Detrazioni lavoro: 1.910 × (50.000 − 22.000) / 35.000 = 1.528 €
Imposta netta lavoro: 5.060 − 1.528 = 3.532 €
Totale: 2.080 + 3.532 = 5.612 €
```

**Opzione Barème**:
```
Reddito complessivo: 22.000 + 8.000 = 30.000 €
Imposta su 30.000 €:
  28.000 × 23% = 6.440 €
  2.000 × 35% = 700 €
  Totale: 7.140 €
Detrazioni lavoro: 1.910 × (50.000 − 30.000) / 35.000 = 1.091 €
Imposta netta: 7.140 − 1.091 = 6.049 €
Convenienza: 6.049 − 5.612 = 437 € di svantaggio
```

**Conclusione**: in questo caso, il PFU è più conveniente.

## 8. Checklist

- [ ] Identificare tipologia di reddito di capitale
- [ ] Applicare aliquota corretta (26% o 12,5%)
- [ ] Verificare se ritenuta è già stata operata
- [ ] Valutare opzione barème se TMI < 26%
- [ ] Compilare Quadro RM solo se necessario
- [ ] Verificare convenzioni contro doppie imposizioni per redditi esteri

## 9. Riferimenti Normativi

- **DPR 917/1986 (TUIR)**: Art. 44, Art. 47
- **D.P.R. 600/1973**: Art. 26 (ritenute)
- **D.L. 21/2024**: Tassazione crypto (se applicabile)
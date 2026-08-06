# Imposte Dirette — IRES, IRAP e Addizionali

**Base normativa**: DPR 917/1986 (TUIR), D.Lgs. 446/1997 (IRAP).

## IRES — Imposta sul Reddito delle Società

### Aliquota e Base Imponibile

| Parametro | Valore | Base Legale |
|-----------|--------|-------------|
| **Aliquota IRES** | 24% | Art. 5 D.Lgs. 284/2004 |
| **Soggetti passivi** | Società di capitali, enti commerciali | Art. 73 TUIR |
| **Periodo d'imposta** | Anno solare (salvo esercizio diverso) | Art. 7 TUIR |

### Calcolo dell'Imponibile IRES

**Formula**:
```
Reddito d'esercizio (CE)
+ Variazioni in aumento (spese non deducibili)
- Variazioni in diminuzione (entrate non imponibili)
= Reddito imponibile IRES

Reddito imponibile × 24% = IRES dovuta
```

### Variazioni in Aumento (Non Deducibili)

| Voce | Percentuale non deducibile | Base Legale |
|------|---------------------------|-------------|
| **Ritenute non versate** | 100% | Art. 100 TUIR |
| **Sanzioni amministrative** | 100% | Art. 100 TUIR |
| **Oneri e donazioni** | 100% (salvo eccezioni) | Art. 100 TUIR |
| **Spese di rappresentanza** | 5% fino a 10.000€, poi 100% | Art. 108 TUIR |
| **Interessi eccedenti** | Parte eccedente thin capitalization | Art. 96 TUIR |
| **Plusvalenze da cessione partecipazioni** | 95% non imponibile (5% imponibile) | Art. 87 TUIR |

### Variazioni in Diminuzione (Non Imponibili)

| Voce | Percentuale non imponibile | Base Legale |
|------|---------------------------|-------------|
| **Dividendi da partecipazioni** | 95% (PEx regime) | Art. 89 TUIR |
| **Plusvalenze partecipazioni** | 95% (PEx regime) | Art. 87 TUIR |
| **Rimanenze** | Variazione di competenza | Art. 88 TUIR |

### Esempio di Calcolo IRES

```
Reddito d'esercizio (utile bilancio civile): 100.000€
+ Spese di rappresentanza (15.000€): 10.000€ (non deducibile)
+ Sanzioni versate (2.000€): 2.000€ (non deducibile)
- Dividendi ricevuti (10.000€): 9.500€ (non imponibile)
= Reddito imponibile IRES: 102.500€

IRES dovuta: 102.500 × 24% = 24.600€
```

**Scrittura di assestamento**:
```
6.05.006 Imposte IRES         24.600,00
  5.04.005 Debiti IRES                    24.600,00
```

### Acconti IRES

**Regola**:
- 1° acconto: 30 giugno (40% dell'acconto)
- 2° acconto: 30 novembre (60% dell'acconto)

**Calcolo acconto**:
```
IRES N-1 × 103% = Base acconto
Base acconto - Saldo N-1 = Totale acconto N
```

**Scrittura acconto**:
```
5.04.005 Debiti IRES           10.000,00
  3.04.003 Banca                        10.000,00
```

## IRAP — Imposta Regionale sulle Attività Produttive

### Aliquote Regionali (2026)

| Regione | Aliquota Base | Aliquota Effettiva |
|---------|---------------|-------------------|
| **Lazio** | 3,90% | 4,45% |
| **Lombardia** | 3,90% | 4,07% |
| **Campania** | 3,90% | 4,65% |
| **Sicilia** | 3,90% | 4,65% |
| **Piemonte** | 3,90% | 4,12% |
| **Veneto** | 3,90% | 4,20% |
| **Emilia-Romagna** | 3,90% | 4,21% |
| **Toscana** | 3,90% | 4,26% |
| **P.A. Bolzano** | 3,90% | 3,90% |
| **P.A. Trento** | 3,90% | 4,15% |
| **Sardegna** | 3,90% | 4,45% |

**Aliquota speciale**:
- **4,90%** per attività bancaria e finanziaria
- **2,43%** per attività di trasporto

### Base Imponibile IRAP

**Formula generale**:
```
Valore della produzione netto
- Costi deducibili
= Base imponibile IRAP

Base imponibile × Aliquota regionale = IRAP dovuta
```

**Componenti positivi** (Art. 5 D.Lgs. 446/97):
- Ricavi delle vendite e delle prestazioni di servizi
- Variazione delle rimanenze
- Proventi da partecipazioni
- Altri proventi e ricavi

**Componenti negativi deducibili** (Art. 6 D.Lgs. 446/97):
- Costi per beni e servizi
- Canoni di locazione e affitto
- Oneri assicurativi
- Ammortamenti
- Provvigioni

**Costi NON deducibili**:
- **Costi per il personale** (salari, stipendi, TFR, contributi)
- **Partecipazioni in altre società**
- **Interessi passivi** (parzialmente deducibili)
- **Utili da partecipazione** (PEx)

### Esempio di Calcolo IRAP

```
Ricavi vendite: 500.000€
+ Variazione rimanenze: 10.000€
+ Altri ricavi: 20.000€
= Valore produzione lordo: 530.000€

- Costi per materie: 200.000€
- Costi per servizi: 150.000€
- Ammortamenti: 30.000€
- Affitti: 40.000€
= Costi deducibili: 420.000€

Base imponibile IRAP: 530.000 - 420.000 = 110.000€

IRAP dovuta (Lazio 4,45%): 110.000 × 4,45% = 4.895€
```

**Scrittura di assestamento**:
```
6.05.006 Imposte IRAP          4.895,00
  5.04.006 Debiti IRAP                    4.895,00
```

### Acconti IRAP

**Regola**:
- 1° acconto: 16 giugno (40%)
- 2° acconto: 30 novembre (60%)

**Calcolo**:
```
IRAP N-1 × 101% = Base acconto
```

## Addizionali Comunali IRPEF

**Applicabile a**: ditte individuali e società di persone (IRPEF)

### Range Addizionali Comunali

| Comune | Aliquota | Base Legale |
|--------|----------|-------------|
| Roma | 0,80% | Delibera comunale |
| Milano | 0,70% | Delibera comunale |
| Napoli | 0,90% | Delibera comunale |
| Torino | 0,75% | Delibera comunale |
| Altri comuni | 0,20% - 1,20% | Variabile |

**Calcolo**:
```
Reddito imponibile IRPEF × Aliquota comunale = Addizionale
```

## Detrazioni e Agevolazioni

### Detrazione per Investimenti (Art. 1 D.L. 104/2023)

**Nuovi investimenti in beni strumentali**:
- **40%** per beni materiali nuovi
- **20%** per beni immateriali nuovi
- **10%** per investimenti in ricerca e sviluppo

### Zona Franca Urbana (ZFU)

**Aree svantaggiate**:
- **Esenzione IRES** per 5 anni
- **Esenzione IRAP** per 5 anni
- Requisiti: assunzione personale, investimenti minimi

### Aree Svantaggiate (D.L. 91/2017)

**Agevolazioni per investimenti al Sud**:
- **Credit d'imposta 40%** per investimenti in beni strumentali
- **Credit d'imposta 50%** per assunzioni a tempo indeterminato

## Scadenze

| Imposta | Saldo | 1° Acconto | 2° Acconto |
|---------|-------|------------|------------|
| **IRES** | 1 luglio | 30 giugno | 30 novembre |
| **IRAP** | 1 luglio | 16 giugno | 30 novembre |
| **IRPEF** (ditte) | 1 luglio | 16 giugno | 30 novembre |

## Scritture di Chiusura

### Stima Imposte Completa

```
Calcolo totale imposte:
- IRES: 24.600€
- IRAP: 4.895€
= Totale imposte: 29.495€

Scrittura:
6.05.006 Imposte IRES/IRAP    29.495,00
  5.04.005 Debiti IRES                    24.600,00
  5.04.006 Debiti IRAP                     4.895,00
```

### Imposte Differite e Attive

**Imposte differite (Differite attive)**:
- Quando costo civilistico > costo fiscale
- Diritto a deduzione futura

**Imposte attive (Differite passive)**:
- Quando ricavo civilistico < ricavo fiscale
- Obbligo di tassazione futura

**Scrittura**:
```
Imposte differite:
29.03 Imposte differite attive    X
  7.03.001 Recupero imposte differite      X

Imposte attive:
6.05.006 Imposte correnti         X
  29.04 Imposte attive passive             X
```

## Note Operative

1. **Modello Redditi**: Dichiarazione IRES/IRAP si presenta con Modello Redditi PF (ditte individuali) o Modello Redditi Società

2. **Scadenza dichiarazione**: 30 novembre (telematica) per l'esercizio precedente

3. **Versamento saldo**: Entro il 1 luglio (o 30 giugno con bonifico)

4. **Ravvedimento operoso**: In caso di ritardo, applicare sanzione ridotta (Art. 13 D.Lgs. 472/97)

5. **Addizionali regionali IRPEF**: Variabile per regione (0,8% - 1,03%), verificare per regione di residenza
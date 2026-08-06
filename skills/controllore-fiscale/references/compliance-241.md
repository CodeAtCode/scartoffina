---
title: Compliance Fiscale - Studi di Settore (D.Lgs. 241/1997)
description: Studi di settore, parametri, GERICO, adeguamento spontaneo
skill: controllore-fiscale
version: 0.2.0
updated: 2026-08-06
---

# Compliance Fiscale - Studi di Settore e Parametri

Strumenti di controllo fiscale basati su stime di ricavi/compensi presunti.

## 1. Base Legale

- **D.Lgs. 9 luglio 1997, n. 241** — Norme di coordinamento in materia di adempimenti fiscali
- **Art. 10-bis L. 212/2000** — Adeguamento agli studi di settore
- **D.M. 23 marzo 1999** — Approvazione studi di settore (e successive modificazioni)

## 2. Studi di Settore

### 2.1 Definizione
Modelli statistici che stimano ricavi/compensi presunti per categoria di attività (codice ATECO).

### 2.2 Struttura
- Questionario anagrafico (dati strutturali)
- Questionario economico (ricavi, costi, addetti)
- Algoritmo di stima (regressioni, cluster analysis)

### 2.3 Software
GERICO (Gestione Studi di Settore), disponibile su https://www.agenziaentrate.gov.it.

## 3. Applicazione

### 3.1 Soggetti
Persone fisiche, società di persone, società di capitali in contabilità semplificata.

### 3.2 Esclusioni
- Società quotate
- Amministrazioni pubbliche
- Soggetti in contabilità ordinaria con ricavi > 5.164.569 euro
- Contribuenti minimi e forfettari

### 3.3 Periodo d'Imposta
Applicazione per il periodo d'imposta in corso al 31 dicembre.

## 4. Esiti dello Studio

### 4.1 Regolare
Contribuente "in regola" con gli studi di settore. Nessun adeguamento richiesto.

### 4.2 Non Regolare
Contribuente "fuori range". Adeguamento spontaneo possibile.

### 4.3 Non Classificato
Contribuente non classificabile (dati anomali).

### 4.4 Non Rilevante
Attività non coperta da studi di settore.

## 5. Adeguamento Spontaneo

### 5.1 Termine
Entro il termine di presentazione della dichiarazione relativa al periodo d'imposta successivo.

### 5.2 Riduzione Sanzioni
Adeguamento spontaneo: **1/3 del minimo** (anziché 100-200%).

### 5.3 Calcolo
```
Ricavi dichiarati:        50.000 €
Ricavi stimati:           65.000 €
Maggiori ricavi:          15.000 €
Imposta (23%):              3.450 €
Sanzione ridotta (1/3):      345 € (1/3 del 1.035)
Interessi:                    86 € (2,5%)
Totale adeguamento:        3.881 €
```

## 6. Parametri

### 6.1 Definizione
Coefficiente di redditività minima per categoria merceologica (simile agli studi di settore ma per più categorie).

### 6.2 Applicazione
Per attività non coperte da studi di settore o in caso di fallimento degli studi.

### 6.3 Adeguamento
Stessa procedura degli studi di settore.

## 7. Nuovi Studi di settore 2025

### 7.1 Revisione
Aggiornamento periodico di studi di settore (ogni 3-5 anni).

### 7.2 Algoritmi di Apprendimento
Nuovi studi usano algoritmi di machine learning per migliorare la stima.

## 8. Compliance Operativa

### 8.1 Controlli Periodici
1. Esecuzione GERICO ogni anno
2. Verifica coerenza con ricavi dichiarati
3. Adeguamento spontaneo se fuori range
4. Documentazione delle scelte organizzative

### 8.2 Diffida
Notifica di adeguamento spontaneo (art. 10-bis L. 212/2000) con termine di 30 giorni.

## 9. Sanzioni

| Violazione | Sanzione |
|------------|----------|
| Omessa compilazione GERICO | 250-2.000€ |
| Inadeguamento senza giustificazione | 100-200% maggiore imposta |
| Adeguamento spontaneo | 1/3 del minimo (ravvedimento) |

## 10. Riferimenti

- Agenzia delle Entrate (GERICO): https://www.agenziaentrate.gov.it
- Studi di settore: https://www.agenziaentrate.gov.it

## 11. Freschezza dei Dati

Studi di settore aggiornati periodicamente. Verificare su https://www.agenziaentrate.gov.it.

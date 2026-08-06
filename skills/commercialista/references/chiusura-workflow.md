# Chiusura d'Esercizio — Workflow Completo

**Base normativa**: Artt. 2423-2435 c.c., OIC 12 (Bilancio di esercizio), OIC 28 (Ammortamenti), OIC 29 (Ratei e risconti).

## Panoramica del Processo

La chiusura d'esercizio si articola in **12 fasi obbligatorie**:

```
1. Bilancio di verifica preliminare
2. Rimanenze di magazzino
3. Ammortamenti immobilizzazioni
4. Svalutazioni e accantonamenti
5. Ratei e risconti
6. Stima imposte (IRES/IRAP)
7. TFR e benefici dipendenti
8. Verifica crediti e fondo svalutazione
9. Chiusura conti economici
10. Chiusura conti patrimoniali
11. Redazione bilancio
12. Approvazione e deposito
```

## Fase 1: Bilancio di Verifica Preliminare

**Obiettivo**: Verificare la quadratura della contabilità prima delle scritture di assestamento.

**Procedura**:
1. Estrarre tutti i movimenti contabili dal libro giornale
2. Riassumere per conto (mastrino)
3. Verificare: Somma Dare = Somma Avere

**Se non quadrato**:
- Controllare scritture di apertura
- Verificare numerazione consecutiva fatture
- Riconciliare estratti conto bancari
- Esaminare movimenti sospetti

**Output**: Bilancio di verifica con saldi per ogni conto.

## Fase 2: Rimanenze di Magazzino

**Obiettivo**: Determinare il valore delle rimanenze finali.

**Metodi di valutazione** (Art. 2426 c.c., OIC 13):
- **FIFO** (First In, First Out) — consigliato
- **LIFO** (Last In, First Out) — non conforme OIC
- **Costo medio ponderato** — alternativo
- **Costo specifico** — per beni unici

**Principio di prudenza**:
- Valutare al **minore tra costo e valore di realizzo**
- Se valore di realizzo < costo → svalutazione

**Scrittura di variazione rimanenze**:

```
Rimanenze finali > Rimanenze iniziali:
15.01 Rimanenze magazzino         X
  70.01 Variazione rimanenze           X

Rimanenze finali < Rimanenze iniziali:
60.01 Variazione rimanenze        X
  15.01 Rimanenze magazzino            X
```

**Output**: Valore rimanenze finali da inserire nello Stato Patrimoniale (Attivo circolante).

## Fase 3: Ammortamenti Immobilizzazioni

**Obiettivo**: Ripartire il costo delle immobilizzazioni lungo la loro vita utile.

### Coefficienti di Ammortamento (DM 31/12/1988)

| Categoria | Aliquota minima | Aliquota massima |
|-----------|-----------------|------------------|
| **Impianti e macchinari** | 10% | 20% |
| **Attrezzature industriali** | 15% | 25% |
| **Mobili e macchinari d'ufficio** | 15% | 25% |
| **Mezzi di trasporto** | 20% | 25% |
| **Impianti informatici** | 33% | 50% |
| **Strumenti musicali** | 20% | 25% |
| **Attrezzature sportive** | 20% | 25% |
| **Altre immobilizzazioni materiali** | 10% | 20% |
| **Concessioni, licenze, marchi** | 10% | 20% |
| **Software** | 33% | 50% |

### Half-Year Convention (Primo Anno)

**Regola**: Per le immobilizzazioni acquistate durante l'esercizio, applicare **50%** del coefficiente nel primo anno.

**Esempio**:
```
Macchinario acquistato 01/06/2026: costo 100.000€
Coefficiente: 15%
Ammortamento 2026 (half-year): 100.000 × 15% × 50% = 7.500€
Ammortamento 2027: 100.000 × 15% = 15.000€
```

### Scrittura di Ammortamento

```
6.04.001 Ammortamento [tipo]      X
  28.01 Fondo ammortamento [tipo]      X
```

**Output**:
- Quota di ammortamento nel Conto Economico (costo)
- Fondo ammortamento nello Stato Patrimoniale (valore netto = costo - fondo)

## Fase 4: Svalutazioni e Accantonamenti

### Svalutazione Crediti

**Obiettivo**: Riconoscere il rischio di insolvenza dei clienti.

**Metodi**:
- **Analisi specifica**: per ogni credito di importo significativo
- **Percentuale storica**: basato su insolvenze passate (tipico 1-5%)
- **Metodo misto**: specifico per grandi crediti + percentuale per il resto

**Scrittura**:
```
6.04.004 Svalutazione crediti     X
  5.01.001 Fondo svalutazione crediti     X
```

### Accantonamento per Rischi

**Tipologie**:
- **Fondo garanzie**: per garanzie concesse su prodotti
- **Fondo cause legali**: per contenziosi in corso
- **Fondo ordini in corso**: per ordini con perdita prevista

**Scrittura**:
```
6.05.005 Accantonamento rischi    X
  5.01.002 Fondo rischi                  X
```

### Svalutazione Rimanenze

**Quando**: Se valore di realizzo < costo storico

**Scrittura**:
```
6.04.005 Svalutazione rimanenze   X
  15.02 Fondo svalutazione rimanenze     X
```

## Fase 5: Ratei e Risconti

**Obiettivo**: Separare costi e ricavi di competenza dell'esercizio da quelli di esercizi successivi.

### Tipologie

| Tipo | Natura | Esemplificazione |
|------|--------|------------------|
| **Rateo attivo** | Ricavo maturato non fatturato | Interessi attivi maturati a dicembre |
| **Risconto attivo** | Costo pagato per competenza futura | Assicurazione pagata dicembre per 12 mesi |
| **Rateo passivo** | Costo maturato non fatturato | Interessi passivi maturati a dicembre |
| **Risconto passivo** | Ricavo incassato per competenza futura | Canone di affitto anticipato |

### Calcolo

**Formula generale**:
```
Importo totale × (Giorni competenza / Giorni totali) = Rateo/Risconto
```

**Esempio 1 — Rateo attivo (interessi bancari)**:
```
Interessi annuali: 1.200€
Giorni maturati dicembre: 31
Giorni anno: 365
Rateo attivo: 1.200 × (31/365) = 102€

Scrittura:
3.02.011 Ratei attivi              102,00
  7.02.001 Interessi attivi              102,00
```

**Esempio 2 — Risconto attivo (assicurazione)**:
```
Assicurazione pagata 01/12/2026: 12.000€ (per 12 mesi)
Competenza 2026: 1 mese = 1.000€
Risconto per 2027: 11 mesi = 11.000€

Scrittura:
15.01 Risconti attivi           11.000,00
  63.02 Assicurazioni                     11.000,00
```

**Esempio 3 — Rateo passivo (interessi bancari)**:
```
Interessi passivi maturati dicembre: 500€

Scrittura:
66.01 Interessi passivi            500,00
  18.01 Ratei passivi                      500,00
```

**Esempio 4 — Risconto passivo (affitto anticipato)**:
```
Affitto incassato 01/10/2026: 12.000€ (per 12 mesi)
Competenza 2026: 3 mesi = 3.000€
Risconto per 2027: 9 mesi = 9.000€

Scrittura:
40.01 Clienti c/acconti         12.000,00
  70.01 Ricavi affitto                     3.000,00
  5.05.002 Risconti passivi                9.000,00
```

## Fase 6: Stima Imposte (IRES/IRAP)

**Obiettivo**: Determinare l'onere fiscale sull'utile d'esercizio.

**Procedura**:
1. Calcolare il reddito imponibile civilistico
2. Applicare variazioni fiscali (IRES)
3. Calcolare IRES (24%)
4. Calcolare IRAP (aliquota regionale)
5. Registrare le imposte

**Scrittura**:
```
6.05.006 Imposte IRES/IRAP       29.495,00
  5.04.005 Debiti IRES                    24.600,00
  5.04.006 Debiti IRAP                     4.895,00
```

## Fase 7: TFR e Benefici Dipendenti

### Accantonamento TFR

**Formula**:
```
Retribuzione annua lorda × 6,91% = TFR maturando
```

**Aggiornamento**:
- **Crescita retributiva**: 1,5% + 75% dell'inflazione ISTAT
- **Aggiornamento annuale** obbligatorio

**Scrittura**:
```
6.03.003 TFR maturando           14.820,00
  5.01.005 Fondo TFR                      14.820,00
```

### Contributi Previdenziali

**Verifica**: Accertare che tutti i contributi INPS/INAIL siano stati registrati e versati.

## Fase 8: Verifica Crediti e Fondo Svalutazione

**Procedura**:
1. Estrarre anagrafica crediti per età
2. Identificare crediti scaduti > 90 giorni
3. Applicare percentuali di svalutazione:
   - 0-90 giorni: 1%
   - 91-180 giorni: 5%
   - 181-365 giorni: 20%
   - > 365 giorni: 50-100%

**Scrittura**:
```
6.04.004 Svalutazione crediti     5.000,00
  5.01.001 Fondo svalutazione crediti      5.000,00
```

## Fase 9: Chiusura Conti Economici

**Obiettivo**: Determinare l'utile/perdita d'esercizio.

**Procedura**:
1. Chiudere tutti i conti di costo (classe 6) al Conto 990
2. Chiudere tutti i conti di ricavo (classe 7) al Conto 990
3. Il saldo del Conto 990 è l'utile/perdita

**Scritture**:

```
Chiusura costi:
990.01 Conto economico chiusura   X
  6.01.001 Acquisti merci                  X
  6.02.001 Servizi                        X
  ...

Chiusura ricavi:
70.01.001 Ricavi vendite          X
  990.01 Conto economico chiusura          X

Saldo Conto 990:
- Se Dare > Avere: Perdita
- Se Avere > Dare: Utile
```

## Fase 10: Chiusura Conti Patrimoniali

**Obiettivo**: Preparare l'apertura del nuovo esercizio.

**Procedura**:
1. Chiudere tutti i conti patrimoniali (classi 1-5) al Conto 990
2. Aprire i nuovi conti con saldi rovesciati

**Scrittura di chiusura**:
```
990.02 Stato patrimoniale chiusura  X
  3.04.003 Banca                         X
  4.01.001 Capitale sociale              X
  ...
```

**Scrittura di apertura (nuovo esercizio)**:
```
3.04.003 Banca                     X
4.01.001 Capitale sociale          X
...
  990.02 Stato patrimoniale apertura     X
```

## Fase 11: Redazione Bilancio

**Documenti obbligatori** (Art. 2423 c.c.):

1. **Stato Patrimoniale** (OIC 28)
2. **Conto Economico** (OIC 28)
3. **Nota Integrativa** (OIC 29)
4. **Rendiconto finanziario** (opzionale per PMI, OIC 34)

### Schema Stato Patrimoniale

```
ATTIVO
A. Crediti verso soci
B. Immobilizzazioni
   I. Immateriali
   II. Materiali
   III. Finanziarie
C. Attivo circolante
   I. Rimanenze
   II. Crediti
   III. Strumenti finanziari
   IV. Disponibilità liquide
D. Ratei e risconti attivi

PASSIVO
A. Patrimonio netto
B. Fondi per rischi e oneri
C. Debiti
   I. Verso banche
   II. Verso fornitori
   III. Tributari
   IV. Previdenziali
D. Ratei e risconti passivi
```

### Schema Conto Economico

```
A. Valore della produzione
   1. Ricavi vendite
   2. Variazione rimanenze
   3. Altri ricavi
B. Costi della produzione
   4. Per materie
   5. Per servizi
   6. Per il personale
   7. Ammortamenti
   8. Oneri diversi
= Risultato operativo (EBIT)
C. Proventi e oneri finanziari
= Risultato prima delle imposte
D. Imposte
= Utile/Perdita d'esercizio
```

## Fase 12: Approvazione e Deposito

**Scadenze**:
- **Chiusura bilancio**: entro 120 giorni dalla fine esercizio (Art. 2364 c.c.)
- **Approvazione**: Assemblea soci entro 180 giorni
- **Deposito**: presso Registro Imprese entro 30 giorni dall'approvazione

**Documenti da depositare**:
1. Stato Patrimoniale
2. Conto Economico
3. Nota Integrativa
4. Relazione sulla gestione (amministratori)
5. Relazione sulla revisione (se obbligatorio)

## Checklist di Chiusura

```
□ Bilancio di verifica preliminare quadrato
□ Rimanenze valutate e registrate
□ Ammortamenti calcolati e registrati
□ Svalutazioni crediti applicate
□ Accantonamenti rischi effettuati
□ Ratei e risconti calcolati
□ Stima imposte IRES/IRAP registrata
□ TFR accantonato
□ Conti economici chiusi
□ Conti patrimoniali chiusi
□ Bilancio redatto (SP + CE + NI)
□ Bilancio approvato dai soci
□ Bilancio depositato al Registro Imprese
```

## Note Operative

1. **Tempi**: Iniziare la chiusura almeno 60 giorni prima della scadenza

2. **Revisione**: Obbligatoria se superate 2 su 3 soglie (Art. 2477 c.c.):
   - Totale attivo: 4.400.000€
   - Ricavi: 8.800.000€
   - Dipendenti medi: 50

3. **Bilancio abbreviato**: Possibile se superate 1 su 2 soglie:
   - Totale attivo: 2.200.000€
   - Ricavi: 4.400.000€

4. **Micro-imprese**: Bilancio super-semplificato se:
   - Totale attivo: 440.000€
   - Ricavi: 880.000€
   - Dipendenti medi: 10
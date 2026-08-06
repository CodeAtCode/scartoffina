---
title: Liquidazione IVA - Guida Dettagliata
skill: commercialista
version: 0.1.0
last_updated: 2026-01-15
---

# Liquidazione IVA - Guida Dettagliata

Questa guida copre il processo completo di liquidazione IVA, inclusi i casi particolari e le operazioni complesse.

## 1. Fondamenti della Liquidazione IVA

### 1.1 Base normativa

- **D.P.R. 633/1972**: Istituzione e disciplina dell'IVA
- **D.L. 331/1993**: Operazioni intracomunitarie
- **D.M. 28/12/1999**: Modalità di liquidazione

### 1.2 Periodo di liquidazione

| Contribuente | Periodo | Scadenza versamento |
|--------------|---------|---------------------|
| Mensile | Mese solare | 16 del mese successivo |
| Trimestrale | Trimestre solare | 16 del mese successivo al trimestre |
| Opzione mensile | Mese solare (anche se trimestrale di diritto) | 16 del mese successivo |

**Contribuenti mensili obbligatori**:
- Fatturato annuo > 400.000€
- Società controllate/controllo
- Soggetti con obbligo fatturazione elettronica verso PA

**Contribuenti trimestrali di diritto**:
- Fatturato annuo ≤ 400.000€
- Imprese agricole
- Piccoli contribuenti

## 2. Processo di Liquidazione

### 2.1 Fase 1: Raccolta dati

**Registri IVA da consultare**:

1. **Registro vendite** (art. 24 D.P.R. 633/1972)
   - Fatture emesse
   - Corrispettivi
   - Documenti di trasporto

2. **Registro acquisti** (art. 25 D.P.R. 633/1972)
   - Fatture ricevute
   - Autofatture
   - Documenti doganali

**Estratto conto bancario**:
- Verificare pagamenti/ricevimenti correlati a fatture

### 2.2 Fase 2: Classificazione operazioni

**Operazioni imponibili** (IVA ordinaria):
- Aliquota 22%: operazioni standard
- Aliquota 10%: servizi turistici, ristorazione, alcuni alimenti
- Aliquota 5%: alcuni alimenti, prodotti sociali
- Aliquota 4%: beni di prima necessità

**Operazioni non imponibili** (art. 7-7-bis D.P.R. 633/1972):
- Esportazioni (aliquota 0%)
- Operazioni intracomunitarie (aliquota 0%)
- Cessioni di titoli, azioni, obbligazioni
- Assicurazioni

**Operazioni esenti** (art. 10 D.P.R. 633/1972):
- Prestazioni sanitarie
- Servizi educativi
- Servizi finanziari (alcuni)
- Locazioni immobiliari (alcune)

**Operazioni fuori campo IVA** (art. 7 D.P.R. 633/1972):
- Prestazioni di lavoro subordinato
- Attribuzioni di soci
- Cessioni di aziende

### 2.3 Fase 3: Calcolo liquidazione

**Formula base**:
```
IVA a debito (vendite) = Σ(imponibile_i × aliquota_i)
IVA a credito (acquisti) = Σ(imponibile_j × aliquota_j)
Saldo = IVA a debito − IVA a credito
```

**Casi particolari**:

| Situazione | Risultato | Azione |
|------------|-----------|--------|
| Debito > Credito | Saldo positivo | Versamento F24 |
| Credito > Debito | Saldo negativo | Credito da compensare/riportare |
| Debito = Credito | Saldo zero | Nessuna azione |

### 2.4 Fase 4: Compilazione F24

**Codici tributo principali**:

| Codice | Descrizione | Scadenza |
|--------|-------------|----------|
| 1001 | IVA mensile saldo | 16 del mese successivo |
| 1002 | IVA mensile acconto | 16 dicembre / 30 novembre |
| 1004 | IVA prima rata acconto | 16 giugno |
| 1005 | IVA seconda rata acconto | 30 novembre |
| 6001 | IVA trimestrale | 16 del mese successivo al trimestre |

**Esempio F24 per liquidazione mensile**:
```
Sezione ERARIO
Codice tributo: 1001
Anno di riferimento: 2026
Mese di riferimento: 01 (gennaio)
Importo: 1.100,00
```

## 3. Casi Particolari

### 3.1 Reverse Charge (Inversione Contabile)

**Ambito di applicazione** (art. 17 D.P.R. 633/1972):

| Operazione | Aliquota | Chi versa IVA |
|------------|----------|---------------|
| Cessione rottami metallici | 22% | Acquirente |
| Cessione semiconduttori | 22% | Acquirente |
| Cessione telefonia mobile | 22% | Acquirente |
| Cessione beni usati (usato professionale) | 22% | Acquirente |
| Prestazioni edili | 22% | Committente |
| Cessione oro da investimento | 22% | Acquirente |

**Scrittura contabile reverse charge**:
```
Fattura ricevuta per rottami metallici (reverse charge)
Imponibile: 5.000€, IVA: 1.100€

Conto              Dare      Avere
─────────────────────────────────────
10.01 Merci c/acquisti      5.000,00
41.01 IVA a credito           1.100,00
  41.01 IVA a credito                   1.100,00
  (autofattura RC n. RC/2026/001)
```

**Nota**: L'IVA è contemporaneamente a debito e a credito, quindi non incide sulla liquidazione ma deve essere registrata.

### 3.2 Split Payment (Pubblica Amministrazione)

**Ambito di applicazione** (art. 17-ter D.P.R. 633/1972):
- Operazioni con pubbliche amministrazioni
- Appalti pubblici
- Forniture a enti pubblici

**Meccanismo**:
- Il fornitore emette fattura con IVA
- La PA paga l'imponibile al fornitore
- La PA versa l'IVA direttamente all'erario

**Scrittura contabile split payment**:
```
Fattura emessa a Comune di Roma (split payment)
Imponibile: 10.000€, IVA: 2.200€

Conto              Dare      Avere
─────────────────────────────────────
40.01 Comune di Roma        10.000,00
  70.01 Ricavi vendite               10.000,00

Conto              Dare      Avere
─────────────────────────────────────
40.01 Comune di Roma         2.200,00
  41.03 IVA split payment             2.200,00
```

**Nota**: L'IVA split payment non concorre alla liquidazione periodica.

### 3.3 Operazioni Intracomunitarie

**Cessione di beni UE** (art. 41 D.L. 331/1993):
- Aliquota 0% (operazione non imponibile)
- Requisiti:
  - Partita IVA del cliente valida (VIES)
  - Prova di uscita dal territorio italiano
  - Registrazione in Intrastat (se sopra soglia)

**Scrittura**:
```
Cessione a cliente tedesco (operazione intracomunitaria)
Imponibile: 20.000€, IVA: 0%

Conto              Dare      Avere
─────────────────────────────────────
40.01 Cliente Germania        20.000,00
  70.01 Ricavi vendite               20.000,00
  (operazione intracomunitaria art. 41)
```

**Dichiarazione IVA**:
- Quadro VE: cessioni intracomunitarie
- Quadro VL: acquisti intracomunitari

**Prestazione di servizi UE** (art. 7-bis D.P.R. 633/1972):
- Reverse charge: il cliente UE versa l'IVA nel proprio paese
- Registrazione in dichiarazione IVA italiana

### 3.4 Autofatture

**Quando emettere autofattura**:

| Situazione | Riferimento | Note |
|------------|-------------|------|
| Importazioni | Art. 17 D.P.R. 633/1972 | IVA versata alla dogana |
| Acquisti da privati UE | Art. 41 D.L. 331/1993 | Reverse charge |
| Operazioni senza fattura | Art. 6 D.P.R. 633/1972 | Quando il fornitore non fattura |
| Integrazione fattura | Art. 6 D.P.R. 633/1972 | Fattura incompleta |

**Scrittura autofattura importazione**:
```
Importazione merci da Cina
Valore doganale: 10.000€
IVA dogana: 2.200€

Conto              Dare      Avere
─────────────────────────────────────
10.01 Merci c/acquisti      10.000,00
41.01 IVA a credito           2.200,00
  41.01 IVA a credito                   2.200,00
  (autofattura importazione AF/2026/001)
```

## 4. Liquidazione con Credito

### 4.1 Opzioni per il credito IVA

Quando l'IVA a credito supera l'IVA a debito:

1. **Ripporto al periodo successivo** (opzione standard)
   - Il credito si accumula e si compensa nei periodi futuri

2. **Compensazione F24** (art. 31 D.L. 83/2012)
   - Utilizzare il credito per compensare altri tributi
   - Limiti: massimo 5.000€ per periodo senza certificazione

3. **Rimborso** (art. 30 D.P.R. 633/1972)
   - Richiesta di rimborso annuale
   - Controlli preventivi dell'Agenzia delle Entrate

### 4.2 Calcolo compensazione

**Esempio**:
- Credito IVA gennaio: 2.000€
- Debito IVA febbraio: 1.500€
- Altri tributi febbraio (IRES acconto): 3.000€

**Compensazione**:
```
Credito disponibile: 2.000€
Debito IVA febbraio: 1.500€
Saldo dopo compensazione IVA: 500€ (credito residuo)

Compensazione F24 febbraio:
- Codice 1001 (IVA febbraio): 0€ (coperto da credito)
- Codice 1002 (IRES acconto): 1.500€ (parte del credito)
- Versamento netto: 1.500€ (rimanente IRES)
```

## 5. Cessione di Ramo d'Azienda

### 5.1 Regime IVA

**Non imponibilità** (art. 2 D.L. 41/1995):
- Cessione di ramo d'azienda come complesso di beni
- Trasferimento di going concern
- Nessuna IVA dovuta sul trasferimento

**Requisiti**:
- Trasferimento di un'organizzazione di beni organizzati
- Continuazione dell'attività da parte del cessionario
- Comunicazione all'Agenzia delle Entrate

**Scrittura**:
```
Cessione ramo d'azienda a Beta S.r.l.
Valore complessivo: 100.000€

Conto              Dare      Avere
─────────────────────────────────────
40.01 Cliente Beta            100.000,00
  70.01 Ricavi cessione ramo           100.000,00
  (operazione non imponibile art. 2 D.L. 41/1995)
```

### 5.2 Trattamento IVA beni singoli

Se la cessione include beni singoli (non ramo d'azienda):

| Bene | Trattamento IVA |
|------|-----------------|
| Immobilizzazioni materiali | IVA 22% (se detrazione precedente) |
| Merci | IVA 22% |
| Immobilizzazioni immateriali | IVA 22% |

## 6. Errori e Correzioni

### 6.1 Errori comuni in liquidazione

| Errore | Conseguenza | Correzione |
|--------|-------------|------------|
| Dimenticare corrispettivi | Sottodichiarazione | Integrazione con sanzioni |
| Doppia registrazione IVA | Credito errato | Storno scrittura |
| Aliquota errata | Liquidazione sbagliata | Rettifica registro |
| Dimenticare reverse charge | IVA non versata | Autofattura integrativa |

### 6.2 Sanzioni per errori

| Violazione | Sanzione |
|------------|----------|
| Omessa liquidazione | 30% dell'IVA non versata |
| Liquidazione infedele | 30% della differenza |
| Ritardo versamento | 0,4% al giorno (max 30%) |
| Omessa registrazione | 90-180€ per documento |

### 6.3 Ravvedimento operoso

Per correggere errori prima dell'accertamento:

```
Sanzione ridotta:
- Entro 30 giorni: 1/10 della sanzione (3%)
- Entro l'anno: 1/8 della sanzione (3,75%)
- Oltre l'anno: 1/6 della sanzione (5%)

Interessi: 0,1% al giorno (tasso legale)
```

## 7. Scadenze e Adempimenti

### 7.1 Calendario IVA

| Mese | Adempimento | Scadenza |
|------|-------------|----------|
| Mensile | Liquidazione mese precedente | 16 del mese successivo |
| Trimestrale | Liquidazione trimestre precedente | 16 del mese successivo al trimestre |
| Annuale | Dichiarazione IVA | 30 novembre (anno successivo) |
| Annuale | Liquidazione annuale | 30 novembre (anno successivo) |

### 7.2 Comunicazione LiPe

**Obbligo**: Contribuenti trimestrali devono comunicare le liquidazioni periodiche.

**Contenuto**:
- Importo IVA a debito
- Importo IVA a credito
- Saldo versato/credito

**Scadenza**: Entro il 16 del secondo mese successivo al trimestre.

## 8. Checklist di Liquidazione

Prima di finalizzare la liquidazione, verificare:

- [ ] Registro vendite completo (nessuna fattura omessa)
- [ ] Registro acquisti completo (tutte le fatture ricevute)
- [ ] Corrispettivi registrati (cassa e carte di credito)
- [ ] Reverse charge identificato e registrato
- [ ] Split payment identificato ed escluso dalla liquidazione
- [ ] Operazioni intracomunitarie registrate correttamente
- [ ] Autofatture emesse (se necessarie)
- [ ] Quadratura IVA debito/credito
- [ ] Codice tributo F24 corretto
- [ ] Scadenza rispettata (o ravvedimento calcolato)
- [ ] Comunicazione LiPe compilata (se trimestrale)

## 9. Riferimenti Normativi

- **D.P.R. 633/1972**: Istituzione e disciplina dell'IVA
- **D.L. 331/1993**: Operazioni intracomunitarie
- **D.L. 41/1995**: Cessione di ramo d'azienda
- **Art. 30 D.P.R. 633/1972**: Rimborso IVA
- **Art. 31 D.L. 83/2012**: Compensazione tributi
- **D.Lgs. 472/1997**: Sanzioni tributarie
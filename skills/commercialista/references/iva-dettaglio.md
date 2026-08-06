# IVA — Operazioni e Regimi

**Base normativa**: DPR 633/1972, D.L. 331/1993 (operazioni intracomunitarie), Direttive UE.

## Aliquote IVA Attuali (2026)

| Aliquota | Applicazione | Base Legale |
|----------|--------------|-------------|
| **22%** | Tasso ordinario — maggior parte beni e servizi | Art. 10 DPR 633/72 |
| **10%** | Tasso ridotto — ristorazione, trasporti, lavori di ristrutturazione, alcuni prodotti alimentari | Art. 12 DPR 633/72 |
| **5%** | Tasso ridottissimo — alcuni prodotti alimentari, libri, prestazioni sociali | Art. 13 DPR 633/72 |
| **4%** | Tasso minimo — prodotti alimentari di prima necessità, libri scolastici, giornali | Art. 13 DPR 633/72 |
| **0%** | Operazioni esenti con diritto a deduzione (export, intracom) | Art. 8-9 DPR 633/72 |

## Tipologie di Operazioni IVA

### 1. Operazioni Imponibili Ordinarie

**Vendite nazionali (cessioni di beni)**:
- IVA applicata all'aliquota ordinaria o ridotta
- Registrazione nel registro vendite
- Scrittura:
```
40.01 Clienti              1.220,00
  70.01 Ricavi vendite               1.000,00
  41.01 IVA a debito                  220,00
```

**Prestazioni di servizi**:
- Stessa trattazione delle cessioni di beni
- Luogo di prestazione: dove è stabilito il prestatore (regola generale B2B)
- Scrittura identica alle cessioni di beni

### 2. Operazioni Non Imponibili

#### Export (Art. 8 DPR 633/72)

**Condizioni**:
- Bene esportato fuori dall'UE
- Documentazione di esportazione (DUA, lettera di vettura)
- Prova dell'uscita dal territorio UE

**Trattamento**:
- IVA 0%
- Diritto a deduzione dell'IVA sugli acquisti correlati
- Registrazione con codice operazione "E"

**Scrittura**:
```
40.01 Clienti estero         1.000,00
  70.01 Ricavi export                  1.000,00
```

#### Operazioni Intracomunitarie — Cessione Beni (Art. 41 D.L. 331/1993)

**Condizioni**:
- Cliente assoggettato IVA in altro Stato UE
- Numero IVA intracomunitario valido (verifica VIES)
- Trasporto del bene dal territorio italiano
- Soglia annuale: 10.000€ (sotto soglia: IVA paese di origine)

**Trattamento**:
- IVA 0% (esenzione con diritto a deduzione)
- Registrazione in Quadro VE dichiarazione IVA
- Comunicazione Intrastat beni (se sopra soglia)

**Scrittura**:
```
40.01 Clienti intracom       2.000,00
  70.01 Ricavi intracom                2.000,00
```

#### Operazioni Intracomunitarie — Prestazioni Servizi (Art. 7-7quater DPR 633/72)

**Regola generale (B2B)**:
- Luogo di prestazione: Stato del prestatore di servizi
- IVA dovuta nel paese del cliente (reverse charge)
- Autoliquidazione da parte del cliente

**Eccezioni (luogo diverso)**:
- Servizi immobiliari: luogo dell'immobile
- Servizi culturali/artistici/sportivi: luogo esecuzione
- Servizi di ristorazione/alberghieri: luogo prestazione

**Trattamento (reverse charge)**:
- Fattura senza IVA
- Cliente italiano: autofattura con reverse charge
- Registrazione in Quadro VL dichiarazione IVA

**Scrittura (prestazione ricevuta da UE)**:
```
6.02.003 Servizi consulenza    1.000,00
41.02 IVA reverse charge         220,00
  40.01 Fornitori intracom       1.000,00
  41.02 IVA reverse charge         220,00
```
*Nota: IVA a debito e a credito si annullano se diritto a deduzione totale*

### 3. Operazioni Esenti (Art. 10 DPR 633/72)

**Principali categorie esenti**:
- Servizi sanitari e ospedalieri
- Servizi educativi e scolastici
- Servizi finanziari e assicurativi
- Servizi postali
- Locazioni di immobili abitativi
- Giochi d'azzardo e scommesse

**Caratteristiche**:
- **Nessuna IVA** applicata sulla fattura
- **Nessun diritto a deduzione** dell'IVA sugli acquisti correlati
- IVA a credito non recuperabile (va stornata)

**Scrittura con storno IVA**:
```
40.01 Clienti                1.000,00
  70.01 Ricavi esenti                1.000,00

6.02.003 Servizi              1.000,00
  41.01 IVA a credito                  220,00  (storno)
  40.01 Fornitori                      1.220,00
```

### 4. Reverse Charge Nazionale

**Operazioni soggette a reverse charge in Italia**:

| Operazione | Aliquota | Base Legale |
|------------|----------|-------------|
| Cessione rottami metallici | 22% | Art. 17 c.2 DPR 633/72 |
| Cessione telefonia mobile | 22% | Art. 17 c.2 DPR 633/72 |
| Cessione semiconduttori | 22% | Art. 17 c.2 DPR 633/72 |
| Lavorazioni edilizie (subappalto) | 22% | Art. 17 c.6 DPR 633/72 |
| Cessione prodotti agricoli | Vari | Art. 17 c.5 DPR 633/72 |
| Cessione indumenti e accessori | 22% | Art. 17 c.2 DPR 633/72 |

**Trattamento**:
- Il destinatario emette autofattura
- IVA a debito e a credito nello stesso soggetto
- Registrazione in Quadro VL

**Scrittura completa**:
```
Acquisto rottami da fornitore:
6.01.001 Acquisto rottami      5.000,00
41.02 IVA reverse charge        1.100,00
  40.01 Fornitori rottami        5.000,00
  41.02 IVA reverse charge        1.100,00

Autofattura emessa:
41.02 IVA reverse charge        1.100,00
  5.04.004 Debiti IVA a debito    1.100,00
```

### 5. Split Payment (Meccanismo di Scissione dei Pagamenti)

**Applicabile a**:
- Operazioni con Pubbliche Amministrazioni (PA)
- Entità soggette a vigilanza pubblica
- Società controllate da PA

**Meccanismo**:
- La PA paga il netto al fornitore (esclusa IVA)
- La PA versa l'IVA direttamente all'erario
- Il fornitore registra IVA ma non la incassa

**Scrittura per il fornitore**:
```
Fattura emessa verso PA:
40.01 PA Cliente               1.220,00
  70.01 Ricavi vendite               1.000,00
  41.03 IVA split payment               220,00

Incasso (solo netto):
3.04.003 Banca                 1.000,00
  40.01 PA Cliente                     1.000,00

Storno IVA split:
41.03 IVA split payment         220,00
  5.04.004 Debiti IVA a debito          220,00
```

### 6. Operazioni con Partita IVA Non Identificata

**Acquisti da soggetti non identificati in Italia**:
- Autoliquidazione IVA all'importazione
- Registrazione come acquisto + IVA importazione
- Possibile deduzione se diritto a detrazione

**Scrittura**:
```
6.01.001 Acquisto merci        1.000,00
41.01 IVA a credito              220,00
  40.01 Fornitore estero         1.000,00
  41.01 IVA a credito              220,00
```

### 7. Importazioni

**Regime**:
- IVA dovuta all'importazione (sospensione possibile in regime doganale)
- Autoliquidazione con modello F24
- Diritto a deduzione immediato per assoggettati IVA

**Scrittura**:
```
6.01.001 Acquisto merci        1.000,00
41.01 IVA a credito              220,00
  40.01 Fornitore estero         1.000,00
  5.04.004 Debiti IVA a debito     220,00

Versamento IVA importazione:
5.04.004 Debiti IVA a debito     220,00
  3.04.003 Banca                   220,00
```

## Registrazioni IVA

### Registro Vendite

**Struttura obbligatoria** (Art. 24 DPR 633/72):
- Data fattura
- Numero fattura
- Nome cliente
- Imponibile
- Aliquota
- Imposta
- Codice operazione (se applicabile)

**Formato CSV**:
```csv
data,num_fattura,cliente,imponibile,aliquota,imposta,codice_op
2026-01-03,FT/2026/001,Cliente Alpha,1000.00,22,220.00,CE
2026-01-10,FT/2026/002,Cliente Beta,2000.00,10,200.00,CE
```

### Registro Acquisti

**Struttura obbligatoria** (Art. 25 DPR 633/72):
- Data fattura
- Numero fattura
- Nome fornitore
- Imponibile
- Aliquota
- Imposta
- Codice operazione

**Formato CSV**:
```csv
data,num_fattura,fornitore,imponibile,aliquota,imposta,codice_op
2026-01-05,INV-BETA-123,Fornitore Beta,800.00,22,176.00,AC
2026-01-08,INV-GAMMA-456,Fornitore Gamma,500.00,22,110.00,AC
```

## Liquidazione IVA

### Formula Base

```
IVA a debito (vendite) - IVA a credito (acquisti) = Saldo
```

**Se saldo > 0**: Versamento dovuto
**Se saldo < 0**: Credito da compensare o riportare

### Scadenze

| Regime | Scadenza | Modalità |
|--------|----------|----------|
| Mensile | 16 del mese successivo | F24 con codice 1001 |
| Trimestrale | 16 del mese successivo al trimestre | F24 con codice 1001 |
| Acconto annuale | 30 novembre (1° rata), 30 dicembre (2° rata) | F24 con codice 1004/1005 |

### Compensazione Credito IVA

**Regole**:
- Credito fino a 5.000€: compensabile con F24
- Credito > 5.000€: richiesta di rimborso o compensazione con autorizzazione
- Credito IVA può compensare: IRES, IRAP, IVA periodi successivi

**Scrittura compensazione**:
```
5.04.004 Debiti IVA a debito     1.000,00
  3.02.008 IVA a credito comp.     1.000,00
```

### Riepilogo Operazioni per Quadro IVA

| Quadro | Operazioni |
|--------|------------|
| **VE** | Cessioni intracomunitarie beni |
| **VL** | Prestazioni servizi intracom, reverse charge |
| **VI** | Acquisti intracomunitari |
| **VP** | Operazioni con PA (split payment) |
| **VC** | Crediti IVA da compensare |

## Note Operative

1. **Conservazione**: Registri IVA vanno conservati per 10 anni (Art. 2214 c.c.)

2. **Bollatura**: Registri IVA devono essere preventivamente vidimati dall'Agenzia delle Entrate o generati elettronicamente

3. **Intrastat**: Obbligatorio sopra soglie (beni: 100.000€/anno, servizi: 50.000€/anno)

4. **VIES**: Verifica obbligatoria numeri IVA intracomunitari prima dell'operazione

5. **Pro-rata**: Per operazioni esenti, calcolare pro-rata di detrazione (Art. 19 DPR 633/72)
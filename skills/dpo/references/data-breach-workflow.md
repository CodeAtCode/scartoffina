---
title: Data Breach - Workflow di Gestione
description: Guida completa alla gestione del data breach: rilevazione, valutazione, notifica al Garante (72h), comunicazione agli interessati
version: 0.1.0
last_updated: 2024-01-15
---

# Data Breach - Workflow di Gestione

## Introduzione

Questa guida fornisce una trattazione operativa della gestione dei data breach secondo il GDPR. Il materiale è destinato a DPO, responsabili della sicurezza e professionisti che devono gestire violazioni di dati personali.

**Riferimenti normativi:**
- GDPR art. 33 - Notifica della violazione al Garante
- GDPR art. 34 - Comunicazione della violazione all'interessato
- Linee Guida WP29 n. 3/2018 - Data Breach
- Provvedimento Garante Privacy n. 147/2022 - Linee guida data breach

---

## 1. Definizione di Data Breach

### 1.1 Cosa è un data breach

**Definizione (art. 4 n. 12 GDPR):**
> "Violazione di sicurezza che comporta accidentalmente o in modo illecito la distruzione, la perdita, la modifica, la divulgazione non autorizzata o l'accesso ai dati personali trasmessi, conservati o comunque trattati."

### 1.2 Tipologie di data breach

| Tipologia | Descrizione | Esempio |
|-----------|-------------|---------|
| **Confidenzialità** | Accesso/divulgazione non autorizzata | Email inviata al destinatario sbagliato |
| **Integrità** | Modifica non autorizzata | Dati alterati da malware |
| **Disponibilità** | Perdita/distruzione di dati | Ransomware che cifra i dati |

### 1.3 Casi comuni

**Violazioni di confidenzialità:**
- Email inviata a destinatario errato
- Dispositivo (laptop, smartphone) smarrito o rubato
- Accesso non autorizzato da parte di dipendenti
- Attacco phishing che compromette credenziali
- Condivisione file su cloud pubblico

**Violazioni di integrità:**
- Modifica accidentale di dati
- Attacco malware che altera dati
- Errori di sistema

**Violazioni di disponibilità:**
- Attacco ransomware
- Danni fisici a server
- Errore di cancellazione

---

## 2. Workflow di Gestione

### 2.1 Fase 1: Rilevazione

**Segnali di possibile data breach:**
- Alert di sistema (antivirus, firewall, SIEM)
- Segnalazione di un dipendente
- Segnalazione di un interessato
- Avviso da parte di terze parti
- Anomalia nei log di accesso

**Azioni immediate:**
1. **Registrare la segnalazione** (data, ora, segnalatore)
2. **Valutare la veridicità** (è un falso positivo?)
3. **Attivare il team di risposta** (DPO, IT, legale)

**Template registro rilevazione:**
```
ID Breach: BR-2024-001
Data rilevazione: 15/01/2024
Ora rilevazione: 14:30
Segnalato da: Mario Rossi (IT Manager)
Descrizione: Alert antivirus - possibile data exfiltration
Stato: In verifica
```

### 2.2 Fase 2: Contenimento

**Azioni di contenimento immediato:**
1. **Isolare i sistemi compromessi** (disconnessione rete)
2. **Revocare credenziali compromesse**
3. **Bloccare accessi non autorizzati**
4. **Preservare le prove** (per analisi forense)

**Priorità:**
- Prima: fermare la violazione in corso
- Seconda: preservare le prove
- Terza: valutare l'impatto

**Checklist contenimento:**
- [ ] Sistemi compromessi isolati
- [ ] Credenziali revocate
- [ ] Accessi bloccati
- [ ] Prove preservate
- [ ] Team di risposta attivato

### 2.3 Fase 3: Valutazione del Rischio

#### 2.3.1 Elementi da valutare

**Secondo art. 33 c. 3 GDPR, la notifica deve includere:**

1. **Natura della violazione:**
   - Categorie di dati coinvolti
   - Numero di interessati
   - Numero di registri di dati

2. **Conseguenze probabili:**
   - Rischio per diritti e libertà
   - Tipologie di danno potenziale

3. **Misure adottate/proposte:**
   - Misure di contenimento già attuate
   - Misure di mitigazione previste

#### 2.3.2 Matrice di valutazione del rischio

**Criteri di rischio (linee guida WP29):**

| Fattore | Basso | Medio | Alto |
|---------|-------|-------|------|
| **Tipo di dati** | Dati ordinari | Dati finanziari | Dati sanitari, biometrici, genetici |
| **Numero interessati** | < 100 | 100-1000 | > 1000 |
| **Identificabilità** | Dati anonimizzati | Dati pseudonimizzati | Dati identificativi diretti |
| **Gravità potenziale** | Danno minimo | Danno moderato | Danno grave |
| **Caratteristiche interessati** | Adulti generici | Minori, soggetti vulnerabili | Categorie particolari |

#### 2.3.3 Livelli di rischio

**Rischio BASSO:**
- Dati ordinari (nome, email)
- Numero limitato di interessati (< 100)
- Dati pseudonimizzati o cifrati
- Danno potenziale minimo

**Rischio MEDIO:**
- Dati finanziari (IBAN, carta di credito)
- Numero medio di interessati (100-1000)
- Possibile danno economico limitato

**Rischio ALTO:**
- Dati sanitari, genetici, biometrici
- Dati relativi a condanne penali
- Numero elevato di interessati (> 1000)
- Minors o soggetti vulnerabili
- Danno potenziale grave (discriminazione, furto identità, danni alla reputazione)

### 2.4 Fase 4: Decisione sulla Notifica

#### 2.4.1 Notifica al Garante (art. 33)

**Obbligatoria SE:**
- Il data breach comporta un **rischio per i diritti e le libertà** degli interessati

**Eccezione (NON notificare):**
- Il rischio è **improbabile** (es. dati cifrati con chiave non compromessa)

**Termini:**
- **Entro 72 ore** dalla scoperta
- Se oltre 72 ore: fornire motivazione del ritardo

#### 2.4.2 Comunicazione all'interessato (art. 34)

**Obbligatoria SE:**
- Il data breach comporta un **rischio elevato** per i diritti e le libertà

**Eccezioni (NON comunicare):**
1. Dati cifrati e chiave non compromessa
2. Misure successive che rendono il rischio improbabile
3. Sproporzione (in tal caso: comunicazione pubblica)

**Termini:**
- **Senza ingiustificato ritardo**
- Di norma: entro 72 ore dalla valutazione

### 2.5 Fase 5: Notifica al Garante

#### 2.5.1 Canali di notifica

**Modulo online:**
- Portale Garante Privacy: www.garanteprivacy.it
- Sezione "Data Breach"
- Modulo "Notifica violazione dati personali"

**Contenuto obbligatorio:**
1. Descrizione natura della violazione
2. Categorie e numero di interessati
3. Categorie e numero di registri
4. Nome e contatti del DPO
5. Conseguenze probabili
6. Misure adottate/proposte

#### 2.5.2 Template notifica

```
NOTIFICA DATA BREACH - ART. 33 GDPR

1. DATI DEL TITOLARE
   Ragione sociale: Azienda Esempio S.r.l.
   Indirizzo: Via Roma 1, 00100 Roma
   P.IVA: 12345678901
   DPO: dpo@aziendaesempio.it

2. DATA E ORA VIOLAZIONE
   Data scoperta: 15/01/2024
   Ora scoperta: 14:30
   Data evento (se nota): 14/01/2024

3. NATURA DELLA VIOLAZIONE
   Tipologia: Accesso non autorizzato
   Descrizione: Attacco phishing ha compromesso credenziali di un dipendente
   Dati coinvolti: Dati anagrafici, email, numeri di telefono

4. CATEGORIE INTERESSATI
   Categoria: Clienti
   Numero stimato: 500

5. CATEGORIE DATI
   - Dati anagrafici (nome, cognome)
   - Dati di contatto (email, telefono)
   - NON dati finanziari
   - NON dati sanitari

6. CONSEGUENZE PROBABILI
   - Rischio di spam/phishing mirato
   - Rischio basso di furto identità
   - Nessun rischio finanziario diretto

7. MISURE ADOTTATE
   - Credenziali revocate
   - Password resettate
   - Monitoraggio account attivato
   - Formazione phishing programmata

8. MISURE DI MITIGAZIONE
   - Notifica agli interessati
   - Supporto per cambio password
   - Monitoraggio attività sospette

9. RITARDO (se applicabile)
   Motivo: -
   Tempo di ritardo: -

Firma: ___________________
Data: 15/01/2024
```

### 2.6 Fase 6: Comunicazione all'Interested

#### 2.6.1 Quando comunicare

**Obbligatoria SE:**
- Rischio ALTO per diritti e libertà

**Esempi di rischio elevato:**
- Dati sanitari compromessi
- Dati finanziari (carte di credito)
- Dati per identificazione diretta
- Possibile furto identità
- Discriminazione potenziale

#### 2.6.2 Modalità di comunicazione

**Canali:**
- Email (se disponibile)
- Lettera raccomandata
- Comunicazione pubblica (se sproporzione)

**Requisiti:**
- Linguaggio chiaro e semplice
- Tempestività
- Trasparenza

#### 2.6.3 Template comunicazione

```
COMUNICAZIONE DATA BREACH - ART. 34 GDPR

Gentile [Nome],

TI INFORMIAMO DI UNA VIOLAZIONE DEI TUOI DATI PERSONALI

Cosa è successo:
Il [data] è stato rilevato un accesso non autorizzato al nostro sistema
che ha interessato i dati dei nostri clienti.

Quali dati sono stati coinvolti:
- Nome e cognome
- Indirizzo email
- Numero di telefono
- NON sono stati coinvolti dati finanziari o finanziari

Cosa stiamo facendo:
- Abbiamo bloccato l'accesso non autorizzato
- Abbiamo rafforzato le nostre misure di sicurezza
- Stiamo indagando sulle cause

Cosa puoi fare tu:
- Monitorare le tue email per possibili tentativi di phishing
- Cambiare la password del tuo account (se ne hai una)
- Contattaci se hai domande

Per maggiori informazioni:
Email: privacy@aziendaesempio.it
Telefono: 06 1234567

Data: 15/01/2024
Firma: Il Titolare del trattamento
```

### 2.7 Fase 7: Documentazione

#### 2.7.1 Documentazione obbligatoria (art. 33 c. 5)

**Ogni violazione deve essere documentata:**
- Data e circostanze della violazione
- Effetti della violazione
- Misure correttive adottate

**Conservazione:**
- Per tutta la durata del rapporto
- + 10 anni dopo (conservazione documentale)

#### 2.7.2 Template documentazione interna

```
DOCUMENTAZIONE DATA BREACH - INTERNA

ID Breach: BR-2024-001

1. RILEVAZIONE
   Data: 15/01/2024
   Ora: 14:30
   Segnalato da: Mario Rossi
   Metodo: Alert antivirus

2. CONTENIMENTO
   Azioni intraprese:
   - 14:35: Isolamento server compromesso
   - 14:40: Revoca credenziali dipendente
   - 15:00: Attivazione team di risposta
   
   Responsabile: IT Manager

3. VALUTAZIONE
   Tipologia: Accesso non autorizzato
   Dati coinvolti: 500 clienti
   Rischio stimato: MEDIO
   
   Valutatore: DPO
   Data: 15/01/2024

4. NOTIFICA AL GARANTE
   Data notifica: 15/01/2024
   Orario: 10:00
   Canale: Portale online
   ID notifica: GAR-2024-12345

5. COMUNICAZIONE INTERESSATI
   Data: 16/01/2024
   Metodo: Email
   Numero interessati: 500
   Template utilizzato: COMM-001

6. MISURE CORRETTIVE
   - Formazione phishing per tutti i dipendenti
   - Implementazione 2FA
   - Revisione policy accessi
   - Audit sicurezza trimestrale

7. CHIUSURA
   Data chiusura: 30/01/2024
   Responsabile: DPO
   Note: Nessuna segnalazione successiva
```

---

## 3. Tempi e Scadenze

### 3.1 Timeline 72 ore

**Ora 0: Scoperta del breach**
- Registrare la segnalazione
- Attivare team di risposta

**Ora 0-24: Contenimento e valutazione iniziale**
- Isolare sistemi compromessi
- Valutare natura e portata
- Identificare dati e interessati coinvolti

**Ora 24-48: Valutazione approfondita**
- Determinare livello di rischio
- Decidere se notificare
- Preparare documentazione

**Ora 48-72: Notifica (se necessaria)**
- Inviare notifica al Garante
- Preparare comunicazione agli interessati

**Ora 72+:**
- Comunicare agli interessati (se rischio elevato)
- Implementare misure correttive
- Documentare tutto

### 3.2 Scadenze

| Adempimento | Termine |
|-------------|---------|
| Notifica al Garante | 72 ore dalla scoperta |
| Comunicazione interessati | Senza ingiustificato ritardo |
| Documentazione interna | Entro la chiusura dell'incidente |
| Report finale | 30 giorni dalla chiusura |

---

## 4. Sanzioni

### 4.1 Mancata notifica

**Art. 83 c. 5 GDPR:**
- Fino a 20 milioni di euro
- O 4% del fatturato mondiale annuo
- Il maggiore dei due importi

**Criteri di irrogazione:**
- Natura, gravità e durata della violazione
- Intenzionalità o negligenza
- Misure di mitigazione adottate
- Grado di cooperazione con il Garante

### 4.2 Casi reali (esempi)

| Azienda | Sanzione | Motivo |
|---------|----------|--------|
| Google | 50 milioni € | Mancata informativa cookie |
| Amazon | 746 milioni € | Violazione dati clienti |
| TikTok | 345 milioni € | Trasferimento dati minori |

---

## 5. Best Practices

### 5.1 Prevenzione

**Misure tecniche:**
- Cifratura dati (a riposo e in transito)
- Controllo accessi (autenticazione multi-fattore)
- Backup regolari
- Monitoraggio continuo (SIEM)
- Aggiornamenti di sicurezza

**Misure organizzative:**
- Policy di sicurezza
- Formazione del personale
- Procedure di risposta
- Test periodici (penetration test)
- Audit di sicurezza

### 5.2 Preparazione

**Prima che accada:**
- Designare team di risposta
- Definire procedure scritte
- Preparare template di notifica
- Testare le procedure (simulazioni)
- Mantenere contatti aggiornati con Garante

---

## 6. Checklist Operativa

### 6.1 Checklist immediata (ore 0-24)

- [ ] Registrare la segnalazione
- [ ] Attivare team di risposta
- [ ] Isolare sistemi compromessi
- [ ] Revocare credenziali compromesse
- [ ] Preservare le prove
- [ ] Iniziare valutazione del rischio

### 6.2 Checklist 72 ore

- [ ] Completare valutazione del rischio
- [ ] Determinare se notificare
- [ ] Preparare notifica al Garante
- [ ] Inviare notifica (entro 72h)
- [ ] Preparare comunicazione interessati
- [ ] Documentare tutte le azioni

### 6.3 Checklist post-breach

- [ ] Comunicare agli interessati (se necessario)
- [ ] Implementare misure correttive
- [ ] Completare documentazione
- [ ] Revisione procedure
- [ ] Formazione aggiuntiva
- [ ] Report finale

---

**Nota:** Questa guida è aggiornata al gennaio 2024. Verificare sempre le linee guida EDPB e i provvedimenti del Garante più recenti.
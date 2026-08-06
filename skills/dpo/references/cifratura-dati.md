# Misure di sicurezza e cifratura dei dati - art. 32 GDPR

## Riferimento normativo
GDPR art. 32 — sicurezza del trattamento. Codice privacy Allegato B (disciplina tecnica).

## Obbligo
Il titolare e il responsabile attuano **misure tecniche e organizzative adeguate** per garantire un livello di sicurezza appropriato al rischio (art. 32 c. 1).

## Fattori di valutazione del rischio (art. 32 c. 1)
1. Stato dell'arte.
2. Costi di attuazione.
3. Natura, portata, contesto e finalità del trattamento.
4. Rischi con probabilità e gravità variabili per i diritti e le libertà delle persone.

## Misure tecniche (art. 32 c. 1 a)
- **Pseudonimizzazione** e cifratura dei dati personali.
- **Riservatezza**, integrità, disponibilità e resilienza dei sistemi.
- **Ripristino** tempestivo della disponibilità in caso di incidente.
- **Procedure** regolari di test, verifica e valutazione dell'efficacia.

## Misure organizzative
- Policy di sicurezza.
- Formazione del personale.
- Gestione accessi (RBAC, least privilege).
- Gestione incidenti (incident response plan).
- Backup e disaster recovery.
- Audit periodici.

## Cifratura
- **A riposo**: AES-256 per database, dischi, backup.
- **In transito**: TLS 1.3 per comunicazioni web.
- **Gestione chiavi**: KMS, rotazione periodica, separazione ruoli.
- **Tokenizzazione** e pseudonimizzazione per ridurre l'esposizione.

## Allegato B Codice privacy (Italia)
Disciplina tecnica minima per trattamenti con strumenti elettronici:
- Autenticazione forte (almeno 8 caratteri, complessità).
- Gestione credenziali (rotazione, revoca).
- Logging accessi (almeno 6 mesi).
- Backup e conservazione.
- Cifratura per dati particolari.

## Data breach
Una violazione delle misure di sicurezza deve essere valutata ex art. 33-34 (notifica Garante entro 72 ore se rischio per diritti e libertà).

## Sanzioni
Violazione delle misure di sicurezza: art. 83 c. 4 GDPR (fino a 10 milioni di euro o 2% fatturato mondiale).

## Verifica sempre online
Lo stato dell'arte della sicurezza evolve. Verificare i provvedimenti del Garante e le raccomandazioni ENISA (enisa.europa.eu).

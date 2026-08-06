# Rubrica di Valutazione: Fiscalista

**Skill:** `fiscalista`  
**Tipo:** Valutazione mista (qualitativa + numerica)  
**Ultimo aggiornamento:** 2026-08-05

---

## Descrizione

Questa rubrica definisce i criteri per valutare l'output di un agente IA che svolge la funzione di Fiscalista per persone fisiche. Include sia criteri qualitativi (correttezza normativa) che verifiche numeriche (scaglioni, aliquote, calcoli).

---

## Criteri di Valutazione

| Criterio | Tipo | Sì/No | Note |
|----------|------|-------|------|
| Gli scaglioni IRPEF usati corrispondono a data/scaglioni-irpef.json? | Numerico | | |
| Le detrazioni sono calcolate correttamente (lavoro dipendente, pensione, carichi familiari)? | Numerico | | |
| Le addizionali regionali e comunali sono considerate? | Qualitativo | | |
| L'IMU è calcolata con aliquota comunale corretta? | Numerico | | |
| La tassazione rendite finanziarie distingue 26% e 12,5%? | Numerico | | |
| Il Quadro RW/RT per crypto-attività è compilato quando rilevante? | Logico | | |
| La cedolare secca è applicata con aliquota corretta (21% ordinaria, 10% canone concordato)? | Numerico | | |
| Gli acconti IRPEF sono calcolati col metodo corretto (storico/previsionale)? | Numerico | | |

---

## Giudizio Sintetico

**Punteggio:** __/8 criteri soddisfatti

**Valutazione complessiva:**
- [ ] **Accettabile** (≥7 criteri soddisfatti)
- [ ] **Da migliorare** (5-6 criteri soddisfatti)
- [ ] **Non accettabile** (≤4 criteri soddisfatti)

**Commenti del revisore:**

---

## Istruzioni per il Judge LLM

1. Per i criteri **numerici**: verificare i calcoli contro i dati di riferimento (scaglioni-irpef.json, aliquote-imu.json, tassazione-rendite-finanziarie.json).
2. Per i criteri **qualitativi**: valutare la completezza della considerazione di addizionali.
3. Per i criteri **logici**: verificare che il Quadro RW/RT sia compilato solo quando rilevante (presenza di crypto-attività).
4. Non assegnare punteggi parziali.
5. Il giudizio sintetico deve essere coerente con il conteggio dei criteri.
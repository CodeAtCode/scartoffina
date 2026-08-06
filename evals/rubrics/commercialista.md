# Rubrica di Valutazione: Commercialista

**Skill:** `commercialista`  
**Tipo:** Valutazione mista (qualitativa + numerica)  
**Ultimo aggiornamento:** 2026-08-05

---

## Descrizione

Questa rubrica definisce i criteri per valutare l'output di un agente IA che svolge la funzione di Commercialista. Include sia criteri qualitativi (conformità normativa) che verifiche numeriche (quadratura, calcoli IVA).

---

## Criteri di Valutazione

| Criterio | Tipo | Sì/No | Note |
|----------|------|-------|------|
| La partita doppia è in quadratura (somma dare = somma avere) per ogni scrittura? | Numerico | | |
| L'IVA è separata correttamente (imponibile × aliquota da data/aliquote-iva.json)? | Numerico | | |
| I codici tributo F24 esistono in data/codici-tributo-f24.json? | Referenziale | | |
| La numerazione fatture è consecutiva (nessun salto/duplicato)? | Logico | | |
| Lo Stato Patrimoniale e il Conto Economico seguono OIC 12? | Qualitativo | | |
| Il `_meta.verified_at` dei dati usati è recente (non scaduto)? | Temporale | | |
| Le scritture di assestamento coprono ammortamenti, TFR, ratei/risconti, rimanenze, imposte? | Qualitativo | | |

---

## Giudizio Sintetico

**Punteggio:** __/7 criteri soddisfatti

**Valutazione complessiva:**
- [ ] **Accettabile** (≥6 criteri soddisfatti)
- [ ] **Da migliorare** (4-5 criteri soddisfatti)
- [ ] **Non accettabile** (≤3 criteri soddisfatti)

**Commenti del revisore:**

---

## Istruzioni per il Judge LLM

1. Per i criteri **numerici**: verificare i calcoli contro i dati di riferimento.
2. Per i criteri **referenziali**: controllare che i codici esistano nei file JSON indicati.
3. Per i criteri **logici**: verificare la consecutività della numerazione.
4. Per i criteri **qualitativi**: valutare la conformità agli standard OIC.
5. Per i criteri **temporali**: verificare che `_meta.verified_at` non superi la cadenza di validità.
6. Non assegnare punteggi parziali.
7. Il giudizio sintetico deve essere coerente con il conteggio dei criteri.
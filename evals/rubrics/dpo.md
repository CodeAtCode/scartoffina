# Rubrica di Valutazione: DPO (Data Protection Officer)

**Skill:** `dpo`  
**Tipo:** Valutazione qualitativa  
**Ultimo aggiornamento:** 2026-08-05

---

## Descrizione

Questa rubrica definisce i criteri qualitativi per valutare l'output di un agente IA che svolge la funzione di Data Protection Officer secondo il GDPR e il Codice privacy italiano. La valutazione è basata su criteri binari (sì/no) applicati dal judge LLM.

---

## Criteri di Valutazione

| Criterio | Sì/No | Note |
|----------|-------|------|
| Il registro dei trattamenti (art. 30) è completo (finalità, categorie, destinatari, trasferimenti, misure)? | | |
| La valutazione DPIA (art. 35) è giustificata quando necessaria? | | |
| La procedura di data breach (72h, art. 33-34) è documentata? | | |
| I diritti dell'interessato (art. 12-22) sono tutti coperti con tempi di risposta? | | |
| I trasferimenti extra-UE (art. 44-49) hanno base giuridica adeguata? | | |
| Le sanzioni (art. 83) sono quantificate correttamente? | | |
| I provvedimenti del Garante rilevanti sono citati? | | |

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

1. Applicare ogni criterio in modo binario: **sì** se il criterio è pienamente soddisfatto, **no** altrimenti.
2. Non assegnare punteggi parziali.
3. Nel campo "Note", indicare brevemente la motivazione del sì/no.
4. Il giudizio sintetico deve essere coerente con il conteggio dei criteri.
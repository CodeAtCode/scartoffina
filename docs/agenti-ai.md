# Guida all'uso di Scartoffina con gli Agenti AI

**Documentazione per l'integrazione delle skill Scartoffina con agenti AI di programmazione.**

---

## ⚠️ Avvertenza legale

**Scartoffina NON è uno strumento di consulenza professionale e NON sostituisce in alcun modo il parere di un professionista abilitato.**

- Scartoffina è uno strumento di supporto alla documentazione e al calcolo. Le informazioni prodotte hanno scopo informativo e di produttività, non costituiscono parere professionale, né consiglio fiscale, contabile, legale, sindacale, previdenziale o in materia di protezione dei dati personali.
- Le norme italiane (fiscali, previdenziali, del lavoro, civili, privacy) cambiano frequentemente e con effetto retroattivo. I dati contenuti nelle skill possono essere obsoleti, incompleti o non applicabili al caso specifico. Verificare sempre la vigenza e l'applicabilità prima di fare affidamento su qualsiasi output.
- L'utilizzo degli output di Scartoffina è a rischio e responsabilità esclusivi dell'utilizzatore. Gli autori e i contributori non rispondono di eventuali errori, omissioni, danni o pregiudizi derivanti dall'uso del materiale, anche in caso di difetti nei dati o nei modelli.

**In caso di dubbi su un adempimento, rivolgersi a un professionista abilitato.**

---

## Prerequisiti

> **Nota:** I comandi usano la variabile `$SCARTOFFINA_DIR` per riferirsi alla directory del repository. Impostala prima di eseguire i comandi:
> ```bash
> export SCARTOFFINA_DIR=/path/to/scartoffina
> ```
> Oppure, se sei nella directory del repository:
> ```bash
> export SCARTOFFINA_DIR=$(pwd)
> ```

Prima di configurare gli agenti AI, assicurati di avere:

1. **Clonato il repository Scartoffina**:
   ```bash
   git clone <repo-url> scartoffina && cd scartoffina
   ```

2. **Creato il file `company.json`**:
   ```bash
   cp company.example.json company.json
   ```
   Compila `company.json` con i dati reali dell'azienda o del contribuente.

3. **Installato le dipendenze** (opzionale, per gli script di aggiornamento):
   ```bash
   ./scartoffina.sh install
   ```

Le 9 skill disponibili sono:
- `commercialista`
- `fiscalista`
- `inps-inail`
- `consulente-del-lavoro`
- `notaio`
- `amministratore-condominio`
- `revisore-legale`
- `controllore-fiscale`
- `dpo`

---

## Tabella agenti supportati

| Agente | URL | Percorso skill (project) | Supporto nativo |
|--------|-----|--------------------------|-----------------|
| Claude Code | https://code.claude.com | `.claude/skills/<name>/SKILL.md` | Sì |
| OpenCode | https://opencode.ai | `.opencode/skills/<name>/SKILL.md` | Sì |
| Cursor | https://cursor.com | `.cursor/skills/<name>/SKILL.md` | Sì |
| Gemini CLI | https://geminicli.com | `.gemini/skills/<name>/SKILL.md` | Sì* |
| Continue.dev | https://continue.dev | `.continue/skills/<name>/SKILL.md` | Sì |
| Cline | https://cline.bot | `.cline/skills/<name>/SKILL.md` | Sì |
| OpenClaw | https://openclaw.ai | `skills/<name>/SKILL.md` | Sì |
| Codex CLI | https://openai.com | `.codex/skills/<name>/SKILL.md` | Sì |
| Hermes | Nous Research | `.hermes/skills/<name>/SKILL.md` | Sì |
| Aider | https://aider.chat | Caricamento manuale | No |

*Gemini CLI richiede l'abilitazione della flag sperimentale: `"experimental": {"skills": true}` nella configurazione.

> **Nota:** I percorsi di caricamento delle skill sono basati sulla documentazione ufficiale di ogni agente (Agosto 2026). Verificare sempre la documentazione corrente dell'agente in uso, poiché i percorsi possono cambiare tra le versioni.

---

## Claude Code

**URL:** https://code.claude.com

**Percorso skill:** `~/.claude/skills/<name>/SKILL.md` (globale) o `<project>/.claude/skills/<name>/SKILL.md` (project)

### Installazione delle skill

Installa tutte le 9 skill di Scartoffina per Claude Code:

```bash
# Crea la directory delle skill
mkdir -p ~/.claude/skills

# Copia tutte le skill
for skill in commercialista fiscalista inps-inail consulente-del-lavoro notaio amministratore-condominio revisore-legale controllore-fiscale dpo; do
  cp -r "$SCARTOFFINA_DIR/skills/$skill" ~/.claude/skills/
done
```

Oppure, per un'installazione project-specific:

```bash
mkdir -p .claude/skills
for skill in commercialista fiscalista inps-inail consulente-del-lavoro notaio amministratore-condominio revisore-legale controllore-fiscale dpo; do
  cp -r skills/$skill .claude/skills/
done
```

### Esempio di utilizzo

Dopo aver avviato Claude Code nel progetto:

```
Usa la skill commercialista per registrare questa fattura:
- Fornitore: Acme S.r.l.
- Numero: Fattura 123/2026
- Data: 15/01/2026
- Importo: € 1.000,00 + IVA 22%
- Conto di costo: 60.10.00 "Acquisti servizi"
```

Claude Code leggerà automaticamente `~/.claude/skills/commercialista/SKILL.md` e risponderà secondo le istruzioni della skill.

---

## OpenCode

**URL:** https://opencode.ai

**Percorso skill:** `.opencode/skills/<name>/SKILL.md` (project) o `~/.config/opencode/skills/` (globale)

### Installazione delle skill

Installa tutte le 9 skill per OpenCode:

```bash
# Installazione project-specific
mkdir -p .opencode/skills
for skill in commercialista fiscalista inps-inail consulente-del-lavoro notaio amministratore-condominio revisore-legale controllore-fiscale dpo; do
  cp -r skills/$skill .opencode/skills/
done
```

Oppure per l'installazione globale:

```bash
mkdir -p ~/.config/opencode/skills
for skill in commercialista fiscalista inps-inail consulente-del-lavoro notaio amministratore-condominio revisore-legale controllore-fiscale dpo; do
  cp -r "$SCARTOFFINA_DIR/skills/$skill" ~/.config/opencode/skills/
done
```

### Esempio di utilizzo

In una sessione OpenCode:

```
Carica la skill fiscalista e calcola l'IRPEF per un contribuente con:
- Reddito lavoro dipendente: € 35.000
- Coniuge a carico
- Spese mediche: € 1.500
```

OpenCode caricherà automaticamente la skill e applicherà le regole di calcolo documentate.

---

## Cursor

**URL:** https://cursor.com

**Percorso skill:** `.cursor/skills/<name>/SKILL.md` (project) o `~/.cursor/skills/` (globale)

### Installazione delle skill

```bash
# Installazione project-specific
mkdir -p .cursor/skills
for skill in commercialista fiscalista inps-inail consulente-del-lavoro notaio amministratore-condominio revisore-legale controllore-fiscale dpo; do
  cp -r skills/$skill .cursor/skills/
done
```

### Esempio di utilizzo

In Cursor, apri la chat e chiedi:

```
Usa la skill notaio per calcolare le spese per un atto di compravendita immobiliare:
- Prezzo: € 200.000
- Categoria: A/2
- Comune: Roma
```

Cursor leggerà la skill `notaio` e calcolerà onorari e imposte secondo il D.M. 17/2017.

---

## Gemini CLI

**URL:** https://geminicli.com

**Percorso skill:** `.gemini/skills/<name>/SKILL.md` (project) o `~/.gemini/skills/` (globale)

### Configurazione preliminare

Abilita le skill nella configurazione di Gemini CLI:

```json
// ~/.gemini/config.json
{
  "experimental": {
    "skills": true
  }
}
```

### Installazione delle skill

```bash
mkdir -p ~/.gemini/skills
for skill in commercialista fiscalista inps-inail consulente-del-lavoro notaio amministratore-condominio revisore-legale controllore-fiscale dpo; do
  cp -r "$SCARTOFFINA_DIR/skills/$skill" ~/.gemini/skills/
done
```

---

## Continue.dev

**URL:** https://continue.dev

**Percorso skill:** `.continue/skills/<name>/SKILL.md` (project) o `~/.continue/skills/` (globale)

### Installazione delle skill

```bash
mkdir -p ~/.continue/skills
for skill in commercialista fiscalista inps-inail consulente-del-lavoro notaio amministratore-condominio revisore-legale controllore-fiscale dpo; do
  cp -r "$SCARTOFFINA_DIR/skills/$skill" ~/.continue/skills/
done
```

---

## Cline

**URL:** https://cline.bot

**Percorso skill:** `.cline/skills/<name>/SKILL.md` (project) o `~/.cline/skills/` (globale)

### Installazione delle skill

```bash
mkdir -p ~/.cline/skills
for skill in commercialista fiscalista inps-inail consulente-del-lavoro notaio amministratore-condominio revisore-legale controllore-fiscale dpo; do
  cp -r "$SCARTOFFINA_DIR/skills/$skill" ~/.cline/skills/
done
```

---

## OpenClaw

**URL:** https://openclaw.ai

**Percorso skill:** `skills/<name>/SKILL.md` (project) o `~/.openclaw/skills/` (globale)

### Installazione delle skill

OpenClaw legge le skill direttamente dalla cartella `skills/` del progetto, quindi non è necessaria alcuna copia se lavori nel repository Scartoffina.

Per l'installazione globale:

```bash
mkdir -p ~/.openclaw/skills
for skill in commercialista fiscalista inps-inail consulente-del-lavoro notaio amministratore-condominio revisore-legale controllore-fiscale dpo; do
  cp -r "$SCARTOFFINA_DIR/skills/$skill" ~/.openclaw/skills/
done
```

---

## Codex CLI

**URL:** https://openai.com

**Percorso skill:** `.codex/skills/<name>/SKILL.md` (project) o `~/.codex/skills/` (globale)

### Installazione delle skill

```bash
mkdir -p ~/.codex/skills
for skill in commercialista fiscalista inps-inail consulente-del-lavoro notaio amministratore-condominio revisore-legale controllore-fiscale dpo; do
  cp -r "$SCARTOFFINA_DIR/skills/$skill" ~/.codex/skills/
done
```

---

## Hermes (Nous Research)

**URL:** Nous Research

**Percorso skill:** `.hermes/skills/<name>/SKILL.md` (project) o `~/.hermes/skills/` (globale)

### Installazione delle skill

```bash
mkdir -p ~/.hermes/skills
for skill in commercialista fiscalista inps-inail consulente-del-lavoro notaio amministratore-condominio revisore-legale controllore-fiscale dpo; do
  cp -r "$SCARTOFFINA_DIR/skills/$skill" ~/.hermes/skills/
done
```

---

## Aider

**URL:** https://aider.chat

**Supporto:** Non nativo — caricamento manuale richiesto

### Metodo 1: Caricamento singolo con flag `--read`

```bash
aider --read skills/commercialista/SKILL.md
```

### Metodo 2: Configurazione permanente in `.aider.conf.yml`

```yaml
# .aider.conf.yml
read:
  - skills/commercialista/SKILL.md
  - skills/fiscalista/SKILL.md
  - skills/inps-inail/SKILL.md
  - skills/consulente-del-lavoro/SKILL.md
  - skills/notaio/SKILL.md
  - skills/amministratore-condominio/SKILL.md
  - skills/revisore-legale/SKILL.md
  - skills/controllore-fiscale/SKILL.md
  - skills/dpo/SKILL.md
```

### Metodo 3: Script di avvio

Crea uno script per caricare tutte le skill:

```bash
#!/bin/bash
# scartoffina-aider.sh

SKILLS_DIR="${SCARTOFFINA_DIR:-$(pwd)}/skills"

aider \
  --read "$SKILLS_DIR/commercialista/SKILL.md" \
  --read "$SKILLS_DIR/fiscalista/SKILL.md" \
  --read "$SKILLS_DIR/inps-inail/SKILL.md" \
  --read "$SKILLS_DIR/consulente-del-lavoro/SKILL.md" \
  --read "$SKILLS_DIR/notaio/SKILL.md" \
  --read "$SKILLS_DIR/amministratore-condominio/SKILL.md" \
  --read "$SKILLS_DIR/revisore-legale/SKILL.md" \
  --read "$SKILLS_DIR/controllore-fiscale/SKILL.md" \
  --read "$SKILLS_DIR/dpo/SKILL.md"
```

---

## Strategia generica: symlink per tutti gli agenti

Invece di copiare le skill per ogni agente, usa i symlink per esporre le skill di Scartoffina a qualsiasi agente senza duplicazione:

```bash
# Esempio per Claude Code
ln -s "$SCARTOFFINA_DIR/skills/commercialista" ~/.claude/skills/commercialista
  ln -s "$SCARTOFFINA_DIR/skills/fiscalista" ~/.claude/skills/fiscalista
# ... ripeti per tutte le skill

# Oppure in un'unica riga per tutte le skill e tutti gli agenti
for agent_dir in ~/.claude/skills ~/.opencode/skills ~/.cursor/skills ~/.gemini/skills ~/.continue/skills ~/.cline/skills ~/.openclaw/skills ~/.codex/skills ~/.hermes/skills; do
  mkdir -p "$agent_dir"
  for skill in commercialista fiscalista inps-inail consulente-del-lavoro notaio amministratore-condominio revisore-legale controllore-fiscale dpo; do
    ln -sf "$SCARTOFFINA_DIR/skills/$skill" "$agent_dir/$skill"
  done
done
```

**Vantaggi:**
- Le skill sono aggiornate automaticamente quando modifichi i file nel repository Scartoffina
- Nessuna duplicazione di dati su disco
- Un'unica fonte di verità

**Svantaggi:**
- Le modifiche accidentali alle skill tramite l'agente AI modificano il repository originale
- Richiede che il percorso assoluto sia corretto

> **⚠️ Attenzione:** I symlink espongono il repository Scartoffina a modifiche accidentali. Se l'agente AI scrive nei file della skill, modifica il repository originale. Per uso production, preferire la copia (`cp -r`) ai symlink.

---

## Risoluzione problemi

### Le skill non vengono caricate automaticamente

**Problema:** L'agente AI non trova le skill.

**Verifica:**
1. Controlla che il percorso delle skill sia corretto:
   ```bash
   ls -la ~/.claude/skills/
   ```
2. Verifica che i file `SKILL.md` esistano:
   ```bash
   ls -la ~/.claude/skills/commercialista/SKILL.md
   ```

**Soluzione:** Ricopia le skill nel percorso corretto.

### L'agente AI non risponde secondo le istruzioni della skill

**Problema:** L'agente ignora le regole della skill.

**Verifica:**
1. Controlla che la skill sia stata caricata nel contesto:
   - Cerca riferimenti al contenuto di `SKILL.md` nella risposta
2. Verifica che il file `SKILL.md` non sia corrotto:
   ```bash
   head -20 ~/.claude/skills/commercialista/SKILL.md
   ```

**Soluzione:** Riavvia la sessione dell'agente AI dopo aver verificato i file.

### Gemini CLI non carica le skill

**Problema:** Le skill non vengono riconosciute da Gemini CLI.

**Verifica:**
1. Controlla che la flag sperimentale sia abilitata:
   ```bash
   cat ~/.gemini/config.json | grep -A2 experimental
   ```

**Soluzione:** Abilita `"experimental": {"skills": true}` e riavvia Gemini CLI.

### Aider non legge le skill

**Problema:** Aider ignora i file `SKILL.md`.

**Verifica:**
1. Controlla che i percorsi in `.aider.conf.yml` siano corretti (relativi alla directory corrente):
   ```bash
   cat .aider.conf.yml
   ```

**Soluzione:** Usa percorsi assoluti o assicurati di eseguire `aider` dalla directory corretta.

### Conflitti tra versioni delle skill

**Problema:** Hai skill duplicate in percorsi globale e project-specific.

**Verifica:**
```bash
ls -la ~/.claude/skills/commercialista/
ls -la .claude/skills/commercialista/
```

**Soluzione:** Usa solo uno dei due percorsi (consigliato: project-specific per portabilità).

---

## Riferimenti

- [README.md](../README.md) — Documentazione principale di Scartoffina
- [skillreg.dev](https://skillreg.dev) — Standard per le skill degli agenti AI
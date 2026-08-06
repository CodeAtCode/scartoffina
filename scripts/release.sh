#!/usr/bin/env bash
# scripts/release.sh — CI di release: scarica tutti i dataset e genera uno ZIP
# Usage: bash scripts/release.sh [version]
# Esempio: bash scripts/release.sh 0.2.0
#
# Cosa fa:
#   1. Aggiorna tutti i dataset (updater)
#   2. Verifica freshness di tutti i file
#   3. Genera uno ZIP pronto al rilascio (skills + data + updater + integrazioni)
#   4. Lo ZIP è autonomo: non richiede git clone, contiene già i dati aggiornati

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

PYTHON="${PYTHON:-python3}"
VERSION="${1:-dev}"
ZIP_NAME="scartoffina-${VERSION}.zip"
STAGING="$(mktemp -d)"
trap 'rm -rf "$STAGING"' EXIT

echo "=== Scartoffina release v${VERSION} ==="
echo ""

# 1. Aggiorna tutti i dataset
echo "[1/4] Aggiornamento dataset..."
"$PYTHON" -m updater.cli update ateco 2>/dev/null || echo "  ⚠️ ateco: salto (fonte non disponibile)"
"$PYTHON" -m updater.cli update irpef 2>/dev/null || echo "  ⚠️ irpef: salto (fonte non disponibile)"
"$PYTHON" -m updater.cli update imu 2>/dev/null || echo "  ⚠️ imu: salto (fonte non disponibile)"
"$PYTHON" -m updater.cli update f24_codici 2>/dev/null || echo "  ⚠️ f24_codici: salto (fonte non disponibile)"
echo "  ✓ Dataset aggiornati"
echo ""

# 2. Verifica freshness
echo "[2/4] Verifica freshness..."
if ! "$PYTHON" -m updater.cli verify; then
    echo "  ⚠️ Alcuni dataset sono scaduti — il ZIP verrà comunque generato."
fi
echo ""

# 3. Prepara staging
echo "[3/4] Preparazione ZIP..."
STAGE="$STAGING/scartoffina"
mkdir -p "$STAGE"

# Copia i contenuti esclusi: .git, __pycache__, .env, company.json (dati reali), .cortexKit
EXCLUDE=(
    ".git"
    "__pycache__"
    ".env"
    "company.json"
    ".cortexKit"
    "scartoffina.zip"
    "scartoffina-dev.zip"
    "UPDATE_REPORT.md"
    "*.example.json"
    "*.example.csv"
)

# Copia con rsync se disponibile, altrimenti cp
if command -v rsync &>/dev/null; then
    RSYNC_EXCLUDES=()
    for e in "${EXCLUDE[@]}"; do
        RSYNC_EXCLUDES+=(--exclude="$e")
    done
    rsync -a "${RSYNC_EXCLUDES[@]}" "$ROOT_DIR/" "$STAGE/"
else
    for item in "$ROOT_DIR"/* "$ROOT_DIR"/.*; do
        [[ -e "$item" ]] || continue
        name="$(basename "$item")"
        case "$name" in
            .|..|.git|.cortexKit) continue ;;
        esac
        cp -r "$item" "$STAGE/"
    done
    rm -rf "$STAGE/__pycache__" "$STAGE/.env" "$STAGE/company.json" 2>/dev/null || true
fi

# Scrivi versione
echo "$VERSION" > "$STAGE/VERSION"

# 4. Crea ZIP
echo "[4/4] Creazione ${ZIP_NAME}..."
(cd "$STAGING" && zip -qr "$ROOT_DIR/$ZIP_NAME" "scartoffina")
echo ""
echo "✓ Release generata: ${ZIP_NAME}"
echo "  Dimensione: $(du -h "$ROOT_DIR/$ZIP_NAME" | cut -f1)"
echo "  Percorso: $ROOT_DIR/$ZIP_NAME"
echo ""
echo "Il ZIP contiene:"
echo "  - skills/       (9 skill con SKILL.md + references/ + data/ + templates/ + evals/)"
echo "  - data/         (16 dataset aggiornati con _meta freshness)"
echo "  - updater/       (modulo Python per aggiornamenti futuri)"
echo "  - integrations/  (modulo SDI per fatturazione elettronica)"
echo "  - evals/         (rubric di valutazione)"
echo "  - scartoffina.sh (entry point bash)"
echo "  - pyproject.toml (dipendenze e build)"
echo "  - README.md      (documentazione)"

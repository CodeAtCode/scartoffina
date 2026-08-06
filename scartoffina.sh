#!/usr/bin/env bash
# scartoffina.sh — entry point unico per Scartoffina
# Sostituisce il Makefile. Usage: ./scartoffina.sh <comando>
#
# Comandi:
#   install   — installa le dipendenze Python
#   update    — aggiorna tutti i dataset dalle fonti pubbliche
#   verify    — verifica freshness di tutti i dataset
#   eval      — esegue gli eval per tutte le skill
#   release   — scarica tutti i dataset e genera uno ZIP pronto al rilascio
#   help      — mostra questo aiuto

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PYTHON="${PYTHON:-python3}"
PIP="${PIP:-pip3}"

cmd_install() {
    "$PIP" install -e ".[dev]"
    echo "✓ Dipendenze installate."
}

cmd_update() {
    echo "Aggiornamento dataset..."
    "$PYTHON" -m updater.cli update ateco || true
    "$PYTHON" -m updater.cli update irpef || true
    "$PYTHON" -m updater.cli update imu || true
    "$PYTHON" -m updater.cli update f24_codici || true
    echo "✓ Aggiornamento completo. Rivedi git diff data/ prima del commit."
}

cmd_verify() {
    "$PYTHON" -m updater.cli verify
}

cmd_eval() {
    "$PYTHON" -m updater.cli evals
}

cmd_release() {
    bash scripts/release.sh "$@"
}

cmd_help() {
    cat <<'HELP'
Scartoffina — comandi disponibili:

  install   Installa le dipendenze Python (pip install -e .[dev])
  update    Aggiorna tutti i dataset dalle fonti pubbliche
  verify    Verifica freshness di tutti i dataset
  eval      Esegue gli eval per tutte le skill
  release   Scarica tutti i dataset e genera uno ZIP pronto al rilascio
  help      Mostra questo aiuto

Esempi:
  ./scartoffina.sh install
  ./scartoffina.sh update
  ./scartoffina.sh release 0.2.0
HELP
}

case "${1:-help}" in
    install)  cmd_install ;;
    update)   cmd_update ;;
    verify)   cmd_verify ;;
    eval)     cmd_eval ;;
    release)  shift; cmd_release "$@" ;;
    help|--help|-h) cmd_help ;;
    *) echo "Comando sconosciuto: $1"; cmd_help; exit 1 ;;
esac

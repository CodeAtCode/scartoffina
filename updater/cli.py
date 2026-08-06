"""
CLI entry point per l'updater di Scartoffina.

Usage:
    python3 -m updater.cli update <dataset>
    python3 -m updater.cli verify
    python3 -m updater.cli report
    python3 -m updater.cli evals
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from updater.validators.freshness import check_all, check_freshness, format_alert, get_summary
from updater.validators.schema import validate


DATASETS: dict[str, dict[str, str]] = {
    "ateco": {
        "source": "istat",
        "schema": "ateco",
        "output": "data/ateco.json",
    },
    "laws": {
        "source": "normattiva",
        "output": "references/laws/",
    },
    "irpef": {
        "source": "manual",
        "schema": "scaglioni-irpef",
        "output": "data/scaglioni-irpef.json",
    },
    "imu": {
        "source": "manual",
        "schema": "imu-aliquote",
        "output": "data/imu-aliquote.json",
    },
    "f24_codici": {
        "source": "manual",
        "schema": "codici-tributo-f24",
        "output": "data/codici-tributo-f24.json",
    },
}


def _check_manual_freshness(output_path: str) -> int:
    """Verifica freshness di un dataset manuale esistente."""
    p = Path(output_path)
    if not p.exists():
        print(f"     File non trovato: {output_path}")
        return 1

    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)

    result = check_freshness(data, output_path)
    icon = {"fresh": "✅", "stale": "🟡", "overdue": "🔴"}[result.status]
    print(f"     {icon} Stato: {result.status}")
    print(f"     Verificato: {result.verified_at[:10]}")
    print(f"     Prossima verifica: {result.next_check_due[:10]}")
    if result.days_overdue > 0:
        print(f"     ⚠️ Giorni scaduto: {result.days_overdue}")
    return 0


def cmd_update(args: argparse.Namespace) -> int:
    dataset: str = args.dataset
    if dataset not in DATASETS:
        print(f"Dataset sconosciuto: {dataset}")
        print(f"Disponibili: {', '.join(DATASETS.keys())}")
        return 1

    config = DATASETS[dataset]
    source = config["source"]
    output_path = config["output"]

    print(f"Aggiornamento dataset: {dataset}")
    print(f"  Fonte: {source}")
    print(f"  Output: {output_path}")

    if source == "istat":
        try:
            from updater.sources.istat import IstatClient

            client = IstatClient(
                base_url="https://esploradati.istat.it/SDMXWS/rest",
                cache_dir="updater/.cache",
            )
            data = client.get_ateco()

            schema_name = config.get("schema")
            if schema_name:
                is_valid, errors = validate(data, schema_name)
                if not is_valid:
                    print("  ❌ Validazione fallita:")
                    for e in errors:
                        print(f"     - {e}")
                    return 1

            out_path = Path(output_path)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"  ✅ Aggiornato: {output_path}")
            return 0

        except Exception as e:
            print(f"  ❌ Errore ISTAT: {e}")
            return 1

    if source == "normattiva":
        try:
            from updater.sources.normattiva import NormattivaClient

            client = NormattivaClient(
                base_url="https://api.normattiva.it/bff-opendata/v1",
                cache_dir="updater/.cache",
            )
            # Skeleton: il parser specifico va implementato per ogni dataset
            print(f"  ℹ️ Connector Normattiva disponibile — parser da implementare per '{dataset}'")
            return 0

        except Exception as e:
            print(f"  ❌ Errore Normattiva: {e}")
            return 1

    if source == "manual":
        print("  ⚠️ Dataset manuale — verifica freshness:")
        return _check_manual_freshness(output_path)

    print(f"  ❌ Fonte non supportata: {source}")
    return 1


def cmd_verify(args: argparse.Namespace) -> int:
    data_dir = "data"
    print(f"Verifica freshness dataset in: {data_dir}/")
    print()

    results = check_all(data_dir)
    if not results:
        print("  Nessun dataset trovato.")
        return 0

    for r in results:
        icon = {"fresh": "✅", "stale": "🟡", "overdue": "🔴"}.get(r.status, "❓")
        name = Path(r.file_path).name
        due = r.next_check_due[:10] if r.next_check_due else "N/A"
        print(f"  {icon} {name}: {r.status} (scade: {due})")

    summary = get_summary(data_dir)
    print()
    print(
        f"Riepilogo: {summary['fresh']} freschi, "
        f"{summary['stale']} in scadenza, "
        f"{summary['overdue']} scaduti"
    )
    return 0 if summary["overdue"] == 0 else 1


def cmd_report(args: argparse.Namespace) -> int:
    data_dir = "data"
    results = check_all(data_dir)
    alert = format_alert(results)

    output = "UPDATE_REPORT.md"
    with open(output, "w", encoding="utf-8") as f:
        f.write(alert)

    print(f"Report generato: {output}")
    return 0


def cmd_evals(args: argparse.Namespace) -> int:
    print("Esecuzione evals — da implementare")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="scartoffina-updater",
        description="Updater CLI per Scartoffina",
    )
    subparsers = parser.add_subparsers(dest="command", help="Comando")

    # update <dataset>
    update_parser = subparsers.add_parser("update", help="Aggiorna un dataset")
    update_parser.add_argument(
        "dataset",
        help="Nome del dataset (ateco, laws, irpef, imu, f24_codici)",
    )

    # verify
    subparsers.add_parser("verify", help="Verifica freshness di tutti i dataset")

    # report
    subparsers.add_parser("report", help="Genera UPDATE_REPORT.md")

    # evals
    subparsers.add_parser("evals", help="Esegue gli eval")

    args = parser.parse_args()

    if args.command == "update":
        return cmd_update(args)
    if args.command == "verify":
        return cmd_verify(args)
    if args.command == "report":
        return cmd_report(args)
    if args.command == "evals":
        return cmd_evals(args)

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())

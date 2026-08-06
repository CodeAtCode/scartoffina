"""
Generatore di report di aggiornamento.

Crea report markdown dettagliati sulle operazioni di aggiornamento
dei dataset, con statistiche e note operative.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class UpdateRecord:
    """
    Record di un singolo aggiornamento di dataset.

    Attributes:
        dataset: Nome del dataset aggiornato (es. "ateco", "irpef")
        source: Fonte dei dati (es. "istat", "normattiva")
        status: Stato dell'aggiornamento ("updated", "unchanged", "error")
        old_count: Numero di record prima dell'aggiornamento (opzionale)
        new_count: Numero di record dopo l'aggiornamento (opzionale)
        timestamp: Timestamp ISO dell'operazione
        notes: Note operative o messaggi di errore
    """

    dataset: str
    source: str
    status: str  # "updated" | "unchanged" | "error"
    old_count: int | None
    new_count: int | None
    timestamp: str
    notes: str = ""


def generate_report(records: list[UpdateRecord]) -> str:
    """
    Genera un report markdown dagli update records.

    Crea un report formattato con:
    - Timestamp del report
    - Tabella dettagliata degli aggiornamenti
    - Statistiche di sintesi

    Args:
        records: Lista di UpdateRecord da includere nel report

    Returns:
        String markdown formattata pronta per essere scritta su file
    """
    lines: list[str] = []

    # Header
    report_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    lines.append("# Report Aggiornamento Dataset")
    lines.append("")
    lines.append(f"**Generato:** {report_time}")
    lines.append("")

    # Tabella dettagliata
    lines.append("## Dettaglio Aggiornamenti")
    lines.append("")
    lines.append("| Dataset | Fonte | Stato | Vecchio conteggio | Nuovo conteggio | Note |")
    lines.append("|---------|-------|-------|-------------------|-----------------|------|")

    for record in records:
        # Icona per stato
        if record.status == "updated":
            status_icon = "✅"
        elif record.status == "unchanged":
            status_icon = "➖"
        else:  # error
            status_icon = "❌"

        status_display = f"{status_icon} {record.status.upper()}"

        old_count = (
            str(record.old_count)
            if record.old_count is not None
            else "N/A"
        )
        new_count = (
            str(record.new_count)
            if record.new_count is not None
            else "N/A"
        )

        notes = record.notes.replace("|", "\\|") if record.notes else ""

        lines.append(
            f"| {record.dataset} | {record.source} | {status_display} | "
            f"{old_count} | {new_count} | {notes} |"
        )

    lines.append("")

    # Statistiche
    lines.append("## Riepilogo")
    lines.append("")

    updated_count = sum(1 for r in records if r.status == "updated")
    unchanged_count = sum(1 for r in records if r.status == "unchanged")
    error_count = sum(1 for r in records if r.status == "error")

    lines.append(f"- **Dataset aggiornati:** {updated_count}")
    lines.append(f"- **Dataset invariati:** {unchanged_count}")
    lines.append(f"- **Errori:** {error_count}")
    lines.append(f"- **Totale elaborati:** {len(records)}")
    lines.append("")

    # Dettaglio per fonte
    sources: dict[str, list[UpdateRecord]] = {}
    for record in records:
        if record.source not in sources:
            sources[record.source] = []
        sources[record.source].append(record)

    if len(sources) > 1:
        lines.append("### Per fonte")
        lines.append("")
        for source, source_records in sorted(sources.items()):
            source_updated = sum(1 for r in source_records if r.status == "updated")
            source_errors = sum(1 for r in source_records if r.status == "error")
            lines.append(
                f"- **{source}:** {source_updated} aggiornati, "
                f"{source_errors} errori"
            )
        lines.append("")

    # Errori dettagliati
    if error_count > 0:
        lines.append("## Errori")
        lines.append("")
        for record in records:
            if record.status == "error":
                lines.append(f"### {record.dataset}")
                lines.append("")
                lines.append(f"- **Fonte:** {record.source}")
                lines.append(f"- **Errore:** {record.notes or 'Non specificato'}")
                lines.append("")

    # Footer
    lines.append("---")
    lines.append(f"*Report generato automaticamente da Scartoffina Updater*")

    return "\n".join(lines)


def write_report(records: list[UpdateRecord], output_path: str) -> None:
    """
    Scrive il report su file.

    Genera il report markdown e lo scrive nel percorso specificato.
    Crea le directory intermedie se non esistono.

    Args:
        records: Lista di UpdateRecord da includere nel report
        output_path: Percorso del file di output (es. "UPDATE_REPORT.md")
    """
    report_content = generate_report(records)

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report_content)


def create_success_record(
    dataset: str,
    source: str,
    old_count: int | None,
    new_count: int,
    notes: str = "",
) -> UpdateRecord:
    """
    Crea un record di aggiornamento riuscito.

    Convenience function per creare record con status "updated".

    Args:
        dataset: Nome del dataset
        source: Fonte dei dati
        old_count: Conteggio precedente (None se nuovo dataset)
        new_count: Nuovo conteggio
        notes: Note opzionali

    Returns:
        UpdateRecord con status "updated"
    """
    return UpdateRecord(
        dataset=dataset,
        source=source,
        status="updated",
        old_count=old_count,
        new_count=new_count,
        timestamp=datetime.utcnow().isoformat() + "Z",
        notes=notes,
    )


def create_unchanged_record(
    dataset: str,
    source: str,
    count: int,
    notes: str = "",
) -> UpdateRecord:
    """
    Crea un record per dataset invariato.

    Convenience function per creare record con status "unchanged".

    Args:
        dataset: Nome del dataset
        source: Fonte dei dati
        count: Numero di record (invariato)
        notes: Note opzionali

    Returns:
        UpdateRecord con status "unchanged"
    """
    return UpdateRecord(
        dataset=dataset,
        source=source,
        status="unchanged",
        old_count=count,
        new_count=count,
        timestamp=datetime.utcnow().isoformat() + "Z",
        notes=notes or "Dati non modificati dalla fonte",
    )


def create_error_record(
    dataset: str,
    source: str,
    error_message: str,
    old_count: int | None = None,
) -> UpdateRecord:
    """
    Crea un record per aggiornamento fallito.

    Convenience function per creare record con status "error".

    Args:
        dataset: Nome del dataset
        source: Fonte dei dati
        error_message: Messaggio di errore
        old_count: Conteggio precedente (se disponibile)

    Returns:
        UpdateRecord con status "error"
    """
    return UpdateRecord(
        dataset=dataset,
        source=source,
        status="error",
        old_count=old_count,
        new_count=None,
        timestamp=datetime.utcnow().isoformat() + "Z",
        notes=error_message,
    )
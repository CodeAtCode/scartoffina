"""
Controllo freschezza dei dati.

Verifica la validità temporale dei dataset controllando i metadati
_di ciascun file JSON e genera alert per dati scaduti o in scadenza.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


@dataclass
class FreshnessResult:
    """
    Risultato del controllo freschezza per un singolo file.

    Attributes:
        file_path: Percorso assoluto del file controllato
        status: Stato della freschezza ("fresh", "stale", "overdue")
        verified_at: Timestamp dell'ultima verifica (da _meta)
        next_check_due: Timestamp della prossima verifica prevista (da _meta)
        days_overdue: Giorni di ritardo (positivo se overdue, 0 altrimenti)
    """

    file_path: str
    status: str  # "fresh" | "stale" | "overdue"
    verified_at: str
    next_check_due: str
    days_overdue: int


def check_freshness(data: dict[str, Any], file_path: str = "") -> FreshnessResult:
    """
    Controlla la freschezza di un dataset dai suoi metadati.

    Analizza il blocco _meta del dataset e confronta i timestamp
    con la data corrente per determinare lo stato di freschezza.

    Args:
        data: Dict contenente il dataset con blocco _meta
        file_path: Percorso del file (opzionale, per reporting)

    Returns:
        FreshnessResult con lo stato di freschezza

    Raises:
        ValueError: Se _meta è mancante o incompleto
    """
    if "_meta" not in data:
        raise ValueError(f"File {file_path}: missing '_meta' block")

    meta = data["_meta"]

    # Campi obbligatori
    required_fields = [
        "verified_at", "next_check_due", "source", "tier"
    ]
    for field in required_fields:
        if field not in meta:
            raise ValueError(
                f"File {file_path}: missing required meta field '{field}'"
            )

    verified_at_str = meta["verified_at"]
    next_check_due_str = meta["next_check_due"]

    # Parse dei timestamp ISO 8601
    try:
        verified_at = datetime.fromisoformat(
            verified_at_str.replace("Z", "+00:00")
        )
    except ValueError:
        verified_at = datetime.utcnow()

    try:
        next_check_due = datetime.fromisoformat(
            next_check_due_str.replace("Z", "+00:00")
        )
    except ValueError:
        next_check_due = datetime.utcnow()

    # Normalizza a UTC per confronto
    now = datetime.utcnow()

    # Rimuovi timezone info per confronto (assumiamo UTC)
    if verified_at.tzinfo is not None:
        verified_at = verified_at.replace(tzinfo=None)
    if next_check_due.tzinfo is not None:
        next_check_due = next_check_due.replace(tzinfo=None)

    # Determina lo stato
    if now > next_check_due:
        # Scaduto
        days_overdue = (now - next_check_due).days
        status = "overdue"
    elif now > verified_at + timedelta(days=30):
        # Vicino alla scadenza (entro 7 giorni da next_check_due)
        days_until_due = (next_check_due - now).days
        if days_until_due <= 7:
            status = "stale"
            days_overdue = 0
        else:
            status = "fresh"
            days_overdue = 0
    else:
        status = "fresh"
        days_overdue = 0

    return FreshnessResult(
        file_path=file_path,
        status=status,
        verified_at=verified_at_str,
        next_check_due=next_check_due_str,
        days_overdue=days_overdue,
    )


def check_all(data_dir: str) -> list[FreshnessResult]:
    """
    Scansiona tutti i file JSON in una directory e controlla la freschezza.

    Args:
        data_dir: Percorso della directory da scansionare

    Returns:
        Lista di FreshnessResult ordinata per days_overdue decrescente
        (i più scaduti prima)
    """
    results: list[FreshnessResult] = []
    data_path = Path(data_dir)

    if not data_path.exists():
        return results

    # Scansiona ricorsivamente tutti i file JSON
    for json_file in data_path.rglob("*.json"):
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            result = check_freshness(data, str(json_file))
            results.append(result)

        except json.JSONDecodeError as e:
            # File JSON corrotto
            results.append(FreshnessResult(
                file_path=str(json_file),
                status="overdue",
                verified_at="",
                next_check_due="",
                days_overdue=999,  # Max penalty
            ))
        except ValueError as e:
            # Metadati mancanti o incompleti
            results.append(FreshnessResult(
                file_path=str(json_file),
                status="overdue",
                verified_at="",
                next_check_due="",
                days_overdue=999,
            ))
        except Exception:
            # Altri errori di lettura
            continue

    # Ordina per days_overdue decrescente
    results.sort(key=lambda r: r.days_overdue, reverse=True)

    return results


def format_alert(results: list[FreshnessResult]) -> str:
    """
    Formatta un alert markdown per dataset scaduti o in scadenza.

    Genera un report leggibile per l'invio via email, Slack o
    inserimento in log di monitoraggio.

    Args:
        results: Lista di FreshnessResult da includere nell'alert

    Returns:
        String markdown formattata con l'alert
    """
    # Filtra solo i risultati non freschi
    stale_overdue = [r for r in results if r.status in ("stale", "overdue")]

    if not stale_overdue:
        return "✅ Tutti i dataset sono aggiornati."

    lines: list[str] = []

    # Header
    lines.append("## ⚠️ Alert Freschezza Dataset")
    lines.append("")
    lines.append(f"Data controllo: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("")

    # Statistiche
    overdue_count = sum(1 for r in stale_overdue if r.status == "overdue")
    stale_count = sum(1 for r in stale_overdue if r.status == "stale")

    lines.append("### Riepilogo")
    lines.append("")
    lines.append(f"- **Dataset scaduti (overdue):** {overdue_count}")
    lines.append(f"- **Dataset in scadenza (stale):** {stale_count}")
    lines.append("")

    # Tabella dettagliata
    lines.append("### Dettagli")
    lines.append("")
    lines.append("| File | Stato | Verificato il | Scade il | Giorni scaduto |")
    lines.append("|------|-------|---------------|----------|----------------|")

    for result in stale_overdue:
        file_name = Path(result.file_path).name
        verified = result.verified_at[:10] if result.verified_at else "N/A"
        due = result.next_check_due[:10] if result.next_check_due else "N/A"
        days = result.days_overdue

        # Icona per stato
        icon = "🔴" if result.status == "overdue" else "🟡"
        status_display = f"{icon} {result.status.upper()}"

        lines.append(
            f"| `{file_name}` | {status_display} | {verified} | {due} | {days} |"
        )

    lines.append("")

    # Azioni raccomandate
    if overdue_count > 0:
        lines.append("### Azioni raccomandate")
        lines.append("")
        lines.append("1. **Priorità alta:** aggiornare i dataset scaduti immediatamente")
        lines.append("2. Verificare la disponibilità dei dati dalle fonti originali")
        lines.append("3. Aggiornare il blocco `_meta` dopo il refresh")
        lines.append("")

    lines.append("---")
    lines.append("*Generato automaticamente da Scartoffina Updater*")

    return "\n".join(lines)


def get_summary(data_dir: str) -> dict[str, int]:
    """
    Ottiene un riepilogo numerico dello stato di freschezza.

    Args:
        data_dir: Percorso della directory da scansionare

    Returns:
        Dict con conteggi per stato: {"fresh": N, "stale": N, "overdue": N}
    """
    results = check_all(data_dir)

    summary = {"fresh": 0, "stale": 0, "overdue": 0}
    for result in results:
        if result.status in summary:
            summary[result.status] += 1

    return summary
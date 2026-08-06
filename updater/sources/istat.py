"""
Client ISTAT per SDMX REST API.

Connettore per l'estrazione dati dall'ISTAT (Istituto Nazionale di Statistica)
tramite l'interfaccia SDMX REST. Implementa rate limiting rigoroso per evitare
il blocco dell'IP (1-2 giorni se superato).
"""

from __future__ import annotations

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests
from requests import Response


class IstatClient:
    """
    Client per l'API SDMX REST dell'ISTAT.

    Implementa un rate limiter a sliding window con max 5 richieste al minuto.
    Cache locale per le risposte raw.
    """

    def __init__(self, base_url: str, cache_dir: str) -> None:
        """
        Inizializza il client ISTAT.

        Args:
            base_url: URL base dell'API SDMX REST (es. https://esploradati.istat.it/SDMXWS/rest)
            cache_dir: Directory per la cache delle risposte raw
        """
        self.base_url = base_url.rstrip("/")
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Rate limiter: max 5 richieste al minuto
        self.rate_limit = 5
        self.request_timestamps: list[float] = []

        self._session = requests.Session()
        self._session.headers.update({
            "User-Agent": "Scartoffina-Updater/1.0",
            "Accept": "application/sdmx+xml, application/json",
        })

    def _fetch(self, path: str, params: dict[str, Any] | None = None) -> Response:
        """
        Esegue una richiesta HTTP con rate limiting e caching.

        Args:
            path: Percorso relativo all'API (es. "/dataflow")
            params: Parametri query opzionali

        Returns:
            Response object da requests

        Raises:
            RuntimeError: Se il rate limit è stato superato
            requests.HTTPError: Per errori HTTP
        """
        # Rate limiting: sliding window
        now = time.time()
        # Rimuovi timestamp più vecchi di 60 secondi
        self.request_timestamps = [
            ts for ts in self.request_timestamps
            if now - ts < 60
        ]

        if len(self.request_timestamps) >= self.rate_limit:
            # Calcola quanto aspettare
            oldest = min(self.request_timestamps)
            wait_time = 60 - (now - oldest)
            if wait_time > 0:
                time.sleep(wait_time)
                # Aggiorna la lista dopo l'attesa
                now = time.time()
                self.request_timestamps = [
                    ts for ts in self.request_timestamps
                    if now - ts < 60
                ]

        # Aggiungi timestamp corrente
        self.request_timestamps.append(time.time())

        url = f"{self.base_url}{path}"
        response = self._session.get(url, params=params, timeout=30)

        if response.status_code >= 400:
            raise requests.HTTPError(
                f"HTTP {response.status_code}: {response.text[:200]}"
            )

        return response

    def _cache_response(self, cache_key: str, content: bytes) -> None:
        """
        Salva una risposta raw nella cache.

        Args:
            cache_key: Nome del file di cache (es. "ateco_raw.xml")
            content: Contenuto binario da salvare
        """
        cache_path = self.cache_dir / cache_key
        cache_path.write_bytes(content)

    def get_ateco(self) -> dict[str, Any]:
        """
        Recupera la classificazione ATECO 2025 dall'API SDMX.

        L'ATECO è la classificazione statistica delle attività economiche.
        Utilizza il formato SDMX per ottenere la struttura delle categorie.

        Returns:
            Dict con la classificazione ATECO parsed.
            La struttura contiene:
            - categories: lista di nodi con codice, nome, livello
            - metadata: informazioni sulla versione e data di estrazione

        Note:
            La risposta raw viene salvata in cache_dir/ateco_raw.xml
        """
        # Endpoint SDMX per dataflow
        response = self._fetch("/dataflow/ISTAT/CL_ATECO2025/1.0")

        # Salva cache raw
        self._cache_response("ateco_raw.xml", response.content)

        # Parse della risposta SDMX (XML)
        # SDMX REST restituisce XML strutturato
        content = response.text

        # Estrazione semplice della struttura ATECO
        # In produzione, usare xmltodict o lxml per parsing completo
        result: dict[str, Any] = {
            "metadata": {
                "source": "istat",
                "source_url": f"{self.base_url}/dataflow/ISTAT/CL_ATECO2025/1.0",
                "fetched_at": datetime.utcnow().isoformat() + "Z",
                "version": "2025",
                "format": "sdmx",
            },
            "categories": [],
        }

        # Parsing base dell'XML SDMX
        # Nota: implementazione semplificata, in produzione usare parser SDMX completo
        try:
            import xml.etree.ElementTree as ET

            root = ET.fromstring(content)

            # Namespace SDMX
            namespaces = {
                "sdmx": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message",
                "structure": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure",
                "generic": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic",
            }

            # Estrai categorie (semplificato)
            for elem in root.iter():
                if "Codelist" in elem.tag or "Concept" in elem.tag:
                    category: dict[str, Any] = {}
                    if "id" in elem.attrib:
                        category["code"] = elem.attrib["id"]
                    for child in elem:
                        if "Name" in child.tag:
                            category["name"] = child.text
                    if category:
                        result["categories"].append(category)

        except Exception as e:
            result["metadata"]["parse_warning"] = f"XML parsing issue: {e}"

        return result

    def get_ipc(self, dataflow_id: str) -> dict[str, Any]:
        """
        Recupera gli indici IPC (Indice Prezzi al Consumo) / FOI.

        Args:
            dataflow_id: Identificatore del dataflow SDMX (es. "ISTAT/IPC_FOI/1.0")

        Returns:
            Dict con gli indici IPC parsed.
            La struttura contiene:
            - observations: lista di osservazioni con data, valore, unità
            - metadata: informazioni sulla serie

        Raises:
            requests.HTTPError: Se il dataflow non esiste o errore HTTP
        """
        response = self._fetch(f"/dataflow/{dataflow_id}")

        cache_key = f"ipc_{dataflow_id.replace('/', '_')}.xml"
        self._cache_response(cache_key, response.content)

        result: dict[str, Any] = {
            "metadata": {
                "source": "istat",
                "source_url": f"{self.base_url}/dataflow/{dataflow_id}",
                "fetched_at": datetime.utcnow().isoformat() + "Z",
                "dataflow_id": dataflow_id,
            },
            "observations": [],
        }

        try:
            import xml.etree.ElementTree as ET

            root = ET.fromstring(response.text)

            namespaces = {
                "sdmx": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message",
                "generic": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic",
            }

            # Estrai osservazioni (semplificato)
            for elem in root.iter():
                if "Obs" in elem.tag:
                    obs: dict[str, Any] = {}
                    for child in elem:
                        if "ObsValue" in child.tag and "value" in child.attrib:
                            obs["value"] = child.attrib["value"]
                        if "TimePeriod" in child.tag and child.text:
                            obs["date"] = child.text
                    if obs:
                        result["observations"].append(obs)

        except Exception as e:
            result["metadata"]["parse_warning"] = f"XML parsing issue: {e}"

        return result

    def get_codelist(self, codelist_id: str) -> dict[str, Any]:
        """
        Recupera un codelist specifico dall'API SDMX.

        Args:
            codelist_id: Identificatore del codelist (es. "CL_ATECO2025")

        Returns:
            Dict con il codelist parsed.
        """
        response = self._fetch(f"/codelist/ISTAT/{codelist_id}/1.0")

        cache_key = f"codelist_{codelist_id}.xml"
        self._cache_response(cache_key, response.content)

        result: dict[str, Any] = {
            "metadata": {
                "source": "istat",
                "codelist_id": codelist_id,
                "fetched_at": datetime.utcnow().isoformat() + "Z",
            },
            "values": [],
        }

        try:
            import xml.etree.ElementTree as ET

            root = ET.fromstring(response.text)

            for elem in root.iter():
                if "Code" in elem.tag:
                    code_entry: dict[str, Any] = {}
                    if "id" in elem.attrib:
                        code_entry["code"] = elem.attrib["id"]
                    for child in elem:
                        if "Name" in child.tag:
                            code_entry["name"] = child.text
                    if code_entry:
                        result["values"].append(code_entry)

        except Exception as e:
            result["metadata"]["parse_warning"] = f"XML parsing issue: {e}"

        return result
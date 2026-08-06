"""
Client Normattiva per OpenData API.

Connettore per l'estrazione dati dal portale Normattiva (legislazione italiana)
tramite l'API OpenData. Restituisce testi legislativi in formato Akoma Ntoso (AKN).
"""

from __future__ import annotations

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests
from requests import Response


class NormattivaClient:
    """
    Client per l'API OpenData di Normattiva.

    Implementa rate limiting di ~1 richiesta al secondo (documentato dalla
    community, non ufficiale). Le risposte sono in formato Akoma Ntoso (AKN) XML.

    License: CC BY 4.0 - repubblicazione consentita con attribuzione.
    """

    def __init__(self, base_url: str, cache_dir: str) -> None:
        """
        Inizializza il client Normattiva.

        Args:
            base_url: URL base dell'API (es. https://api.normattiva.it/bff-opendata/v1)
            cache_dir: Directory per la cache delle risposte
        """
        self.base_url = base_url.rstrip("/")
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Rate limiter: ~1 richiesta al secondo
        self.rate_limit_per_sec = 1
        self.last_request_time: float = 0

        self._session = requests.Session()
        self._session.headers.update({
            "User-Agent": "Scartoffina-Updater/1.0",
            "Accept": "application/xml, application/json",
        })

    def _fetch(self, path: str, params: dict[str, Any] | None = None) -> Response:
        """
        Esegue una richiesta HTTP con rate limiting e caching.

        Args:
            path: Percorso relativo all'API
            params: Parametri query opzionali

        Returns:
            Response object da requests

        Raises:
            requests.HTTPError: Per errori HTTP
        """
        # Rate limiting: almeno 1 secondo tra le richieste
        now = time.time()
        elapsed = now - self.last_request_time
        if elapsed < 1.0:
            time.sleep(1.0 - elapsed)

        self.last_request_time = time.time()

        url = f"{self.base_url}{path}"
        response = self._session.get(url, params=params, timeout=60)

        if response.status_code >= 400:
            raise requests.HTTPError(
                f"HTTP {response.status_code}: {response.text[:200]}"
            )

        return response

    def _cache_response(self, cache_key: str, content: bytes) -> None:
        """
        Salva una risposta nella cache.

        Args:
            cache_key: Nome del file di cache
            content: Contenuto binario da salvare
        """
        cache_path = self.cache_dir / cache_key
        cache_path.write_bytes(content)

    def get_law(self, urn: str) -> dict[str, Any]:
        """
        Recupera il testo di una legge in formato Akoma Ntoso (AKN).

        Args:
            urn: URN della legge (es. "urn:Legge:2021;118")

        Returns:
            Dict con la legge parsed. La struttura contiene:
            - urn: identificativo della legge
            - titolo: titolo della legge
            - data: data di approvazione
            - contenuto: testo strutturato AKN
            - metadata: informazioni aggiuntive

        Raises:
            requests.HTTPError: Se la legge non esiste o errore HTTP
        """
        # Endpoint per recuperare una legge specifica
        path = f"/legislazione/{urn}"

        response = self._fetch(path)

        # Cache con URN come chiave (sanitizzato)
        cache_key = f"law_{urn.replace(':', '_').replace(';', '_')}.xml"
        self._cache_response(cache_key, response.content)

        content = response.text

        result: dict[str, Any] = {
            "metadata": {
                "source": "normattiva",
                "source_url": f"{self.base_url}/legislazione/{urn}",
                "fetched_at": datetime.utcnow().isoformat() + "Z",
                "urn": urn,
                "format": "akoma_ntoso",
            },
            "data": {},
        }

        # Parsing base dell'XML AKN
        try:
            import xml.etree.ElementTree as ET

            root = ET.fromstring(content)

            # Namespace Akoma Ntoso
            namespaces = {
                "akn": "http://docs.oasis-open.org/legaldocml/ns/akn/3.0",
            }

            # Estrai metadati base
            meta_elem = root.find(".//akn:meta", namespaces)
            if meta_elem is not None:
                title_elem = meta_elem.find(".//akn:docTitle", namespaces)
                if title_elem is not None:
                    result["metadata"]["title"] = title_elem.text

                date_elem = meta_elem.find(".//akn:docDate", namespaces)
                if date_elem is not None:
                    result["metadata"]["date"] = date_elem.attrib.get("value", "")

            # Estrai contenuto principale
            body_elem = root.find(".//akn:body", namespaces)
            if body_elem is not None:
                result["data"]["body"] = ET.tostring(
                    body_elem, encoding="unicode", method="xml"
                )

        except Exception as e:
            result["metadata"]["parse_warning"] = f"XML parsing issue: {e}"

        return result

    def search(self, query: str, tipo_atto: str | None = None) -> list[dict[str, Any]]:
        """
        Cerca disposizioni legislative.

        Args:
            query: Parola chiave o frase da cercare
            tipo_atto: Tipo di atto opzionale (es. "legge", "decreto", "regolamento")

        Returns:
            Lista di dict con i risultati della ricerca. Ogni elemento contiene:
            - urn: identificativo della legge
            - titolo: titolo dell'atto
            - data: data dell'atto
            - tipo: tipo di atto
            - snippet: estratto contenente la ricerca

        Raises:
            requests.HTTPError: Per errori HTTP
        """
        params: dict[str, Any] = {
            "query": query,
            "format": "json",
        }

        if tipo_atto:
            params["tipo_atto"] = tipo_atto

        response = self._fetch("/cerca", params)

        cache_key = f"search_{hash(query) % 10000}_{tipo_atto or 'all'}.json"
        self._cache_response(cache_key, response.content)

        try:
            data = response.json()
        except json.JSONDecodeError:
            data = {}

        result: list[dict[str, Any]] = []

        # Parsing dei risultati (struttura dipende dall'API)
        if "risultati" in data:
            for item in data["risultati"]:
                result.append({
                    "urn": item.get("urn", ""),
                    "titolo": item.get("titolo", ""),
                    "data": item.get("data", ""),
                    "tipo": item.get("tipo_atto", ""),
                    "snippet": item.get("estratto", ""),
                })
        elif "results" in data:
            for item in data["results"]:
                result.append({
                    "urn": item.get("urn", ""),
                    "titolo": item.get("title", ""),
                    "data": item.get("date", ""),
                    "tipo": item.get("type", ""),
                    "snippet": item.get("snippet", ""),
                })

        return result

    def get_tuir(self) -> dict[str, Any]:
        """
        Recupera il TUIR (Testo Unico Imposte Redditi).

        Convenience method per ottenere l'intero TUIR (DPR 917/1986).

        Returns:
            Dict con il TUIR parsed. La struttura contiene:
            - urn: URN del TUIR
            - titolo: titolo completo
            - articoli: lista di articoli con numero e contenuto
            - metadata: informazioni sulla versione e data di estrazione
        """
        # URN del TUIR (DPR 917/1986)
        tuir_urn = "urn:DecretoPresidenzaConsiglioMinistri:1986;917"

        result = self.get_law(tuir_urn)

        # Aggiungi informazioni specifiche TUIR
        result["metadata"]["tuir_info"] = {
            "nome_comune": "TUIR",
            "nome_completo": "Testo Unico delle Imposte sui Redditi",
            "decreto": "DPR 917/1986",
        }

        # Estrai articoli dal contenuto AKN
        if result["data"].get("body"):
            import xml.etree.ElementTree as ET

            try:
                body = ET.fromstring(result["data"]["body"])
                namespaces = {"akn": "http://docs.oasis-open.org/legaldocml/ns/akn/3.0"}

                articoli = []
                for articolo in body.findall(".//akn:article", namespaces):
                    art_num = articolo.attrib.get("eId", "").split("_")[-1]
                    art_content = ET.tostring(
                        articolo, encoding="unicode", method="xml"
                    )
                    articoli.append({
                        "numero": art_num,
                        "contenuto": art_content,
                    })

                result["data"]["articoli"] = articoli
                result["data"]["articoli_count"] = len(articoli)

            except Exception:
                result["data"]["articoli"] = []
                result["data"]["articoli_count"] = 0

        return result

    def get_legge_finanziaria(self, anno: int) -> dict[str, Any]:
        """
        Recupera la legge di bilancio/finanziaria per un anno specifico.

        Args:
            anno: Anno di riferimento (es. 2024)

        Returns:
            Dict con la legge di bilancio parsed.
        """
        # Cerca la legge di bilancio per l'anno specificato
        query = f"legge di bilancio {anno}"
        results = self.search(query, tipo_atto="legge")

        if not results:
            return {
                "metadata": {
                    "source": "normattiva",
                    "search_query": query,
                    "anno_richiesto": anno,
                    "fetched_at": datetime.utcnow().isoformat() + "Z",
                },
                "data": {},
                "error": f"Nessuna legge di bilancio trovata per {anno}",
            }

        # Prendi il primo risultato (tipicamente il più recente/rilevante)
        primo_risultato = results[0]

        # Recupera il testo completo
        return self.get_law(primo_risultato["urn"])

    def get_decreto_legge(self, numero: int, anno: int) -> dict[str, Any]:
        """
        Recupera un decreto-legge specifico.

        Args:
            numero: Numero del decreto (es. 73)
            anno: Anno del decreto (es. 2024)

        Returns:
            Dict con il decreto-legge parsed.
        """
        # Cerca il decreto-legge
        query = f"decreto-legge {numero}/{anno}"
        results = self.search(query, tipo_atto="decreto-legge")

        if not results:
            return {
                "metadata": {
                    "source": "normattiva",
                    "search_query": query,
                    "fetched_at": datetime.utcnow().isoformat() + "Z",
                },
                "data": {},
                "error": f"Decreto-legge {numero}/{anno} non trovato",
            }

        return self.get_law(results[0]["urn"])
"""
Validazione JSON Schema per i file di dati.

Definisce gli schemi di validazione per i diversi dataset fiscali
e implementa la funzione di validazione con fallback manuale.
"""

from __future__ import annotations

from typing import Any

try:
    import jsonschema
    from jsonschema import Draft7Validator
    JSONSCHEMA_AVAILABLE = True
except ImportError:
    JSONSCHEMA_AVAILABLE = False


_META_SCHEMA: dict[str, Any] = {
    "type": "object",
    "required": [
        "source", "source_url", "fetched_at",
        "verified_at", "fetched_by", "tier", "next_check_due",
    ],
    "properties": {
        "source": {"type": "string", "minLength": 1},
        "source_url": {"type": "string"},
        "fetched_at": {"type": "string"},
        "verified_at": {"type": "string"},
        "fetched_by": {"type": "string"},
        "license": {"type": "string"},
        "tier": {"type": "string", "enum": ["open", "semi", "manual"]},
        "next_check_due": {"type": "string"},
        "note": {"type": "string"},
    },
}


SCHEMAS: dict[str, dict[str, Any]] = {
    "aliquote-iva": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "required": ["_meta", "aliquote"],
        "properties": {
            "_meta": _META_SCHEMA,
            "aliquote": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["codice", "aliquota", "descrizione"],
                    "properties": {
                        "codice": {"type": "string", "minLength": 1},
                        "aliquota": {"type": "number", "minimum": 0, "maximum": 1},
                        "descrizione": {"type": "string", "minLength": 1},
                        "riferimento_normativo": {"type": "string"},
                    },
                },
            },
            "operazioni_non_imponibili": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["descrizione"],
                    "properties": {
                        "descrizione": {"type": "string", "minLength": 1},
                        "riferimento_normativo": {"type": "string"},
                    },
                },
            },
        },
    },

    "scaglioni-irpef": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "required": ["_meta", "scaglioni"],
        "properties": {
            "_meta": _META_SCHEMA,
            "anno_imposta": {"type": "integer", "minimum": 2000, "maximum": 2100},
            "riferimento_normativo": {"type": "string"},
            "scaglioni": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["progressivo", "limite_inferiore", "aliquota"],
                    "properties": {
                        "progressivo": {"type": "integer", "minimum": 1},
                        "limite_inferiore": {"type": "integer", "minimum": 0},
                        "limite_superiore": {
                            "type": ["integer", "null"],
                            "minimum": 0,
                        },
                        "aliquota": {"type": "number", "minimum": 0, "maximum": 1},
                        "descrizione": {"type": "string"},
                    },
                },
            },
            "detrazioni_forfettarie": {"type": "object"},
            "no_tax_area": {"type": "object"},
        },
    },

    "codici-tributo-f24": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "required": ["_meta", "codici"],
        "properties": {
            "_meta": _META_SCHEMA,
            "anno_riferimento": {"type": "integer", "minimum": 2000, "maximum": 2100},
            "codici": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["codice", "descrizione", "ente"],
                    "properties": {
                        "codice": {"type": "string", "minLength": 1},
                        "descrizione": {"type": "string", "minLength": 1},
                        "ente": {"type": "string", "minLength": 1},
                    },
                },
            },
        },
    },

    "piano-conti-oic": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "required": ["_meta", "conti"],
        "properties": {
            "_meta": _META_SCHEMA,
            "riferimento_normativo": {"type": "string"},
            "conti": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["codice", "descrizione", "tipo", "classe"],
                    "properties": {
                        "codice": {"type": "string", "minLength": 1},
                        "descrizione": {"type": "string", "minLength": 1},
                        "tipo": {
                            "type": "string",
                            "enum": ["stato_patrimoniale", "conto_economico"],
                        },
                        "classe": {"type": "string", "minLength": 1},
                    },
                },
            },
        },
    },

    "calendario-fiscale": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "required": ["_meta", "anno", "scadenze"],
        "properties": {
            "_meta": _META_SCHEMA,
            "anno": {"type": "integer", "minimum": 2000, "maximum": 2100},
            "scadenze": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["mese", "giorno", "descrizione", "tipo"],
                    "properties": {
                        "mese": {"type": "integer", "minimum": 1, "maximum": 12},
                        "giorno": {"type": "integer", "minimum": 1, "maximum": 31},
                        "descrizione": {"type": "string", "minLength": 1},
                        "riferimento": {"type": "string"},
                        "tipo": {
                            "type": "string",
                            "enum": [
                                "iva", "ritenute", "contributi", "mensile",
                                "dichiarazione", "certificazione", "acconto",
                                "imu", "bilancio",
                            ],
                        },
                    },
                },
            },
        },
    },

    "ateco": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "required": ["_meta", "categories"],
        "properties": {
            "_meta": _META_SCHEMA,
            "categories": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["code", "name"],
                    "properties": {
                        "code": {"type": "string", "minLength": 1},
                        "name": {"type": "string", "minLength": 1},
                        "livello": {"type": "integer", "minimum": 1, "maximum": 6},
                        "parent": {"type": ["string", "null"]},
                        "note": {"type": "string"},
                    },
                },
            },
        },
    },

    "imu-aliquote": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "required": ["_meta", "aliquote"],
        "properties": {
            "_meta": _META_SCHEMA,
            "aliquote": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["comune", "tipo_immobile", "aliquota", "anno"],
                    "properties": {
                        "comune": {"type": "string", "minLength": 1},
                        "codice_istat": {"type": "string"},
                        "tipo_immobile": {
                            "type": "string",
                            "enum": [
                                "abitazione_principale", "seconda_casa",
                                "catastali_a", "catastali_b", "catastali_c",
                                "terreni", "fabbricati_strumentali",
                                "unita_montane",
                            ],
                        },
                        "aliquota": {"type": "number", "minimum": 0, "maximum": 1},
                        "detrazione": {"type": "number", "minimum": 0},
                        "anno": {"type": "integer", "minimum": 2000, "maximum": 2100},
                        "note": {"type": "string"},
                    },
                },
            },
        },
    },
}


def validate(data: dict[str, Any], schema_name: str) -> tuple[bool, list[str]]:
    """
    Valida un dict di dati contro uno schema predefinito.

    Args:
        data: Dict da validare
        schema_name: Nome dello schema (es. "aliquote-iva", "scaglioni-irpef")

    Returns:
        Tuple (is_valid, errors)

    Raises:
        ValueError: Se schema_name non è riconosciuto
    """
    if schema_name not in SCHEMAS:
        raise ValueError(
            f"Schema '{schema_name}' non riconosciuto. "
            f"Schema disponibili: {', '.join(SCHEMAS.keys())}"
        )

    schema = SCHEMAS[schema_name]

    if JSONSCHEMA_AVAILABLE:
        validator = Draft7Validator(schema)  # type: ignore[possibly-unbound]
        errors = list(validator.iter_errors(data))

        if not errors:
            return True, []

        error_messages = [
            f"{error.json_path}: {error.message}"
            for error in errors
        ]
        return False, error_messages

    return _manual_validate(data, schema)


def _manual_validate(data: dict[str, Any], schema: dict[str, Any]) -> tuple[bool, list[str]]:
    """Validazione manuale fallback quando jsonschema non è disponibile."""
    errors: list[str] = []

    if schema.get("type") == "object" and not isinstance(data, dict):
        errors.append("Expected object at root level")
        return False, errors

    required = schema.get("required", [])
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")

    if errors:
        return False, errors

    properties = schema.get("properties", {})
    for key, value in data.items():
        if key in properties:
            _validate_property(key, value, properties[key], errors)

    return len(errors) == 0, errors


def _validate_property(
    path: str,
    value: Any,
    schema: dict[str, Any],
    errors: list[str],
) -> None:
    """Valida una singola proprietà contro il suo schema."""
    expected_type = schema.get("type")

    if expected_type == "string" and not isinstance(value, str):
        errors.append(f"{path}: expected string, got {type(value).__name__}")
        return
    if expected_type == "number" and not isinstance(value, (int, float)):
        errors.append(f"{path}: expected number, got {type(value).__name__}")
        return
    if expected_type == "integer" and not isinstance(value, int):
        errors.append(f"{path}: expected integer, got {type(value).__name__}")
        return
    if expected_type == "boolean" and not isinstance(value, bool):
        errors.append(f"{path}: expected boolean, got {type(value).__name__}")
        return
    if expected_type == "array" and not isinstance(value, list):
        errors.append(f"{path}: expected array, got {type(value).__name__}")
        return
    if expected_type == "object" and not isinstance(value, dict):
        errors.append(f"{path}: expected object, got {type(value).__name__}")
        return

    if "enum" in schema and value not in schema["enum"]:
        errors.append(
            f"{path}: value '{value}' not in allowed values: {schema['enum']}"
        )

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: value must be '{schema['const']}', got '{value}'")

    if isinstance(value, (int, float)):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: value {value} below minimum {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{path}: value {value} above maximum {schema['maximum']}")

    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(
                f"{path}: string length {len(value)} below minimum {schema['minLength']}"
            )
        if "pattern" in schema:
            import re
            if not re.match(schema["pattern"], value):
                errors.append(
                    f"{path}: value '{value}' does not match pattern '{schema['pattern']}'"
                )

    if isinstance(value, list) and "items" in schema:
        item_schema = schema["items"]
        for i, item in enumerate(value):
            _validate_property(f"{path}[{i}]", item, item_schema, errors)

    if isinstance(value, dict):
        for key, val in value.items():
            if key in schema.get("properties", {}):
                _validate_property(
                    f"{path}.{key}",
                    val,
                    schema["properties"][key],
                    errors,
                )

"""Modulo SDI per fatturazione elettronica italiana (formato FPR12)."""

from .adapter import SDIAdapter, FatturaElettronica, EsitoTrasmissione

__all__ = ["SDIAdapter", "FatturaElettronica", "EsitoTrasmissione"]
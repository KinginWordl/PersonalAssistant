"""Configuración del asistente GoHan."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Ajustes del asistente.

    En etapas posteriores se cargarán desde archivo de configuración,
    variables de entorno y preferencias persistidas en SQLite.
    """

    assistant_name: str = "GoHan"
    language: str = "es-ES"


def create_settings() -> Settings:
    """Crea las settings con los valores por defecto."""
    return Settings()

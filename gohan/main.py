"""Composition Root del asistente GoHan."""

from gohan import __version__
from gohan.config import create_settings


def main() -> int:
    """Punto de entrada principal del asistente."""
    settings = create_settings()
    print(f"{settings.assistant_name} v{__version__} arrancando...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

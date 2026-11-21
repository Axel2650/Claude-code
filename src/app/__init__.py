"""Paquete principal del proyecto."""

__version__ = "0.1.0"


def saludar(nombre: str = "mundo") -> str:
    """Devuelve un saludo para ``nombre``."""
    return f"Hola, {nombre}!"

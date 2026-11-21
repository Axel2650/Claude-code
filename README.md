# Claude-code

Proyecto base en Python (>= 3.11) con estructura `src/`, pruebas con `pytest` y linting con `ruff`.

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Uso

```bash
app            # Hola, mundo!
app Axel       # Hola, Axel!
python -m app --version
```

## Desarrollo

```bash
pytest           # pruebas
ruff check .     # linting
ruff format .    # formato
```

## Estructura

```
src/app/         código del paquete
tests/           pruebas
pyproject.toml   metadatos, dependencias y configuración de herramientas
```

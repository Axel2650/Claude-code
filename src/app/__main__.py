import argparse

from app import __version__, saludar


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="app", description="Proyecto base en Python")
    parser.add_argument("nombre", nargs="?", default="mundo")
    parser.add_argument("--version", action="version", version=__version__)
    args = parser.parse_args(argv)
    print(saludar(args.nombre))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

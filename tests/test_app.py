from app import saludar
from app.__main__ import main


def test_saludar_por_defecto():
    assert saludar() == "Hola, mundo!"


def test_saludar_con_nombre():
    assert saludar("Axel") == "Hola, Axel!"


def test_main_imprime_saludo(capsys):
    assert main(["Python"]) == 0
    assert capsys.readouterr().out == "Hola, Python!\n"

import pytest
from src.proceso import Proceso

def test_proceso_valido():
    p = Proceso("P1", 5, 2)
    assert p.pid == "P1"
    assert p.duracion == 5
    assert p.prioridad == 2
    assert p.tiempo_restante == 5

def test_pid_vacio_lanza_error():
    with pytest.raises(ValueError):
        Proceso("", 5, 1)

def test_duracion_invalida():
    with pytest.raises(ValueError):
        Proceso("P2", 0, 1)


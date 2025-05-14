import os
import tempfile
from src.proceso import Proceso
from src.repositorio import RepositorioProcesos

def test_agregar_y_listar_procesos():
    repo = RepositorioProcesos()
    p1 = Proceso("P1", 10, 1)
    repo.agregar_proceso(p1)
    assert len(repo.listar()) == 1
    assert repo.obtener("P1") == p1

def test_pid_duplicado():
    repo = RepositorioProcesos()
    repo.agregar_proceso(Proceso("P1", 10, 1))
    try:
        repo.agregar_proceso(Proceso("P1", 5, 2))
        assert False, "Debió lanzar ValueError por PID duplicado"
    except ValueError:
        pass

def test_eliminar_proceso():
    repo = RepositorioProcesos()
    repo.agregar_proceso(Proceso("P1", 10, 1))
    repo.eliminar("P1")
    assert len(repo.listar()) == 0

def test_guardar_y_cargar_json():
    repo = RepositorioProcesos()
    repo.agregar_proceso(Proceso("P1", 10, 1))

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        repo.guardar_json(tmp.name)
        ruta = tmp.name

    nuevo_repo = RepositorioProcesos()
    nuevo_repo.cargar_json(ruta)
    assert len(nuevo_repo.listar()) == 1
    os.remove(ruta)

def test_guardar_y_cargar_csv():
    repo = RepositorioProcesos()
    repo.agregar_proceso(Proceso("P1", 10, 1))

    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        repo.guardar_csv(tmp.name)
        ruta = tmp.name

    nuevo_repo = RepositorioProcesos()
    nuevo_repo.cargar_csv(ruta)
    assert len(nuevo_repo.listar()) == 1
    os.remove(ruta)

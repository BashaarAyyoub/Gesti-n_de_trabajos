import pytest
from src.proceso import Proceso
from src.scheduler.fcfs_scheduler import FCFSScheduler
from src.scheduler.round_robin_scheduler import RoundRobinScheduler
from src.repositorio import RepositorioProcesos

def test_fcfs_scheduler():
    repo = RepositorioProcesos()
    p1 = Proceso("P1", 5, 2)
    p2 = Proceso("P2", 3, 1)
    p3 = Proceso("P3", 4, 3)
    repo.agregar_proceso(p1)
    repo.agregar_proceso(p2)
    repo.agregar_proceso(p3)

    scheduler = FCFSScheduler()
    gantt = scheduler.planificar(repo.listar_procesos())

    assert gantt == [("P2", 0, 3), ("P1", 3, 8), ("P3", 8, 12)]

def test_round_robin_scheduler():
    repo = RepositorioProcesos()
    p1 = Proceso("P1", 5, 2)
    p2 = Proceso("P2", 3, 1)
    p3 = Proceso("P3", 4, 3)
    repo.agregar_proceso(p1)
    repo.agregar_proceso(p2)
    repo.agregar_proceso(p3)

    scheduler = RoundRobinScheduler(2)
    gantt = scheduler.planificar(repo.listar_procesos())

    assert gantt == [("P2", 0, 2), ("P1", 2, 4), ("P3", 4, 6), ("P1", 6, 8), ("P3", 8, 10), ("P1", 10, 12)]


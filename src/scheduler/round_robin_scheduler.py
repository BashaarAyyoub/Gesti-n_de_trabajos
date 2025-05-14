from typing import List, Tuple
import sys
import os

# Ajuste para resolver importación en ejecución directa
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from proceso import Proceso
from scheduler.scheduler_base import Scheduler

GanttEntry = Tuple[str, int, int]

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        if quantum <= 0:
            raise ValueError("El quantum debe ser mayor a 0.")
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        tiempo_actual = 0
        gantt: List[GanttEntry] = []
        cola = procesos.copy()

        for p in cola:
            p.tiempo_restante = p.duracion
            p.tiempo_inicio = None  # Se establece cuando se ejecuta por primera vez

        while any(p.tiempo_restante > 0 for p in cola):
            for p in cola:
                if p.tiempo_restante <= 0:
                    continue
                if p.tiempo_inicio is None:
                    p.tiempo_inicio = tiempo_actual

                tiempo_ejecucion = min(self.quantum, p.tiempo_restante)
                tiempo_inicio = tiempo_actual
                tiempo_actual += tiempo_ejecucion
                tiempo_fin = tiempo_actual
                p.tiempo_restante -= tiempo_ejecucion

                if p.tiempo_restante == 0:
                    p.tiempo_fin = tiempo_actual

                gantt.append((p.pid, tiempo_inicio, tiempo_fin))

        return gantt

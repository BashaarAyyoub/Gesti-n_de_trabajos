from typing import List, Tuple
import sys
import os

# Ajuste para resolver importación en ejecución directa
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from proceso import Proceso
from scheduler.scheduler_base import Scheduler

GanttEntry = Tuple[str, int, int]

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        tiempo_actual = 0
        gantt: List[GanttEntry] = []

        for p in procesos:
            p.tiempo_inicio = tiempo_actual
            p.tiempo_fin = tiempo_actual + p.duracion
            gantt.append((p.pid, p.tiempo_inicio, p.tiempo_fin))
            tiempo_actual += p.duracion

        return gantt

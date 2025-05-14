from abc import ABC, abstractmethod
from typing import List, Tuple
from src.proceso import Proceso

# Definición de tipo para las entradas del diagrama de Gantt
GanttEntry = Tuple[str, int, int]

class Scheduler(ABC):
    """
    Clase abstracta que define la interfaz común para los planificadores de CPU.
    Cada planificador debe implementar el método `planificar`.
    """
    
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """
        Método que debe ser implementado por los planificadores concretos para
        planificar la ejecución de los procesos y generar el diagrama de Gantt.

        Parámetros:
            procesos (List[Proceso]): Lista de objetos de tipo Proceso que se van a planificar.

        Retorna:
            List[GanttEntry]: Lista de tuplas (pid, tiempo_inicio, tiempo_fin) que representan el diagrama de Gantt.
        """
        pass

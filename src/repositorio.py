import json, csv
from typing import List
from src.proceso import Proceso

class RepositorioProcesos:
    def __init__(self):
        self.procesos: List[Proceso] = []

    def agregar_proceso(self, proceso: Proceso):
        if any(p.pid == proceso.pid for p in self.procesos):
            raise ValueError(f"Ya existe un proceso con PID {proceso.pid}")
        self.procesos.append(proceso)

    def listar(self) -> List[Proceso]:
        return self.procesos

    def eliminar(self, pid: str):
        self.procesos = [p for p in self.procesos if p.pid != pid]

    def obtener(self, pid: str) -> Proceso:
        return next((p for p in self.procesos if p.pid == pid), None)

    def guardar_json(self, ruta: str):
        with open(ruta, 'w') as f:
            json.dump([p.__dict__ for p in self.procesos], f)

    def cargar_json(self, ruta: str):
        with open(ruta, 'r') as f:
            data = json.load(f)
        self.procesos = [Proceso(**{k: v for k, v in d.items() if k in ['pid', 'duracion', 'prioridad']}) for d in data]

    def guardar_csv(self, ruta: str):
        with open(ruta, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['pid', 'duracion', 'prioridad'])
            for p in self.procesos:
                writer.writerow([p.pid, p.duracion, p.prioridad])

    def cargar_csv(self, ruta: str):
        with open(ruta, 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            self.procesos = [Proceso(row['pid'], int(row['duracion']), int(row['prioridad'])) for row in reader]

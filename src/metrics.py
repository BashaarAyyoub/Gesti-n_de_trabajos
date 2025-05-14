from typing import List
from src.proceso import Proceso

def calcular_metricas(procesos: List[Proceso]):
    n = len(procesos)
    tiempos_respuesta = [p.tiempo_inicio - p.tiempo_llegada for p in procesos]
    tiempos_retorno = [p.tiempo_fin - p.tiempo_llegada for p in procesos]
    tiempos_espera = [ret - p.duracion for ret, p in zip(tiempos_retorno, procesos)]
    return {
        'respuesta_prom': sum(tiempos_respuesta) / n,
        'retorno_prom': sum(tiempos_retorno) / n,
        'espera_prom': sum(tiempos_espera) / n
    }

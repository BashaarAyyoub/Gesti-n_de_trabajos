import pytest
from src.proceso import Proceso
from src.metrics import calcular_metricas

def test_metricas_fcfs_ejemplo():
    # Crear procesos con duración conocida
    p1 = Proceso("P1", 5, 1)
    p2 = Proceso("P2", 3, 2)
    p3 = Proceso("P3", 2, 3)

    # Asumimos llegada en t=0 para todos
    # Simulamos ejecución FCFS:
    # P1: 0 -> 5
    # P2: 5 -> 8
    # P3: 8 -> 10

    p1.tiempo_inicio, p1.tiempo_fin = 0, 5
    p2.tiempo_inicio, p2.tiempo_fin = 5, 8
    p3.tiempo_inicio, p3.tiempo_fin = 8, 10

    procesos = [p1, p2, p3]

    metricas = calcular_metricas(procesos)

    # Esperados:
    # Respuesta: [0, 5, 8]
    # Retorno: [5, 8, 10]
    # Espera: [0, 5, 8] - [5, 3, 2] = [0, 2, 6]
    assert metricas["tiempo_respuesta_promedio"] == pytest.approx((0 + 5 + 8) / 3)
    assert metricas["tiempo_retorno_promedio"] == pytest.approx((5 + 8 + 10) / 3)
    assert metricas["tiempo_espera_promedio"] == pytest.approx((0 + 2 + 6) / 3)


import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from proceso import Proceso
from scheduler.fcfs_scheduler import FCFSScheduler
from scheduler.round_robin_scheduler import RoundRobinScheduler
from repositorio import RepositorioProcesos


def mostrar_menu():
    print("----- Menú -----")
    print("1. Agregar proceso")
    print("2. Listar procesos")
    print("3. Ejecutar FCFS")
    print("4. Ejecutar Round Robin")
    print("5. Salir")
    print("---------------")

def main():
    repo = RepositorioProcesos()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            pid = input("PID del proceso: ")
            duracion = int(input("Duración del proceso: "))
            prioridad = int(input("Prioridad del proceso (menor = más urgente): "))
            try:
                proceso = Proceso(pid, duracion, prioridad)
                repo.agregar_proceso(proceso)
            except ValueError as e:
                print(e)
        elif opcion == "2":
            for p in repo.listar_procesos():
                print(f"PID: {p.pid}, Duración: {p.duracion}, Prioridad: {p.prioridad}")
        elif opcion == "3":
            scheduler = FCFSScheduler()
            gantt = scheduler.planificar(repo.listar_procesos())
            print("Diagrama de Gantt (FCFS):")
            for entry in gantt:
                print(f"PID: {entry[0]}, Tiempo inicio: {entry[1]}, Tiempo fin: {entry[2]}")
        elif opcion == "4":
            quantum = int(input("Introduce el quantum de tiempo para Round Robin: "))
            scheduler = RoundRobinScheduler(quantum)
            gantt = scheduler.planificar(repo.listar_procesos())
            print("Diagrama de Gantt (Round Robin):")
            for entry in gantt:
                print(f"PID: {entry[0]}, Tiempo inicio: {entry[1]}, Tiempo fin: {entry[2]}")
        elif opcion == "5":
            sys.exit(0)
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()


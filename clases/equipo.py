# clases/equipo.py

from clases.jugador import Jugador
class Equipo:
    def __init__(self, nombre, entrenador):
        self.nombre = nombre
        self.entrenador = entrenador
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_equipo(self):
        print(f"Equipo: {self.nombre}, Entrenador: {self.entrenador}")
        print("Jugadores:")
        for jugador in self.jugadores:
            print(f"  - {jugador.nombre}")

# clases/partido.py

from clases.equipo import Equipo

class Partido:
    def __init__(self, equipo1, equipo2, fecha):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.fecha = fecha
        self.resultado = "Pendiente"

    def actualizar_resultado(self, marcador):
        self.resultado = marcador

    def mostrar_partido(self):
        print(f"{self.equipo1.nombre} vs {self.equipo2.nombre}")
        print(f"Fecha: {self.fecha}")
        print(f"Resultado: {self.resultado}")

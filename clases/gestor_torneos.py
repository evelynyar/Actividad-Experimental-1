# clases/gestor_torneos.py

from clases.equipo import Equipo
from clases.partido import Partido

class GestorTorneos:
    def __init__(self):
        self.equipos = []
        self.partidos = []

    def registrar_equipo(self, equipo):
        self.equipos.append(equipo)

    def crear_partido(self, equipo1, equipo2, fecha):
        partido = Partido(equipo1, equipo2, fecha)
        self.partidos.append(partido)

    def listar_equipos(self):
        for equipo in self.equipos:
            equipo.mostrar_equipo()

    def mostrar_historial_partidos(self):
        for partido in self.partidos:
            partido.mostrar_partido()

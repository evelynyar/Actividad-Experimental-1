# main.py

from clases.equipo import Equipo
from clases.jugador import Jugador
from clases.partido import Partido
from clases.gestor_torneos import GestorTorneos

# Crear el gestor de torneos
gestor = GestorTorneos()

# Registrar equipos y jugadores
equipo1 = Equipo("Alianza Juvenil", "Hernan Parra")
equipo1.agregar_jugador(Jugador("Luis"))
equipo1.agregar_jugador(Jugador("Juan Carlos"))

equipo2 = Equipo("Titanes", "David Caluqui")
equipo2.agregar_jugador(Jugador("Erick"))
equipo2.agregar_jugador(Jugador("Cristopher"))

gestor.registrar_equipo(equipo1)
gestor.registrar_equipo(equipo2)

# Crear y mostrar un partido
gestor.crear_partido(equipo1, equipo2, "2024-12-15")

print("\nEquipos registrados:")
gestor.listar_equipos()

print("\nHistorial de partidos:")
gestor.mostrar_historial_partidos()

# Actualizar resultado del partido
partido = gestor.partidos[0]
partido.actualizar_resultado("8-2")

print("\nHistorial actualizado de partidos:")
gestor.mostrar_historial_partidos()

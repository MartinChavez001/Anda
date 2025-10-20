import time
import threading

from Configuraciones import Jugador, Carta, Mazo
from Configuraciones import clear, texto_lento

for i in range(2):
    nombreA = input("Ingrese el nombre del jugador A = ")
    nombreB = input("Ingrese el nombre del jugador B = ")
    
Jugador.jugadores[nombreA, nombreB] = (Jugador.jugadores[1], Jugador.jugadores[2])
Jugador.jugadores = list(Jugador.jugadores.items())

print(Jugador.jugadores)



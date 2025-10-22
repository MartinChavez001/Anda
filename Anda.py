import time

from Configuraciones import Jugador, Carta, Mazo
from Configuraciones import clear, texto_lento


j = Jugador()
m = Mazo ()

clear ()

for i in range(1):
    nombreA = input("Ingrese el nombre del jugador A = ")
    nombreB = input("Ingrese el nombre del jugador B = ")
    
    j.jugadorA["Nombre"] = nombreA
    j.jugadorB["Nombre"] = nombreB

m.generacion_mazo()
m.mezclar()
m.repatir(j.jugadores, m.mazo)

print(j.jugadorA, j.jugadorB)
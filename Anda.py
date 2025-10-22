import time

from Configuraciones import Jugador, Carta, Mazo
from Configuraciones import clear, texto_lento


j = Jugador()
m = Mazo ()

clear ()

print("""

    BIEVENIDO A ADNA!

""")

time.sleep(5)

reglas = """
    Bienvenido a Adna, un juego de carta de 4 jugadores. En este juego cada jugador debera jugar sus cartas
    hasta quedarse con 1 y gritar "ADNA!", si logra tirar su ultima carta sera el ganador.
    
    Hay 100 cartas, 72 numericas, 28 especiales. Recuerden jugar bien sus cartas.
"""

texto_lento(reglas, velocidad=0.05)

for i in range(1):
    nombreA = input("Ingrese el nombre del jugador A = ")
    nombreB = input("Ingrese el nombre del jugador B = ")
    
    j.jugadorA["Nombre"] = nombreA
    j.jugadorB["Nombre"] = nombreA

m.generacion_mazo()
m.mezclar()

for jugador in j.jugadores:
    m.repatir()

print(j.jugadorA, j.jugadorB)
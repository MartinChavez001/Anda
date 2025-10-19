import time

from Configuraciones import Jugador, Carta, Mazo
from Configuraciones import clear, texto_lento


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

for _ in range(2):
    nombreA = input("Ingrese el nombre del jugador A =")
    nombreB = input("Ingrese el nombre del jugador B =")
    
    Jugador.jugadores[nombreA, nombreB] = (idx, nombre)
import random
import time
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def texto_lento(texto, velocidad=0.05):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(velocidad)
    print()

class Jugador():
    def __init__(self):
        self.jugadorA = {}
        self.jugadorB = {}
        self.jugadores = [self.jugadorA, self.jugadorB]

    def tirar(jugadores, posicion_turno):
        if posicion_turno == Jugador.jugadorA:
            print(f"Jugador {Jugador.jugadorA["Nombre"]} tire una de sus cartas = ")
            for i in Jugador.jugadorA["MazoJugador"]:
                print(Jugador.jugadorA["MazoJugador"])
            carta_seleccionada = str(input())
            if carta_seleccionada in Jugador.jugadorA["MazoJugador"]:
                Jugador.jugadorA.remove(carta_seleccionada["MazoJugador"])
                Mazo.carta_jugador.append(carta_seleccionada)



class Carta():
    def __init__(self):
        self.total_cartas = 100
        self.numero = [1,2,3,4,5,6,7,8,9]
        self.colores = ["naranja", "violeta", "rosa", "marron"]
        self.tipo = ["Toma Dos", "Reversa", "Salta", "Toma Cuatro"]

class Mazo():
    def __init__(self, carta = None):

        self.cartas_generadas = {}
        self.mazo = {}
        self.carta = carta or Carta()
    
    def generacion_mazo (self):
        idx = 1
        for color in self.carta.colores:
            for numero in self.carta.numero:
                for _ in range(2):
                    self.cartas_generadas[idx] = (color, numero)
                    idx += 1
        
        for color in self.carta.colores:
            for tipo in self.carta.tipo:
                if tipo == self.carta.tipo[3]:
                    self.cartas_generadas[idx] = (color, tipo)
                    idx += 1
                else:
                    for _ in range(2):
                        self.cartas_generadas[idx] = (color, tipo)
                        idx += 1
        
        self.mazo = list(self.cartas_generadas.values())
        
    
    def mezclar(self):
        random.shuffle(self.mazo)

    def repatir(self, jugadores, mazo):
        for jugador in jugadores:
            jugador["MazoJugador"] = []
            for i in range(5):
                carta = random.choice(mazo)
                jugador["MazoJugador"].append(carta)
                mazo.remove(carta)

class Pozo ():
    def __init__(self, jugadorA, jugadorB):
        
        mazo_pozo = {}

        ultima_carta_pozo = list(mazo_pozo.values())[-1]
        
        carta_jugador = None 

class Partida ():
    def __init__(self,jugadores):
        self.ganador = None
        self.jugadores = jugadores
        self.posicion_turno = [Jugador.jugadorA, Jugador.jugadorB]

    def turno (turno):
        while True:
            for jugador in turno:



clear()

for i in range(1):
    nombreA = input("Ingrese el nombre del jugador A = ")
    nombreB = input("Ingrese el nombre del jugador B = ")
    
    Jugador.jugadorA["Nombre"] = nombreA
    Jugador.jugadorB["Nombre"] = nombreB

Mazo.generacion_mazo()
Mazo.mezclar()
Mazo.repatir(Jugador.jugadores, Mazo.mazo)

print(Jugador.jugadorA, Jugador.jugadorB)
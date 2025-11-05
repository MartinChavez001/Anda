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

    def tirar(jugador_actual, mazo_pozo):
        tirar = False
        print(f"Jugador {jugador_actual["Nombre"]} tire una de sus cartas = ")
        for indice, carta in enumerate(jugador_actual["MazoJugador"]):
            print(f"{indice} : {carta}")
        carta_seleccionada = int(input())
        cantidad_cartas = len(jugador_actual["MazoJugador"])
        if carta_seleccionada >= 0 and carta_seleccionada < cantidad_cartas:
            carta_a_jugar = jugador_actual["MazoJugador"][carta_seleccionada]
            jugador_actual["MazoJugador"].pop(carta_seleccionada)
            mazo_pozo.append(carta_a_jugar)
            tirar = True
        return tirar == True

class Carta():
    def __init__(self):
        self.total_cartas = 100
        self.numero = [1,2,3,4,5,6,7,8,9]
        self.colores = ["naranja", "violeta", "rosa", "marron"]
        self.tipo = ["Toma Dos", "Reversa", "Salta", "Toma Cuatro"]

class Mazo():
    def __init__(self, carta = None):

        self.cartas_generadas = {}
        self.mazo = []
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
    def __init__(self):
        self.mazo_pozo = []
        #ultima_carta_pozo = list(mazo_pozo.values())[-1] 

class Partida ():
    def __init__(self):
        self.ganador = None

    def turno (self,jugadores):
        posicion_turno = jugadores
        idx = 0
        jugador_actual = posicion_turno[idx]
        while True:
            tirar = Jugador.tirar(jugador_actual, pozo.mazo_pozo)
            if tirar:
                idx = (idx + 1) % len(posicion_turno)
                jugador_actual = posicion_turno[idx]


clear()

jugador = Jugador()
mazo = Mazo()
partida = Partida()
pozo = Pozo()

for i in range(1):
    nombreA = input("Ingrese el nombre del jugador A = ")
    nombreB = input("Ingrese el nombre del jugador B = ")
    
    jugador.jugadorA["Nombre"] = nombreA
    jugador.jugadorB["Nombre"] = nombreB



mazo.generacion_mazo()
mazo.mezclar()
mazo.repatir(jugador.jugadores, mazo.mazo)

partida.turno(jugador.jugadores)

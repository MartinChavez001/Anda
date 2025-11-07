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
        cantidad_cartas = len(jugador_actual["MazoJugador"])
        agarrar = len(jugador_actual["MazoJugador"])
        for indice, carta in enumerate(jugador_actual["MazoJugador"]):
            print(f"{indice} : {carta}")
        print(f"{agarrar} : Tomar carta.")
        carta_seleccionada = int(input())
        if carta_seleccionada >= 0 and carta_seleccionada < cantidad_cartas:
            carta_a_jugar = jugador_actual["MazoJugador"][carta_seleccionada]
            if pozo.comparacion(carta_a_jugar) == True:
                jugador_actual["MazoJugador"].pop(carta_seleccionada)
                mazo_pozo.append(carta_a_jugar)
                tirar = True
        elif carta_seleccionada == cantidad_cartas:
            print("Tomas una carta y pasas turno.")
            carta_tomada = mazo.mazo.pop()
            jugador_actual["MazoJugador"].append(carta_tomada)
            print(carta_tomada)
            tirar = True
        else:
            print("Carta Invalida.")
        return tirar



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
        self.cantidad_cartas = len(self.mazo)
    
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
                    self.cartas_generadas[idx] = (color, None ,tipo)
                    idx += 1
                else:
                    for _ in range(2):
                        self.cartas_generadas[idx] = (color, None ,tipo)
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
    
    def ultima_carta_mazo(self):
        if self.mazo:
            return self.mazo[-1]
        return None
    def cantidad_cartas(self):
        cartas_en_mazo =  len(mazo.mazo)
        return cartas_en_mazo

class Pozo ():
    def __init__(self):
        self.mazo_pozo = []
    
    def ultima_carta_pozo(self):
        if self.mazo_pozo:
            return self.mazo_pozo[-1]
        return None

    def comparacion(self, carta_a_jugar):
        if not self.mazo_pozo:
            return True
        ultima_carta = self.ultima_carta_pozo()
        

        if ultima_carta[0] == carta_a_jugar[0] or ultima_carta[1] == carta_a_jugar[1]:
            return True
        





class Partida ():
    def __init__(self):
        self.ganador = None

    def turno (self,jugadores, mazo_obj, pozo_obj):
        posicion_turno = jugadores
        idx = 0
        jugador_actual = posicion_turno[idx]
        while True:
            cartas_en_mazo = len(mazo_obj.mazo)
            ultima_pozo = pozo_obj.ultima_carta_pozo()
            print(f"Cartas en el mazo {cartas_en_mazo}")
            print(f"Pozo: {ultima_pozo}")
            tirar = Jugador.tirar(jugador_actual, pozo_obj.mazo_pozo)
            
            if tirar:
                idx = (idx + 1) % len(posicion_turno)
                jugador_actual = posicion_turno[idx]
            else:
                print("Carta erronea")
            
    def prepracion(self, mazo, mazo_pozo):
        print("Se prepara el juego")
        carta_inicial = mazo.pop(-1)
        mazo_pozo.append(carta_inicial)

clear()

jugador = Jugador()
mazo = Mazo()
partida = Partida()
pozo = Pozo()

# Introduccion nombres de jugadores

nombreA = input("Ingrese el nombre del jugador A = ")
nombreB = input("Ingrese el nombre del jugador B = ")

jugador.jugadorA["Nombre"] = nombreA
jugador.jugadorB["Nombre"] = nombreB

#---------------------------------------------------------

mazo.generacion_mazo()
mazo.mezclar()
mazo.repatir(jugador.jugadores, mazo.mazo)
partida.prepracion(mazo.mazo, pozo.mazo_pozo)
partida.turno(jugador.jugadores, mazo, pozo)

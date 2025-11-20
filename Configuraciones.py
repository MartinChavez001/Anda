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
            if carta_a_jugar[1] == 'Salta':
                return "Salta"
            elif carta_a_jugar[1] == 'Reversa':
                return "Reversa"
            elif carta_a_jugar[1] == 'Toma Dos':
                return "Toma Dos"
            elif carta_a_jugar[1] == 'Toma Cuatro':
                return "Toma Cuatro"
            else:
                return "Siguiente"
        else:
            print("Carta erronea (COMPARACION).")
            return False
class Jugador():
    def __init__(self):
        self.jugadorA = {}
        self.jugadorB = {}
        self.jugadores = [self.jugadorA, self.jugadorB]
        self.compracion = None


    def tirar(jugador_actual, mazo_pozo, jugador_siguiente):
        print("jugador actual " + jugador_actual["Nombre"])
        print("jugador siguiente " + jugador_siguiente["Nombre"])
        cartas_en_mazo = mazo.cantidad_cartas() #calcula la cantidad de cartas en el mazo
        ultima_pozo = pozo.ultima_carta_pozo() #obtiene la ultima carta del pozo
        print(f"Cartas en el mazo {cartas_en_mazo}") # muestra la cantidad de cartas en el mazo
        print(f"Pozo: {ultima_pozo}") # muestra la ultima carta del pozo
        print(f"Jugador {jugador_actual["Nombre"]} tire una de sus cartas = ") #PRESENTACION
        cantidad_cartas = len(jugador_actual["MazoJugador"]) # CUENTA LA CANTIDAD DE CARTAS DEL JUGADOR
        agarrar = len(jugador_actual["MazoJugador"]) # AGREGA LA OPCION DE AGARRAR

        for indice, carta in enumerate(jugador_actual["MazoJugador"]): #OPCIONES DEL JUGADOR
            print(f"{indice} : {carta}") # ---
        print(f"{agarrar} : Tomar carta.") # ---
        carta_seleccionada = int(input()) # EL JUGADOR ELIGE UNA CARTA
        if carta_seleccionada >= 0 and carta_seleccionada < cantidad_cartas: # Detecta si la carta esta dentro del mazo del jugador
            carta_a_jugar = jugador_actual["MazoJugador"][carta_seleccionada] # Guarda la carta seleccionada
            comparacion = pozo.comparacion(carta_a_jugar)
            print(f"ESTA ES LA COMPARACION = {comparacion}")
            if comparacion:
                jugador_actual["MazoJugador"].pop(carta_seleccionada)
                mazo_pozo.append(carta_a_jugar)
                return comparacion
        elif carta_seleccionada == cantidad_cartas:
            print("Tomas una carta y pasas turno.")
            carta_tomada = mazo.mazo.pop()
            jugador_actual["MazoJugador"].append(carta_tomada)
            print(carta_tomada)
            return "Agarrar"

class Partida ():
    def __init__(self):
        self.ganador = None
        self.idx = 0
        self. jugador_actual = None
    
    def preparacion(self, mazo, mazo_pozo):
        print("Se prepara el juego")
        carta_inicial = mazo.pop(-1)
        if not isinstance(carta_inicial[1], int):
            print(carta_inicial)
            print("Carta invalida para comenzar el juego, se buscara otra")
            mazo.insert(0,carta_inicial) #se cambio append por insert
            return self.preparacion(mazo, mazo_pozo) # recursividad
        else:
            mazo_pozo.append(carta_inicial)


    def turno (self, idx,jugadores, mazo, pozo):
        posicion_turno = jugadores
        jugador_actual = posicion_turno[idx]
        jugador_siguiente = posicion_turno[(idx + 1) % len(posicion_turno)] # si IDX = 0 : (0 + 1) % 2 = 1, si IDX = 1 : (1 + 1) % 2 = 0
        
        
        tirar = Jugador.tirar(jugador_actual, pozo.mazo_pozo, jugador_siguiente)
        
        if tirar == "Toma Cuatro":
            tomar_cartas = mazo.mazo[-4:]
            del mazo.mazo[-4:]
            jugador_siguiente["MazoJugador"].extend(tomar_cartas)
            self.idx = (idx + 2) % len(posicion_turno)


####################VERIFICAR QUIEN ES JUGADOR SIGUIENTE Y POR QUE EL TOMA 2 NO PONE LAS CARTAS EN
        elif tirar == "Toma Dos":
            tomar_cartas = mazo.mazo[-2:]
            del mazo.mazo[-2:]
            jugador_siguiente["MazoJugador"].extend(tomar_cartas)
            self.idx = (idx + 2) % len(posicion_turno)

        elif tirar == "Salta":
            self.idx = (idx + 2) % len(posicion_turno)
            jugador_actual = posicion_turno[idx]
            self.jugador_actual = jugador_actual
            

        elif tirar == "Reversa":
            idx = (idx - 1) % len(posicion_turno)
            jugador_actual = posicion_turno[idx]
            self.jugador_actual = jugador_actual
            
        elif tirar == "Siguiente":
            self.idx = (idx + 1) % len(posicion_turno)
            jugador_actual = posicion_turno[idx]
            self.jugador_actual = jugador_actual
        
        elif tirar == "Agarrar":
            self.idx = (idx + 1) % len(posicion_turno)
            jugador_actual = posicion_turno[idx]
            self.jugador_actual = jugador_actual
            
        else:
            return Jugador.tirar(jugador_actual, pozo.mazo_pozo, jugador_siguiente) #recursividad

    
    def inicio(self):
        clear()
        nombreA = input("Ingrese el nombre del jugador A = ")
        nombreB = input("Ingrese el nombre del jugador B = ")

        jugador.jugadorA["Nombre"] = nombreA
        jugador.jugadorB["Nombre"] = nombreB

    def ronda(self):
        clear()
        Partida.inicio(self)
        mazo.generacion_mazo()
        mazo.mezclar()
        mazo.repatir(jugador.jugadores, mazo.mazo)
        partida.preparacion(mazo.mazo, pozo.mazo_pozo)
        self.jugador_actual = jugador.jugadores[self.idx]

        ganador = False
        while ganador != True:
            
            self.turno(self.idx,jugador.jugadores, mazo, pozo)
            
            jugador_actual = partida.jugador_actual
            if not jugador_actual["MazoJugador"]:
                print(f"Jugador {jugador_actual} es el ganador.")
                ganador = True


jugador = Jugador()
mazo = Mazo()
partida = Partida()
pozo = Pozo()


partida.ronda()



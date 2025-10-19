import random

class Jugador():
    def __init__(self, Jugador_A = None, Jugador_B = None, Jugador_C = None, Jugador_D = None):
        self.jugadores = ["A","B","C","D"]
        self.mazo_jugador = {}


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
        
        self.mazo = list(self.cartas_generadas.items())
        
    
    def mezclar(self):

        random.shuffle(self.mazo)

        for item in self.mazo:
            print(item)


m = Mazo()
m.generacion_mazo()
m.mezclar()






class Jugador():
    def __init__(self):
        self.nombres = []
        self.mazo_jugador = []

class Carta():
    def __init__(self):
        self.total_cartas = 100
        self.numero = [1,2,3,4,5,6,7,8,9]
        self.colores = ["naranja", "violeta", "rosa", "marron"]
        self.tipo = ["Toma Dos", "Reversa", "Salta", "Toma Cuatro"]
        self.cantidad_numericas = 72
        self.cantidad_tomados = 8
        self.cantidad_reversa = 8
        self.cantidad_salta = 8
        self.cantidad_tomacuatro = 4

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
        
        self.mazo = list(self.cartas_generadas.items())
        print(f"Cartas generadas: {len(self.mazo)}")

        for item in self.mazo[:self.carta.cantidad_numericas]:
            print(item)


m = Mazo()
m.generacion_mazo()






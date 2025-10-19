class Jugador():
    def __init__(self):
        self.nombres = []
        self.mazo_jugador = []


class Mazo():
    def __ini__(self, numero, colores, tipo,total_cartas,cantidad_tomados, cantidad_tomacuatro, cantidad_reserva,cantidad_salta):

        self.cartas_generadas = {}
        self.mazo = {}
    
    def generacion_mazo ():
        


class Carta():
    def __ini__(self):
        self.total_cartas = 100
        self.numero = [1,2,3,4,5,6,7,8,9]
        self.colores = ["naranja", "violeta", "rosa", "marron"]
        self.tipo = ["Toma Dos", "Reversa", "Salta", "Toma Cuatro"]
        self.cantidad_numericas = 72
        self.cantidad_tomados = 8
        self.cantidad_reversa = 8
        self.cantidad_salta = 8
        self.cantidad_tomacuatro = 4


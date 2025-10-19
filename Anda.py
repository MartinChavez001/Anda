class Jugador():
    def __init__(self):
        self.nombres = []
        self.mazo_jugador = []

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

class Mazo():
    def __ini__(self, numero, colores, tipo,total_cartas,cantidad_tomados, cantidad_tomacuatro, cantidad_reserva,cantidad_salta):

        self.cartas_generadas = {}
        self.mazo = {}
    
    def generacion_mazo (total_cartas, cartas_generadas, cantidad_numericas,cantidad_tomados, cantidad_tomacuatro, cantidad_reserva,cantidad_salta, mazo):
        for i in total_cartas:
            for numero, colores in cantidad_numericas:
                if not cartas_generadas:
                    cartas_generadas[len(cartas_generadas)+ 1] = (colores, numero, )
                    print(cartas_generadas)








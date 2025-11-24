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
        self.jugadorA = {"Bot": False, "Adna": False}
        self.jugadorB = {"Bot": True, "Adna": False}
        self.jugadorC = {"Bot": False, "Adna": False}
        self.jugadorD = {"Bot": True, "Adna": False}
        self.jugadores = [self.jugadorA, self.jugadorB, self.jugadorC, self.jugadorD]
        self.compracion = None

    def tirar(self, jugador_actual, mazo_pozo, jugador_siguiente, cartas_a_agarrar):
        cartas_en_mazo = mazo.cantidad_cartas()
        
        if cartas_en_mazo <= 0:
            print("Ya no hay cartas en el mazo. Reciclando...")
            mazo.mazo.extend(pozo.mazo_pozo)
            pozo.mazo_pozo.clear()
            partida.preparacion(mazo.mazo, pozo.mazo_pozo)
        
        ultima_pozo = pozo.ultima_carta_pozo()
        print("jugador actual " + jugador_actual["Nombre"])
        print("jugador siguiente " + jugador_siguiente["Nombre"])
        print(f"Cartas en el mazo {cartas_en_mazo}")
        print(f"Pozo: {ultima_pozo}")
        print(f"Jugador {jugador_actual['Nombre']} tire una de sus cartas = ")

        cantidad_cartas = len(jugador_actual["MazoJugador"])
        agarrar = cantidad_cartas + 1
        adna_opcion = cantidad_cartas + 2

        for indice, carta in enumerate(jugador_actual["MazoJugador"]):
            print(f"{indice + 1} : {carta}")
        
        if cartas_a_agarrar > 0:
            print(f"{agarrar} : Tomar {cartas_a_agarrar} cartas.")
        else:
            print(f"{agarrar} : Tomar carta.")
        
        print(f"{adna_opcion} : Decir 'Adná'")

        if jugador_actual["Bot"]:
            print(f"{jugador_actual['Nombre']} está pensando...")
            time.sleep(2)
            if jugador_actual == self.jugadorB:
                carta_seleccionada = self.est_bot_B(jugador_actual, ultima_pozo, cartas_a_agarrar)
            elif jugador_actual == self.jugadorD:
                carta_seleccionada = self.est_bot_D(jugador_actual, ultima_pozo, cartas_a_agarrar)
        else:
            carta_seleccionada = int(input()) - 1

        # Decir Adna
        if carta_seleccionada == adna_opcion - 1:
            if cantidad_cartas == 2:
                print(f"{jugador_actual['Nombre']} dice 'Adná'!")
                jugador_actual["Adna"] = True
                print("Ahora tirá tu carta:")
                return self.tirar(jugador_actual, mazo_pozo, jugador_siguiente, cartas_a_agarrar)
            else:
                print(f"No podés decir 'Adná' con {cantidad_cartas} cartas. Solo cuando tenés 2.")
                return self.tirar(jugador_actual, mazo_pozo, jugador_siguiente, cartas_a_agarrar)
        
        # Tomar cartas
        if carta_seleccionada == cantidad_cartas:
            if cartas_a_agarrar > 0:
                print(f"Tomas {cartas_a_agarrar} cartas y pasas turno.")
                tomar_cartas = mazo.mazo[-cartas_a_agarrar:]
                del mazo.mazo[-cartas_a_agarrar:]
                jugador_actual["MazoJugador"].extend(tomar_cartas)
                jugador_actual["Adna"] = False
                return "Tomo Acumuladas"
            else:
                print("Tomas una carta y pasas turno.")
                carta_tomada = mazo.mazo.pop()
                jugador_actual["MazoJugador"].append(carta_tomada)
                print(carta_tomada)
                jugador_actual["Adna"] = False
                return "Agarrar"

        # Jugar una carta
        elif carta_seleccionada >= 0 and carta_seleccionada < cantidad_cartas:
            carta_a_jugar = jugador_actual["MazoJugador"][carta_seleccionada]
            comparacion = pozo.comparacion(carta_a_jugar)
            print(f"ESTA ES LA COMPARACION = {comparacion}")
            
            if cartas_a_agarrar > 0:
                if comparacion in ['Toma Dos', 'Toma Cuatro']:
                    jugador_actual["MazoJugador"].pop(carta_seleccionada)
                    mazo_pozo.append(carta_a_jugar)
                    jugador_actual["Adna"] = False
                    return comparacion
                else:
                    print("Solo podés contestar con +2 o +4, o tomar las cartas.")
                    return self.tirar(jugador_actual, mazo_pozo, jugador_siguiente, cartas_a_agarrar)
            else:
                if comparacion:
                    # Verifica si se debe decir adna o no
                    if cantidad_cartas == 2 and not jugador_actual.get("Adna", False):
                        print(f"¡Olvidaste decir 'Adná'! Tomás 2 cartas de penalidad.")
                        penalizacion = mazo.mazo[-2:]
                        del mazo.mazo[-2:]
                        jugador_actual["MazoJugador"].extend(penalizacion)
                        jugador_actual["Adna"] = False
                        return "Siguiente"
                    
                    jugador_actual["MazoJugador"].pop(carta_seleccionada)
                    mazo_pozo.append(carta_a_jugar)
                    
                    if len(jugador_actual["MazoJugador"]) == 1:
                        jugador_actual["Adna"] = False
                    
                    return comparacion
                else:
                    return self.tirar(jugador_actual, mazo_pozo, jugador_siguiente, cartas_a_agarrar)
        
        else:
            print("Opción inválida.")
            return self.tirar(jugador_actual, mazo_pozo, jugador_siguiente, cartas_a_agarrar)

    def est_bot_B(self, jugador_actual, ultima_pozo, cartas_a_agarrar):
        """El colorista"""
        cantidad_cartas = len(jugador_actual["MazoJugador"])
        
        if cantidad_cartas == 2:
            jugador_actual["Adna"] = True
            print(f"{jugador_actual['Nombre']} (Bot) dice 'Adná'!")
        
        colores = {}
        for carta in jugador_actual["MazoJugador"]:
            color = carta[0]
            colores[color] = colores.get(color, 0) + 1
        
        color_favorito = max(colores, key=colores.get)

        cartas_validas = []
        for indice, carta in enumerate(jugador_actual["MazoJugador"]):
            if pozo.comparacion(carta):
                cartas_validas.append((indice, carta))
        
        if not cartas_validas:
            return cantidad_cartas
        
        if cartas_a_agarrar > 0:
            for indice, carta in cartas_validas:
                if carta[1] in ['Toma Dos', 'Toma Cuatro']:
                    return indice
            return cantidad_cartas
        
        for indice, carta in cartas_validas:
            if carta[0] == color_favorito:
                return indice
        
        return cartas_validas[0][0]
    
    def est_bot_D(self, jugador_actual, ultima_pozo, cartas_a_agarrar):
        """El estratega"""
        cantidad_cartas = len(jugador_actual["MazoJugador"])
        
        if cantidad_cartas == 2:
            jugador_actual["Adna"] = True
            print(f"{jugador_actual['Nombre']} (Bot) dice 'Adná'!")
        
        min_cartas = min(len(j["MazoJugador"]) for j in self.jugadores if j != jugador_actual)

        cartas_validas = []
        for indice, carta in enumerate(jugador_actual["MazoJugador"]):
            if pozo.comparacion(carta):
                cartas_validas.append((indice, carta))
        
        if not cartas_validas:
            return cantidad_cartas
        
        if cartas_a_agarrar > 0:
            for indice, carta in cartas_validas:
                if carta[1] in ['Toma Dos', 'Toma Cuatro']:
                    return indice
            return cantidad_cartas
        
        if min_cartas <= 2:
            for indice, carta in cartas_validas:
                if carta[1] in ['Toma Cuatro', 'Toma Dos', 'Salta']:
                    return indice
        
        for indice, carta in cartas_validas:
            if carta[1] in ['Reversa', 'Salta']:
                return indice
        
        cartas_numericas = [(i, c) for i, c in cartas_validas if isinstance(c[1], int)]
        if cartas_numericas:
            carta_elegida = max(cartas_numericas, key=lambda x: x[1][1])
            return carta_elegida[0]
        
        return cartas_validas[0][0]

class Partida ():
    def __init__(self):
        self.ganador = None
        self.idx = 0
        self.jugador_actual = None
        self.cartas_a_agarrar = 0
        self.carta_pasada = 0
        self.sentido = 1
    
    def preparacion(self, mazo, mazo_pozo):
        
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
        
        tirar_resultado = jugador.tirar(jugador_actual, pozo.mazo_pozo, jugador_siguiente, self.cartas_a_agarrar)
        
        if tirar_resultado == "Toma Cuatro":
            carta_pasada = 4
            self.cartas_a_agarrar += 4
            self.idx = (idx + self.sentido) % len(posicion_turno)
            jugador_actual = posicion_turno[self.idx]
            self.jugador_actual = jugador_actual
            
        elif tirar_resultado == "Toma Dos":
            self.cartas_a_agarrar += 2
            carta_pasada = 2
            self.idx = (idx + self.sentido) % len(posicion_turno)
            jugador_actual = posicion_turno[self.idx]
            self.jugador_actual = jugador_actual

        elif tirar_resultado == "Salta":
            self.idx = (idx + 2 * self.sentido) % len(posicion_turno)
            jugador_actual = posicion_turno[self.idx]
            self.jugador_actual = jugador_actual
            

        elif tirar_resultado == "Reversa":
            self.sentido *= -1
            self.idx = (idx + self.sentido) % len(posicion_turno)
            jugador_actual = posicion_turno[self.idx]
            self.jugador_actual = jugador_actual
            
        elif tirar_resultado == "Siguiente":
            self.idx = (idx + self.sentido) % len(posicion_turno)
            jugador_actual = posicion_turno[self.idx]
            self.jugador_actual = jugador_actual
        
        elif tirar_resultado == "Agarrar":
            self.idx = (idx + self.sentido) % len(posicion_turno)
            jugador_actual = posicion_turno[self.idx]
            self.jugador_actual = jugador_actual
            
        elif tirar_resultado == "Tomo Acumuladas":
            self.cartas_a_agarrar = 0
            self.idx = (idx + self.sentido) % len(posicion_turno)
            jugador_actual = posicion_turno[self.idx]
            self.jugador_actual = jugador_actual
        else:
            return jugador.tirar(jugador_actual, pozo.mazo_pozo, jugador_siguiente, self.cartas_a_agarrar) #recursividad

    
    def inicio(self):
        clear()
        nombreA = input("Ingrese el nombre del jugador A = ")
        nombreC = input("Ingrese el nombre del jugador C = ")

        jugador.jugadorA["Nombre"] = nombreA #Pablo, Juan, Martin, Mathew
        jugador.jugadorB["Nombre"] = "Juan"
        jugador.jugadorC["Nombre"] = nombreC
        jugador.jugadorD["Nombre"] = "Mathew"

    def ronda(self):
        clear()
        Partida.inicio(self)
        mazo.generacion_mazo()
        mazo.mezclar()
        mazo.repatir(jugador.jugadores, mazo.mazo)
        partida.preparacion(mazo.mazo, pozo.mazo_pozo)
        print("Se prepara el juego")
        self.jugador_actual = jugador.jugadores[self.idx]

        ganador = False
        while ganador != True:
            
            self.turno(self.idx,jugador.jugadores, mazo, pozo)
            
            jugador_actual = partida.jugador_actual
            if not jugador_actual["MazoJugador"]:
                print(f"Jugador {jugador_actual['Nombre']} es el ganador.")
                ganador = True


jugador = Jugador()
mazo = Mazo()
partida = Partida()
pozo = Pozo()


partida.ronda()



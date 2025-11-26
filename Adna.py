import random
import time
import os


# Funcion para limpiar la consola
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# Funcion para que los prints sean mas lentos

def texto_lento(texto, velocidad=0.05, end ='\n'):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(velocidad)
    print(end=end)

# Clase jugador
class Carta():
    def __init__(self): 
        self.numero = [1,2,3,4,5,6,7,8,9]
        self.colores = ["naranja", "violeta", "rosa", "marron"]
        self.tipo = ["Toma Dos", "Reversa", "Salta", "Toma Cuatro"]

class Mazo():
    def __init__(self):
        self.cartas_generadas = {} # Guarda las cartas generadas con indice : color, tipo o numero
        self.mazo = [] # Guarda las cartas generadas en el mazo para ser usado en la partida
        self.carta = Carta()

    def generacion_mazo (self): # Genera las 100 cartas para el juego
        idx = 1 # Indice de cada carta

        # Genera todas las cartas numericas, 2 copias por cada una (72 cartas en total)

        for color in self.carta.colores: # recorre cada color
            for numero in self.carta.numero: # recorre cada numero
                for _ in range(2): # crea 2 copias 
                    self.cartas_generadas[idx] = (color, numero) #genera cartas haciendo : Indice, color, numero
                    idx += 1 # incrementa el indice
        
        # Genera las cartas de tipo accion (28 cartas)

        for color in self.carta.colores:
            for tipo in self.carta.tipo:
                if tipo == self.carta.tipo[3]: # Crea solo 4 cartas 'Toma Cuatro' una por cada color
                    self.cartas_generadas[idx] = (color, tipo)
                    idx += 1
                else:
                    for _ in range(2): # Genera 2 cartas de tipo accion por color 
                        self.cartas_generadas[idx] = (color, tipo)
                        idx += 1
        
        self.mazo = list(self.cartas_generadas.values()) # Guarda las cartas como tuplas
        
    def mezclar(self):
        random.shuffle(self.mazo) #Mezcla las cartas de forma aleatoria 

    def repartir(self, jugadores, mazo):
        for jugador in jugadores: # Por jugador, reparte 5 cartas del mazo
            jugador["MazoJugador"] = []
            for _ in range(5):
                carta = mazo.pop()
                jugador["MazoJugador"].append(carta)
    
    def ultima_carta_mazo(self): #Devuelve la ultima carta del mazo
        if self.mazo:
            return self.mazo[-1]
        return None
    def cantidad_cartas(self): #Devuelve la cantidad de cartas que quedan en el mazo
        cartas_en_mazo =  len(mazo.mazo)
        return cartas_en_mazo

class Pozo ():
    def __init__(self):
        self.mazo_pozo = [] #Lista para el mazo del pozo
    
    def ultima_carta_pozo(self): #Devuelve la ultima carta del pozo (usada para comparaciones)
        if self.mazo_pozo:
            return self.mazo_pozo[-1]
        return None

    def comparacion(self, carta_a_jugar): #Funcion que compara la ultima carta del pozo con la carta del jugador
        if not self.mazo_pozo: #Verifica que el pozo este vacio antes de jugar la primera carta
            return True
        
        ultima_carta = self.ultima_carta_pozo() # Establece la ultima carta tirada en el pozo
        
        if ultima_carta[0] == carta_a_jugar[0] or ultima_carta[1] == carta_a_jugar[1]: #Compara los indices de cada carta y verifica si alguno de los 2 coincide
            if carta_a_jugar[1] == 'Salta': # Si indice 1 (tipo) es igual a 'Salta' la funcion comparacion devuelve el tipo 'Salta' y asi con cada una
                return "Salta"
            elif carta_a_jugar[1] == 'Reversa':
                return "Reversa"
            elif carta_a_jugar[1] == 'Toma Dos':
                return "Toma Dos"
            elif carta_a_jugar[1] == 'Toma Cuatro':
                return "Toma Cuatro"
            else: # Este else verifica si la carta tirada coincide en color o numero y devuelve 'Siguiente'
                return "Siguiente" 
        else:
            print("Carta erronea.") # Si ninguna condicion se dio, devuelve error 
            return False

class Jugador():    
    def __init__(self):
        self.jugadorA = {"Bot": False, "Adna": False} # Establece a cada jugador, definiendo si es un bot o no
        self.jugadorB = {"Bot": True, "Adna": False} # Asi como tambien si dijo Adna o no
        self.jugadorC = {"Bot": False, "Adna": False}
        self.jugadorD = {"Bot": True, "Adna": False}
        self.jugadores = [self.jugadorA, self.jugadorB, self.jugadorC, self.jugadorD] # Almacena a todos los jugadores

    def tirar(self, jugador_actual, mazo_pozo, jugador_siguiente, cartas_a_agarrar):
        # Funcion que se encarga de que el jugador tire una carta
        clear()
        cartas_en_mazo = mazo.cantidad_cartas()
        
        if cartas_en_mazo <= 0:
            clear()
            texto_lento(f"Ya no hay cartas en el mazo. Reciclando...", velocidad = 0.05)
            mazo.mazo.extend(pozo.mazo_pozo)
            pozo.mazo_pozo.clear()
            mazo.mezclar()
            partida.preparacion(mazo.mazo, pozo.mazo_pozo)
        
        ultima_pozo = pozo.ultima_carta_pozo()
        print("="*40)
        print(f"\nTurno de {jugador_actual["Nombre"]}")
        print("="*40)
        print(f"\nCartas en el mazo {cartas_en_mazo}")
        print(f"\nPozo: {ultima_pozo}")
        print(f"\nJugador {jugador_actual['Nombre']} tire una de sus cartas = ")
        print("\n")

        cantidad_cartas = len(jugador_actual["MazoJugador"])
        agarrar = cantidad_cartas + 1
        adna_opcion = cantidad_cartas + 2

        for indice, carta in enumerate(jugador_actual["MazoJugador"]):
            print(f"{indice + 1} : {carta}")
        
        if cartas_a_agarrar > 0:
            print(f"\n {agarrar} : Tomar {cartas_a_agarrar} cartas.")
        else:
            print(f"\n {agarrar} : Tomar carta.")
        
        print(f"\n {adna_opcion} : Decir 'Adná'")

        if jugador_actual["Bot"]:
            texto_lento(f"\n{jugador_actual['Nombre']} está pensando...", velocidad=0.05)

            time.sleep(3)
            if jugador_actual == self.jugadorB:
                carta_seleccionada = self.est_bot_B(jugador_actual, ultima_pozo, cartas_a_agarrar)
            elif jugador_actual == self.jugadorD:
                carta_seleccionada = self.est_bot_D(jugador_actual, ultima_pozo, cartas_a_agarrar)
        else:
            texto_lento("\nElegí una opción: ", velocidad=0.05, end="")
            carta_seleccionada = int(input()) - 1

        # Decir Adna
        if carta_seleccionada == adna_opcion - 1:
            if cantidad_cartas == 2:
                texto_lento(f"{jugador_actual['Nombre']} dice 'Adna'!", velocidad = 0.05)
                jugador_actual["Adna"] = True
                texto_lento("Ahora tira tu carta:", velocidad = 0.05)
                time.sleep(2)
                return self.tirar(jugador_actual, mazo_pozo, jugador_siguiente, cartas_a_agarrar)
            else:
                clear()
                texto_lento(f"No podes decir 'Adna' con {cantidad_cartas} cartas. Solo cuando tenes 2.", velocidad=0.05)
                time.sleep(3)
                return self.tirar(jugador_actual, mazo_pozo, jugador_siguiente, cartas_a_agarrar)
        
        # Tomar cartas
        if carta_seleccionada == cantidad_cartas:
            if cartas_a_agarrar > 0:  # Verifica si el jugador tiene que agarrar cartas previas
                clear()
                texto_lento(f"Tomas {cartas_a_agarrar} cartas y pasas turno.", velocidad=0.05)
                tomar_cartas = mazo.mazo[-cartas_a_agarrar:] #mazo.mazo[-1]
                del mazo.mazo[-cartas_a_agarrar:]
                jugador_actual["MazoJugador"].extend(tomar_cartas)
                jugador_actual["Adna"] = False
                return "Tomo Acumuladas"
            else:
                clear()
                texto_lento(f"{jugador_actual['Nombre']} tomas una carta y pasas turno.", velocidad=0.05)
                carta_tomada = mazo.mazo.pop()
                jugador_actual["MazoJugador"].append(carta_tomada)
                print(carta_tomada)
                jugador_actual["Adna"] = False
                return "Agarrar"

        # Jugar una carta
        elif carta_seleccionada >= 0 and carta_seleccionada < cantidad_cartas:
            carta_a_jugar = jugador_actual["MazoJugador"][carta_seleccionada]
            comparacion = pozo.comparacion(carta_a_jugar)
            
            if cartas_a_agarrar > 0: #Verifica si el jugador tiene que tirar un +2 o +4 para responder
                if comparacion in ['Toma Dos', 'Toma Cuatro']:
                    jugador_actual["MazoJugador"].pop(carta_seleccionada)
                    mazo_pozo.append(carta_a_jugar)
                    jugador_actual["Adna"] = False
                    return comparacion
                else:
                    texto_lento(f"Solo podés contestar con +2 o +4, o tomar las cartas.", velocidad=0.05)
                    return self.tirar(jugador_actual, mazo_pozo, jugador_siguiente, cartas_a_agarrar)
            else:
                if comparacion:
                    # Verifica si se debe decir adna o no
                    if cantidad_cartas == 2 and not jugador_actual.get("Adna", False):
                        clear()
                        texto_lento(f"¡Olvidaste decir 'Adná'! Tomás 2 cartas de penalidad.", velocidad=0.05)
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
            texto_lento(f"{jugador_actual['Nombre']} (Bot) dice 'Adná'!", velocidad = 0.05)
            time.sleep(1)
        
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
            texto_lento(f"{jugador_actual['Nombre']} (Bot) dice 'Adná'!", velocidad =0.05)
            time.sleep(1)
        
        min_cartas = min(len(j["MazoJugador"]) for j in self.jugadores if j != jugador_actual)

        cartas_validas = []
        for indice, carta in enumerate(jugador_actual["MazoJugador"]):
            if pozo.comparacion(carta):
                cartas_validas.append((indice, carta))
        
        if not cartas_validas:
            return cantidad_cartas #agarrar
        
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
        
        return cartas_validas[0][0]

class Partida ():
    def __init__(self):
        self.ganador = None
        self.idx = 0
        self.jugador_actual = None
        self.cartas_a_agarrar = 0
        self.sentido = 1
    
    def preparacion(self, mazo, mazo_pozo):
        
        carta_inicial = mazo.pop(-1)
        if not isinstance(carta_inicial[1], int):
            print(carta_inicial)

            texto_lento(f"Carta invalida para comenzar el juego, se buscara otra", velocidad=0.05)

            mazo.insert(0,carta_inicial) #se cambio append por insert
            return self.preparacion(mazo, mazo_pozo) # recursividad
        else:
            mazo_pozo.append(carta_inicial)


    def turno (self, idx,jugadores, mazo, pozo):
        posicion_turno = jugadores
        jugador_actual = posicion_turno[idx]
        jugador_siguiente = posicion_turno[(idx + 1) % len(posicion_turno)] # si IDX = 0 : (0 + 1) % 4 = 1, si IDX = 1 : (1 + 1) % 4 = 2, si IDX = 2 : (2+1) % 4 = 3, si IDX = 3 : (3+1) % 4 = 0
        
        tirar_resultado = jugador.tirar(jugador_actual, pozo.mazo_pozo, jugador_siguiente, self.cartas_a_agarrar)
        
        if not jugador_actual["MazoJugador"]:
            clear()
            texto_lento(f"¡Jugador {jugador_actual['Nombre']} es el ganador!", velocidad=0.05)
            self.ganador = jugador_actual
            return True
        
        if tirar_resultado == "Toma Cuatro":
            self.cartas_a_agarrar += 4
            self.idx = (idx + self.sentido) % len(posicion_turno)
            jugador_actual = posicion_turno[self.idx]
            self.jugador_actual = jugador_actual
            
        elif tirar_resultado == "Toma Dos":
            self.cartas_a_agarrar += 2
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
        print("""

                BIENVENIDO A ADNA!

        """)

        reglas = """
        Bienvenido a Adna, un juego de carta de 4 jugadores. En este juego cada jugador debera jugar sus cartas
        hasta quedarse con 1 y gritar "ADNA!", si logra tirar su ultima carta sera el ganador.
        Hay 100 cartas, 72 numericas, 28 especiales. Recuerden jugar bien sus cartas.
        """
        texto_lento(reglas, velocidad=0.05)

        texto_lento(f"Por favor, ingrese el nombre de los jugadores. ", velocidad=0.05)

        texto_lento(f"Ingrese el nombre del jugador A = ", velocidad=0.05, end ="")
        nombreA = input()
        
        texto_lento(f"Ingrese el nombre del jugador C = ", velocidad=0.05, end="")
        nombreC = input()


        jugador.jugadorA["Nombre"] = nombreA
        jugador.jugadorB["Nombre"] = "Juan"
        jugador.jugadorC["Nombre"] = nombreC
        jugador.jugadorD["Nombre"] = "Mathew"

    def ronda(self):
        clear()
        Partida.inicio(self)
        mazo.generacion_mazo()
        mazo.mezclar()
        mazo.repartir(jugador.jugadores, mazo.mazo)
        partida.preparacion(mazo.mazo, pozo.mazo_pozo)
        self.jugador_actual = jugador.jugadores[self.idx]

        texto_lento(f"Se prepara el juego", velocidad=0.05)

        while not self.ganador:
            hay_ganador = self.turno(self.idx, jugador.jugadores, mazo, pozo)
            if hay_ganador:
                break

jugador = Jugador()
mazo = Mazo()
partida = Partida()
pozo = Pozo()

partida.ronda()
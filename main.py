import random

class Partida:

    partida = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

    def sumar_puntuaciones(self):
        resultado = sum(list(map(sum, list(self.partida)))) 
        return resultado

    def lanzar_bolas(self):
        tirada = []
        tirada.append(random.randint(0,10))
        tirada.append(random.randint(0,(10 - tirada[0])))
        return tirada

    def asignar_puntuacion(self, posicion, puntos):
        self.partida[posicion] = puntos
        return self.partida



import random

class Partida:

    tabla_puntos = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

    def sumar_puntuaciones(self):
        resultado = sum(list(map(sum, list(self.tabla_puntos)))) 
        return resultado

    def lanzar_bolas(self):
        tirada = []
        tirada.append(random.randint(0,10))
        tirada.append(random.randint(0,(10 - tirada[0])))
        return tirada

    def asignar_puntuacion(self, posicion, puntos):
        self.tabla_puntos[posicion] = puntos
        return self.tabla_puntos



import random

class Partida():

    partida = ([0,0])*10

    def sumar_puntuaciones(partida):
        resultado = sum(list(map(sum, list(partida)))) 
        return resultado

    def lanzar_bolas():
        tirada = []
        tirada.append(random.randint(0,10))
        tirada.append(random.randint(0,(10 - tirada[0])))
        return tirada
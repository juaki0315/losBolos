
class Partida():

    partida = ([0,0])*10

    def sumar_puntuaciones(partida):
        resultado = sum(list(map(sum, list(partida)))) 
        return resultado
        


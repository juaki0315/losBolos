import random


class Partida:

    def __init__(self):
        self.tabla_puntos = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

    def sumar_puntuaciones(self):
        # resultado = sum(list(map(sum, list(self.tabla_puntos)))) 
        resultado = 0
        ha_habido_strike = False
        ha_habido_spare = False
        for elemento in self.tabla_puntos:
            posicion = 0
            if self.check_strike(elemento):
                resultado += 10
                ha_habido_strike = True
                posicion += 1 
            
            elif self.check_spare(elemento):
                resultado += 10 
                ha_habido_spare = True
                posicion += 1
            
            else: 
                if ha_habido_strike:
                    resultado += 2*(sum(elemento))
                    ha_habido_strike = False

                elif ha_habido_spare:
                    resultado = resultado + sum(elemento) + elemento[0]
                    ha_habido_spare = False

                else:
                    resultado += sum(elemento)

                posicion += 1

        return resultado

    def lanzar_bolas(self):
        tirada = []
        tirada.append(random.randint(0,10))
        tirada.append(random.randint(0,(10 - tirada[0])))
        return tirada

    def asignar_puntuacion(self, posicion, puntos):
        self.tabla_puntos[posicion] = puntos
        return self.tabla_puntos

    def check_strike(self, turno):
        if turno[0] == 10:
            return True
        else:
            return False

    def check_spare(self, turno):
        if (sum(turno) == 10) & (turno[0] != 10):
            return True
        else:
            return False


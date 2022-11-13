import unittest
from main import Partida

class TestBolos(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual('foo'.upper(), 'FOO')


    def test_existe_partida(self):
        esperado = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        prueba = Partida()
        resultado = prueba.tabla_puntos
        self.assertEqual(esperado, resultado)
    
    def test_sumar_puntuacion(self):
        prueba = Partida()
        prueba.tabla_puntos = [[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0]]
        esperado = 10
        resultado = prueba.sumar_puntuaciones()
        self.assertEqual(esperado, resultado)

    def test_sumar_puntuacion2(self):
        prueba = Partida()
        prueba.tabla_puntos = [[1,1],[1,0],[1,0],[1,0],[1,5],[1,0],[1,0],[1,0],[1,0],[1,0]]
        esperado = 16  
        resultado = prueba.sumar_puntuaciones()
        self.assertEqual(esperado, resultado)

    def test_lanzar_bolas(self):
        prueba = Partida()
        tirada = prueba.lanzar_bolas()
        self.assertLessEqual(sum(tirada), 10)

    def test_lanzar_bolas2(self):
        prueba = Partida()
        tirada = prueba.lanzar_bolas()
        self.assertGreaterEqual(sum(tirada), 0)

    def test_asignar_puntuacion(self):
        prueba = Partida()
        tirada = prueba.lanzar_bolas()
        escenario = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        escenario[0] = tirada
        self.assertEqual(escenario, prueba.asignar_puntuacion(0, tirada))

    def test_asignar_puntuacion2(self):
        prueba = Partida()
        tirada = prueba.lanzar_bolas()
        escenario = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        escenario[2] = tirada
        self.assertEqual(escenario, prueba.asignar_puntuacion(2, tirada))    


    def test_check_strike(self):
        prueba = Partida()
        escenario = [[10,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        prueba.tabla_puntos = escenario
        turno = prueba.tabla_puntos[0]
        self.assertTrue(prueba.check_strike(turno))

    

if __name__ == '__main__':
    unittest.main()

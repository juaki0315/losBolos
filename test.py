import unittest
from main import Partida

class TestBolos(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_existe_partida(self):
        esperado = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        resultado = Partida.partida
        Partida.partida[0] = [0,0]
        self.assertEqual(esperado, resultado)
    
    def test_sumar_puntuacion(self):
        partida = [[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0]]
        esperado = 10
        resultado = Partida.sumar_puntuaciones(partida)
        self.assertEqual(esperado, resultado)

    def test_sumar_puntuacion2(self):
        partida = [[1,1],[1,0],[1,0],[1,0],[1,5],[1,0],[1,0],[1,0],[1,0],[1,0]]
        esperado = 16
        resultado = Partida.sumar_puntuaciones(partida)
        self.assertEqual(esperado, resultado)

    def test_lanzar_bolas(self):
        tirada = Partida.lanzar_bolas()
        self.assertLessEqual(sum(tirada), 10)

    def test_lanzar_bolas2(self):
        tirada = Partida.lanzar_bolas()
        self.assertGreaterEqual(sum(tirada), 0)

    def test_asignar_puntuacion(self):
        tirada = Partida.lanzar_bolas()
        partida = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        partida[0] = tirada
        self.assertEqual(partida, Partida.asignar_puntuacion(0, tirada))


if __name__ == '__main__':
    unittest.main()

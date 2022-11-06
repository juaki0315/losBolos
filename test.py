import unittest
from main import Partida

class TestBolos(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_existe_partida(self):
        esperado = ([0,0])*10
        resultado = Partida.partida
        self.assertEqual(esperado, resultado)
    
    def test_sumar_puntuacion(self):
        partida = ([1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0])
        esperado = 10
        resultado = Partida.sumar_puntuaciones(partida)
        self.assertEqual(esperado, resultado)


if __name__ == '__main__':
    unittest.main()
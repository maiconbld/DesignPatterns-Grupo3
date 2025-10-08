import unittest
from src.strategy_agent import AgenteConversacional, UsuarioPerfil, EnsinoInfantil

class TestStrategy(unittest.TestCase):
    def test_demo_behavior(self):
        agente = AgenteConversacional(UsuarioPerfil(idade=8))
        resp = agente.ensinar('adição', {'a':2,'b':2})
        self.assertIn('4', resp)

    def test_change_strategy(self):
        agente = AgenteConversacional(UsuarioPerfil(idade=13))
        resp1 = agente.ensinar('multiplicação', {'a':3,'b':3})
        agente.set_strategy(EnsinoInfantil())
        resp2 = agente.ensinar('multiplicação', {'a':3,'b':3})
        self.assertNotEqual(resp1, resp2)

if __name__ == '__main__':
    unittest.main()

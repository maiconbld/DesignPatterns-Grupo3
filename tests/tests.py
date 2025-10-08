import unittest
from agente_conversacional import (
    IMetodoEnsino,
    EnsinoTeorico,
    EnsinoPratico,
    EnsinoResumido,
    UsuarioPerfil,
    AgenteConversacional
)

class TestStrategyPattern(unittest.TestCase):

    def test_ensino_teorico(self):
        strategy = EnsinoTeorico()
        resultado = strategy.ensinar("Programação Orientada a Objetos", {})
        self.assertIn("Explicação teórica", resultado)

    def test_ensino_pratico(self):
        strategy = EnsinoPratico()
        resultado = strategy.ensinar("Estruturas de Dados", {})
        self.assertIn("Exercício prático", resultado)

    def test_ensino_resumido(self):
        strategy = EnsinoResumido()
        resultado = strategy.ensinar("Banco de Dados", {})
        self.assertIn("Resumo rápido", resultado)

    def test_agente_inicia_com_estrategia_certa(self):
        agente_iniciante = AgenteConversacional(UsuarioPerfil("iniciante"))
        self.assertIsInstance(agente_iniciante._strategy, EnsinoTeorico)

        agente_intermediario = AgenteConversacional(UsuarioPerfil("intermediario"))
        self.assertIsInstance(agente_intermediario._strategy, EnsinoResumido)

        agente_avancado = AgenteConversacional(UsuarioPerfil("avancado"))
        self.assertIsInstance(agente_avancado._strategy, EnsinoPratico)

    def test_troca_de_estrategia(self):
        perfil = UsuarioPerfil("iniciante")
        agente = AgenteConversacional(perfil)
        agente.set_strategy(EnsinoPratico())

        resultado = agente.ensinar("Python", {"nivel": "avancado"})
        self.assertIn("Exercício prático", resultado)

    def test_interface_abstrata(self):
        with self.assertRaises(TypeError):
            IMetodoEnsino()  # Não pode ser instanciada diretamente

if __name__ == '__main__':
    unittest.main()

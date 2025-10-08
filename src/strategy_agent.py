# Implementação do Strategy Pattern para o Agente Conversacional (em Python).
# Arquivo principal com demo e execução de testes.
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
import unittest

# ---------------------------
# Interface / Abstração
# ---------------------------

class IMetodoEnsino(ABC):
    """
    Interface que representa um método de ensino.
    Cada estratégia concreta implementa como explicar um conceito/questão.
    """
    @abstractmethod
    def ensinar(self, topico: str, contexto: dict) -> str:
        pass

# ---------------------------
# Estratégias concretas
# ---------------------------

class EnsinoInfantil(IMetodoEnsino):
    def ensinar(self, topico: str, contexto: dict) -> str:
        if topico.lower() in ("adição", "soma", "somar"):
            a = contexto.get("a")
            b = contexto.get("b")
            if a is not None and b is not None:
                return f"Vamos somar com objetos: se você tem {a} maçãs e ganha {b} maçã(s), agora tem {a + b} maçãs. 😊"
            return "Soma é juntar coisas. Se você junta 2 brinquedos com 3 brinquedos, tem 5 brinquedos."
        return f"Explicação simples sobre '{topico}': vamos usar desenhos e exemplos do dia a dia."

class EnsinoFundamental(IMetodoEnsino):
    def ensinar(self, topico: str, contexto: dict) -> str:
        if topico.lower() in ("fração", "frações"):
            return ("Frações representam partes de um todo. Ex.: 1/2 é metade. "
                    "Para somar frações com mesmo denominador, some os numeradores.")
        if topico.lower() in ("multiplicação", "multiplicar"):
            a = contexto.get("a")
            b = contexto.get("b")
            if a is not None and b is not None:
                return (f"{a} × {b} = {a*b}. Multiplicação é somar {a} repetidas {b} vezes.")
        return f"Explicação passo-a-passo sobre '{topico}', com exemplos e exercícios curtos."

class EnsinoMedio(IMetodoEnsino):
    def ensinar(self, topico: str, contexto: dict) -> str:
        if topico.lower() in ("equação", "equações", "equação do 1º grau"):
            return ("Equação do 1º grau: ax + b = 0. Isolamos x: x = -b/a (se a ≠ 0). "
                    "Exercício: resolva 2x + 4 = 0.")
        if topico.lower() in ("derivada", "derivadas"):
            return ("Derivada é a taxa de variação instantânea. Formalmente, f'(x)=lim(h→0)(f(x+h)-f(x))/h.")
        return f"Explicação formal e relacionada a aplicações para '{topico}'."

# ---------------------------
# Contexto: Agente Conversacional
# ---------------------------

@dataclass
class UsuarioPerfil:
    idade: int
    escolaridade: Optional[str] = None

class AgenteConversacional:
    def __init__(self, perfil: UsuarioPerfil):
        self.perfil = perfil
        self._strategy: IMetodoEnsino = self._escolher_strategy_inicial()

    def _escolher_strategy_inicial(self) -> IMetodoEnsino:
        if self.perfil.idade <= 9:
            return EnsinoInfantil()
        if 10 <= self.perfil.idade <= 14:
            return EnsinoFundamental()
        return EnsinoMedio()

    def set_strategy(self, strategy: IMetodoEnsino):
        self._strategy = strategy

    def ensinar(self, topico: str, contexto: dict = None) -> str:
        ctx = contexto or {}
        return self._strategy.ensinar(topico, ctx)

# ---------------------------
# Demonstração (main)
# ---------------------------
def demo():
    print("=== Demo: Agente Conversacional com Strategy Pattern ===\n")
    perfis = [
        UsuarioPerfil(idade=7),
        UsuarioPerfil(idade=12),
        UsuarioPerfil(idade=17)
    ]
    topicos = [("adição", {"a": 2, "b": 3}), ("fração", {}), ("equação", {})]

    for perfil, (topico, ctx) in zip(perfis, topicos):
        agente = AgenteConversacional(perfil)
        resposta = agente.ensinar(topico, ctx)
        print(f"Perfil (idade={perfil.idade}) -> tópico: '{topico}'\nResposta: {resposta}\n")

    agente = AgenteConversacional(UsuarioPerfil(idade=12))
    print("Antes (estratégia automática):", agente.ensinar("multiplicação", {"a": 3, "b": 4}))
    agente.set_strategy(EnsinoInfantil())
    print("Depois (forçando EnsinoInfantil):", agente.ensinar("multiplicação", {"a": 3, "b": 4}))
    print("\n=== Fim da Demo ===\n")

# ---------------------------
# Testes unitários
# ---------------------------
class TestStrategyPattern(unittest.TestCase):
    def test_ensino_infantil_soma(self):
        agente = AgenteConversacional(UsuarioPerfil(idade=6))
        resp = agente.ensinar("adição", {"a": 1, "b": 2})
        self.assertIn("3", resp)
        self.assertIn("maçã", resp)

    def test_ensino_fundamental_fracao(self):
        agente = AgenteConversacional(UsuarioPerfil(idade=12))
        resp = agente.ensinar("fração")
        self.assertIn("partes de um todo", resp)

    def test_ensino_medio_equacao(self):
        agente = AgenteConversacional(UsuarioPerfil(idade=16))
        resp = agente.ensinar("equação")
        self.assertIn("ax + b = 0", resp)

    def test_troca_dinamica_de_estrategia(self):
        agente = AgenteConversacional(UsuarioPerfil(idade=15))
        resp1 = agente.ensinar("multiplicação", {"a":2,"b":5})
        agente.set_strategy(EnsinoInfantil())
        resp2 = agente.ensinar("multiplicação", {"a":2,"b":5})
        self.assertNotEqual(resp1, resp2)

if __name__ == "__main__":
    demo()
    print("Executando testes unitários...\n")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStrategyPattern)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

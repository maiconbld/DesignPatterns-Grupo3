"""
Versão INTERATIVA do Agente Conversacional com integração à API da OpenAI.
Utiliza o modelo 'gpt-4o-mini' e o padrão Strategy Pattern.
"""

import os
from abc import ABC, abstractmethod
from enum import Enum
import openai

# --- CONFIGURAÇÃO DA API OPENAI ---
try:
    client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
except openai.OpenAIError:
    print("Erro: variável OPENAI_API_KEY não configurada.")
    client = None

# --- ENUM: PERFIS DE USUÁRIO ---
class UsuarioPerfil(Enum):
    INFANTIL = "Ensino Infantil"
    FUNDAMENTAL = "Ensino Fundamental"
    MEDIO = "Ensino Médio"

# --- INTERFACE ---
class IMetodoEnsino(ABC):
    @abstractmethod
    def ensinar(self, topico: str) -> str:
        pass

# --- ESTRATÉGIAS CONCRETAS ---
class EnsinoInfantil(IMetodoEnsino):
    def ensinar(self, topico: str) -> str:
        if not client:
            return "API não configurada."
        prompt_sistema = "Você é um professor de matemática para crianças. Fale de forma lúdica e alegre."
        prompt_usuario = f"Explique de forma divertida o que é '{topico}'."
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": prompt_sistema},
                    {"role": "user", "content": prompt_usuario}
                ],
                temperature=0.7,
                max_tokens=150
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao chamar API: {e}"

class EnsinoFundamental(IMetodoEnsino):
    def ensinar(self, topico: str) -> str:
        if not client:
            return "API não configurada."
        prompt_sistema = "Você é um tutor de matemática do ensino fundamental. Use exemplos práticos."
        prompt_usuario = f"Explique o conceito de '{topico}'."
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": prompt_sistema},
                    {"role": "user", "content": prompt_usuario}
                ],
                temperature=0.5,
                max_tokens=200
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao chamar API: {e}"

class EnsinoMedio(IMetodoEnsino):
    def ensinar(self, topico: str) -> str:
        if not client:
            return "API não configurada."
        prompt_sistema = "Você é um professor de matemática do ensino médio. Seja técnico e formal."
        prompt_usuario = f"Discorra sobre o tópico '{topico}'."
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": prompt_sistema},
                    {"role": "user", "content": prompt_usuario}
                ],
                temperature=0.4,
                max_tokens=250
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao chamar API: {e}"

# --- CONTEXTO ---
class AgenteConversacional:
    def __init__(self, perfil: UsuarioPerfil):
        self.perfil = perfil
        self._strategy: IMetodoEnsino = self._get_strategy_for_profile(perfil)
        print(f"Agente iniciado para: {perfil.value}")

    def _get_strategy_for_profile(self, perfil: UsuarioPerfil) -> IMetodoEnsino:
        if perfil == UsuarioPerfil.INFANTIL:
            return EnsinoInfantil()
        elif perfil == UsuarioPerfil.FUNDAMENTAL:
            return EnsinoFundamental()
        elif perfil == UsuarioPerfil.MEDIO:
            return EnsinoMedio()
        else:
            raise ValueError("Perfil inválido")

    def set_perfil(self, perfil: UsuarioPerfil):
        print(f"Mudando perfil para: {perfil.value}")
        self.perfil = perfil
        self._strategy = self._get_strategy_for_profile(perfil)

    def ensinar(self, topico: str) -> str:
        print(f"Buscando explicação sobre '{topico}'...")
        return self._strategy.ensinar(topico)

def selecionar_perfil() -> UsuarioPerfil:
    perfis = list(UsuarioPerfil)
    print("Escolha o nível de ensino:")
    for i, perfil in enumerate(perfis):
        print(f"[{i+1}] - {perfil.value}")
    while True:
        try:
            escolha = int(input("Digite o número: "))
            if 1 <= escolha <= len(perfis):
                return perfis[escolha - 1]
            print("Opção inválida.")
        except ValueError:
            print("Digite um número válido.")

def main():
    if not client:
        print("API não configurada. Configure OPENAI_API_KEY.")
        return
    print("### AGENTE DE MATEMÁTICA GPT-4o-mini ###")
    perfil = selecionar_perfil()
    agente = AgenteConversacional(perfil)
    while True:
        comando = input("\nDigite um tópico ou 'trocar'/'sair': ").strip().lower()
        if comando == "sair":
            print("Até logo!")
            break
        elif comando == "trocar":
            novo_perfil = selecionar_perfil()
            agente.set_perfil(novo_perfil)
        elif comando:
            print(agente.ensinar(comando))
        else:
            print("Entrada inválida.")

if __name__ == "__main__":
    main()

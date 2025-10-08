# 🧠 Agente Conversacional de IA para Matemática Básica

## Introdução ao tema (Design Patterns)

Este repositório contém a implementação prática do **Strategy Pattern** aplicada a um agente conversacional de IA para ensino de matemática básica.

Padrões de Projeto (Design Patterns) são soluções reutilizáveis para problemas comuns que aparecem em um contexto específico de design de software. Eles oferecem um modelo ou um mapa que pode ser empregado para resolver um problema específico em seu código.
Os Padrões de Projeto tornam seu software mais flexível, mais robusto e mais fácil de manter, além de oferecerem uma linguagem compartilhada entre os desenvolvedores, o que torna a comunicação mais simples.

Os principais tipos de Padrões de Projeto são:

- Padrões Criacionais: Estes padrões especificam mecanismos de criação de objetos que tornam o sistema flexível e o código reutilizável. Eles se preocupam com a forma como os objetos são criados, o que torna o sistema independente de como seus objetos são instanciados.
- Padrões Estruturais: Estes padrões se preocupam com a estrutura de classes e objetos para formar estruturas maiores e sistemas mais complicados. Eles simplificam o design, identificando maneiras diretas de realizar relacionamentos entre entidades.
- Padrões Comportamentais: Estes padrões se preocupam com a comunicação e a delegação de tarefas entre os objetos. Eles especificam como os objetos interagem e atribuem responsabilidades, e sua comunicação se torna eficiente e flexível.

## Padrão escolhido
**Strategy Pattern**

No nosso projeto, temos múltiplos métodos de ensino possíveis (teórico, prático, resumido, etc.), e a escolha do método pode variar de acordo com o perfil do usuário ou o contexto do aprendizado.

Sem o Strategy Pattern, seria necessário usar condicionais espalhadas pelo código, algo como:

```
  if perfil == "iniciante":
    ensinar_teoricamente(topico)
  elif perfil == "avancado":
    ensinar_praticamente(topico)

```
Problemas desse approach:

- Código difícil de manter; toda vez que surge um novo método de ensino, precisamos alterar o agente.
- Violação do princípio aberto/fechado (Open/Closed Principle): o código não está aberto para extensão e fechado para modificação.
- Difícil de testar e reutilizar cada método de ensino isoladamente.

O Strategy Pattern resolve isso ao encapsular cada algoritmo de ensino em uma estratégia separada, permitindo trocar métodos de ensino dinamicamente sem modificar a lógica do agente.

## **Strategy Pattern** na arquitetura atual

No projeto, o AgenteConversacional atua como contexto, e cada IMetodoEnsino é uma estratégia concreta.

- O AgenteConversacional não precisa conhecer detalhes do método de ensino; ele apenas chama ensinar(topico, contexto).
- As estratégias concretas (EnsinoTeorico, EnsinoPratico, EnsinoResumido) encapsulam a lógica específica de cada abordagem.
- O perfil do usuário define qual estratégia inicial será usada, mas o sistema ainda permite trocar estratégias dinamicamente via set_strategy.

Esse encaixe mantém o agente flexível, modular e fácil de estender, pois adicionar um novo método de ensino é tão simples quanto criar uma nova classe que implementa IMetodoEnsino.

## **Benefícios**

- Flexibilidade: permite alternar estratégias em tempo de execução.
- Manutenção facilitada: cada método de ensino é independente; alterações não afetam outras estratégias.
- Extensibilidade: novos métodos podem ser adicionados sem modificar o agente.
- Testabilidade: estratégias podem ser testadas isoladamente, melhorando a confiabilidade do código.
- Clareza arquitetural: separa “o que o agente faz” (contexto) de “como ele faz” (estratégia).

## 🎯 Objetivo
Personalizar o ensino de matemática de acordo com o público-alvo:
- **Ensino Infantil:** linguagem lúdica e simples;
- **Ensino Fundamental:** exemplos práticos;
- **Ensino Médio:** explicações técnicas e formais.

## 🧩 Estrutura de classes / Diagrama UML (simplificado)

```
+------------------+
| IMetodoEnsino    |
+------------------+
| + ensinar()      |
+--------^----------+
         |
+--------+--------+--------+
|EnsinoInfantil|EnsinoFundamental|EnsinoMedio|
+---------------+----------------+------------+
        |
+--------------------------+
| AgenteConversacional     |
+--------------------------+
| + set_perfil()           |
| + ensinar()              |
+--------------------------+
```

## Trechos de código ilustrativos

Exemplo: interface e contexto (trecho)
```
from abc import ABC, abstractmethod

# Interface do método de ensino
class IMetodoEnsino(ABC):
    @abstractmethod
    def ensinar(self, topico: str, contexto: dict) -> str:
        pass

# Estratégias concretas
class EnsinoTeorico(IMetodoEnsino):
    def ensinar(self, topico: str, contexto: dict) -> str:
        return f"Explicação teórica sobre {topico}: detalhando conceitos e fundamentos."

class EnsinoPratico(IMetodoEnsino):
    def ensinar(self, topico: str, contexto: dict) -> str:
        return f"Exercício prático de {topico}: aplicando na prática os conceitos."

class EnsinoResumido(IMetodoEnsino):
    def ensinar(self, topico: str, contexto: dict) -> str:
        return f"Resumo rápido de {topico}: principais pontos e ideias-chave."

# Perfil do usuário
class UsuarioPerfil:
    def __init__(self, experiencia: str):
        self.experiencia = experiencia  # "iniciante", "intermediario", "avancado"

# Agente conversacional que usa o Strategy Pattern
class AgenteConversacional:
    def __init__(self, perfil: UsuarioPerfil):
        self.perfil = perfil
        self._strategy = self._escolher_strategy_inicial()

    def _escolher_strategy_inicial(self) -> IMetodoEnsino:
        if self.perfil.experiencia == "iniciante":
            return EnsinoTeorico()
        elif self.perfil.experiencia == "intermediario":
            return EnsinoResumido()
        else:
            return EnsinoPratico()

    def set_strategy(self, strategy: IMetodoEnsino):
        self._strategy = strategy

    def ensinar(self, topico: str, contexto: dict = None) -> str:
        return self._strategy.ensinar(topico, contexto or {})

# Exemplo de uso
perfil = UsuarioPerfil("iniciante")
agente = AgenteConversacional(perfil)

print(agente.ensinar("Python"))
agente.set_strategy(EnsinoPratico())
print(agente.ensinar("Python", {"nivel": "alto"}))

```

## Estrutura do repositório
```
Agente-Conversacional-Matematica/
├─ README.md
├─ requirements.txt
├─ src/
│  └─ agent.py
├─ tests/
│  └─ test.py
└─ .gitignore
```

## Instruções de execução e testes

Requisitos:
- Python 3.8+
- Biblioteca `openai`

Passos:
1. Criar e ativar um ambiente virtual (opcional mas recomendado)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows
   ```
2. Instalar dependências
   ```bash
   pip install -r requirements.txt
   pip install openai
   export OPENAI_API_KEY="sua_chave_api"
   ```
3. Executar demo
```bash
python src/agent.py
```

### Exemplo
```
### AGENTE DE MATEMÁTICA GPT-4o-mini ###
[1] - Ensino Infantil
[2] - Ensino Fundamental
[3] - Ensino Médio
> 2
Digite um tópico: frações
```
## 🧠 Conclusões

A aplicação do Strategy Pattern nesse projeto permitiu a criação de um sistema adaptável e dinâmico, capaz de alterar dinamicamente o método de ensino de acordo com o perfil do usuário ou o ambiente de aprendizagem. Ao dividir de forma clara a lógica do agente das estratégias de ensino, o padrão facilitou um código mais organizado, que se tornou mais fácil de manter, testar e estender, como ao introduzir novos métodos de ensino sem interferir nas funcionalidades existentes.

Além disso, a implementação deste padrão também destacou o encapsulamento de comportamentos e a adaptação dinâmica em sistemas de software, e mostrou como os padrões de projeto podem ser uma ferramenta útil para resolver problemas típicos de design de forma estruturada e eficiente. Apesar de uma camada adicional de abstração, os ganhos em flexibilidade, escalabilidade e clareza superaram os trade-offs, e o sistema se tornou mais robusto e preparado para desenvolvimentos futuros.

Por fim, a experiência trouxe lições instrutivas sobre como equilibrar complexidade e benefícios, criar software focado no usuário e como criar sistemas que são desenvolvidos naturalmente ao longo do tempo, especialmente em sistemas de inteligência artificial e agentes adaptativos.

## Autor(es)
Maicon Dias - 082210032.
Pedro Vieira - 082210025.
Thiago Baptistella - 082210010.

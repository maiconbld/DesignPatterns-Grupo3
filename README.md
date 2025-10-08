# Agente Conversacional de IA para Matemática Básica

## Introdução ao tema (Design Patterns)

Este repositório contém a implementação prática do **Strategy Pattern** aplicada a um agente conversacional de IA para ensino de matemática básica.
Design Patterns são soluções reutilizáveis para problemas recorrentes em engenharia de software. Eles ajudam a organizar código, promover baixo acoplamento e facilitar manutenção e evolução.

## Padrão escolhido
**Strategy Pattern**

- **Problema abordado:** permite alternar algoritmos/estratégias de ensino (ex.: explicação para crianças, explicação para ensino fundamental, explicação para ensino médio) sem condicionalizar o fluxo principal.
- **Resumo:** encapsula famílias de algoritmos (métodos de ensino) e os torna intercambiáveis por meio de uma interface comum.

## Estrutura de classes / Diagrama UML (simplificado)

```
+---------------------+       implements      +---------------------+
|  AgenteConversacional|<---------------------|   IMetodoEnsino     |
|---------------------|                      |---------------------|
| - perfil: Usuario   |                      | + ensinar(topico)   |
| - _strategy         |                      +---------------------+
| + set_strategy()    |                              /|\
| + ensinar()         |                               |
+---------------------+                +--------------+--------------+
                                       |              |              |
                               +---------------+ +---------------+ +---------------+
                               | EnsinoInfantil| |EnsinoFundamental| | EnsinoMedio  |
                               +---------------+ +---------------+ +---------------+
                               | + ensinar()   | | + ensinar()   | | + ensinar()   |
                               +---------------+ +---------------+ +---------------+
```

## Trechos de código ilustrativos

Exemplo: interface e contexto (trecho)
```python
class IMetodoEnsino(ABC):
    @abstractmethod
    def ensinar(self, topico: str, contexto: dict) -> str:
        pass

class AgenteConversacional:
    def __init__(self, perfil: UsuarioPerfil):
        self.perfil = perfil
        self._strategy = self._escolher_strategy_inicial()

    def set_strategy(self, strategy: IMetodoEnsino):
        self._strategy = strategy

    def ensinar(self, topico: str, contexto: dict = None) -> str:
        return self._strategy.ensinar(topico, contexto or {})
```

## Estrutura do repositório
```
Agente-Conversacional-Matematica/
├─ README.md
├─ requirements.txt
├─ src/
│  └─ strategy_agent.py
├─ tests/
│  └─ test_strategy.py
└─ .gitignore
```

## Instruções de execução e testes

Requisitos:
- Python 3.8+

Passos:
1. Criar e ativar um ambiente virtual (opcional mas recomendado)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows
   ```
2. Instalar dependências (nenhuma externa necessária para este exemplo)
   ```bash
   pip install -r requirements.txt
   ```
3. Executar demo + testes (arquivo principal)
   ```bash
   python src/strategy_agent.py
   ```
4. Ou executar testes com pytest/unittest:
   ```bash
   python -m unittest discover -v
   ```

## Conclusões e aprendizados do grupo

- O Strategy Pattern facilita adicionar novos métodos de ensino sem mudar o fluxo do agente.
- Separar responsabilidades (contexto vs estratégia) aumenta testabilidade.
- Em um produto real, combinar Strategy com outros padrões (Factory para criação de estratégias, Decorator para enriquecimento de respostas) aumenta flexibilidade.

## Autor(es)
Maicon Dias - 082210032
Pedro Vieira - 082210025
Thiago Baptistella - 082210010

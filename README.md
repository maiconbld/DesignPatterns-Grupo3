# 🧠 Agente Conversacional de IA para o Ensino de Frações (5º Ano do Ensino Fundamental)

## 📘 Introdução

Este repositório apresenta o desenvolvimento de um **Agente Conversacional de Inteligência Artificial** voltado ao **ensino de frações para alunos do 5º ano do Ensino Fundamental**.  

A solução combina **Design Patterns**, **arquitetura em nuvem** e **integração com modelos de linguagem (LLMs)** para oferecer explicações personalizadas, atividades interativas e recursos visuais que tornam o aprendizado de frações mais acessível e envolvente.

O projeto é uma aplicação prática do **Strategy Pattern**, integrando tecnologias modernas como **Lovable (Front-end)**, **N8n (orquestrador e API Gateway)**, **Supabase (banco de dados)** e **APIs de IA (ChatGPT e Gemini)** — todas conectadas em uma arquitetura modular e escalável hospedada na **Hostinger**.

---

## 🎯 Objetivo Geral

Desenvolver um agente de IA capaz de **ensinar conceitos de frações** de forma **interativa, visual e adaptada ao nível de compreensão de alunos do 5º ano**, utilizando abordagens diferentes (teórica, prática e lúdica) com base no perfil do estudante.

---

## 💡 Padrão de Projeto Utilizado — Strategy Pattern

O **Strategy Pattern** foi aplicado para estruturar diferentes **estratégias de ensino**, tornando o agente capaz de alternar entre explicações **teóricas**, **práticas** e **lúdicas**, conforme o nível do aluno.

### Problema sem Strategy Pattern:
```python
if perfil == "iniciante":
    ensinar_teoricamente(topico)
elif perfil == "avancado":
    ensinar_praticamente(topico)
```

Esse modelo gera alto acoplamento e dificulta a manutenção do código.

### Solução com Strategy Pattern:
Cada método de ensino é uma **classe independente**, e o agente pode alternar entre elas dinamicamente.  
Isso permite um ensino mais adaptável, flexível e alinhado ao perfil pedagógico do aluno.

---

## 🧱 Arquitetura da Solução

A arquitetura proposta segue um modelo **modular e escalável**, integrando front-end, backend, APIs e armazenamento de dados.

### 🔹 Visão Geral

```
[Lovable Front-end] → Webhook (HTTP POST)
        ↓
     [N8n - API Gateway / Backend]
        ↓
[ChatGPT / Gemini APIs] ←→ [Supabase Storage]
        ↓
Resposta JSON → Lovable
```

### 🔹 Componentes Principais

| Camada | Componente | Função |
|--------|-------------|--------|
| **Front-end** | **Lovable (React 18)** | Interface lúdica e interativa para alunos, com chat educativo. |
| **Backend / Orquestração** | **N8n (Node.js)** | Processa perguntas, conecta APIs e gerencia fluxos de conversa. |
| **IA Conversacional** | **ChatGPT (GPT-4o)** | Gera explicações e exercícios de frações. |
| **IA Visual** | **Gemini 2.0 Flash** | Cria imagens didáticas, como pizzas ou barras fracionadas. |
| **Banco de Dados** | **Supabase (PostgreSQL)** | Armazena interações, progresso e desempenho dos alunos. |
| **Hospedagem** | **Hostinger (VM)** | Ambiente de produção com execução do N8n e APIs. |

---

## ⚙️ Pipeline DevSecOps

O ciclo de desenvolvimento segue boas práticas de **DevSecOps**, garantindo qualidade, segurança e automação contínua.

### **Etapas do Pipeline**

1. **Source (SAST)** — análise estática de segurança com **Semgrep** e **Gitleaks**.  
2. **Build** — instalação de dependências e escaneamento de vulnerabilidades com **Trivy**.  
3. **Test (DAST)** — testes de segurança dinâmicos com **OWASP ZAP**.  
4. **Release** — validação e aprovação automatizada do build.  
5. **Deploy** — publicação automatizada em produção (Hostinger / Docker).

---

## 🧩 Estrutura do Projeto (Strategy Pattern)

```
+------------------+
| IMetodoEnsino    |
+------------------+
| + ensinar()      |
+--------^----------+
         |
+--------+--------+--------+
|EnsinoTeorico|EnsinoPratico|EnsinoLudico|
+---------------+-------------+-----------+
        |
+--------------------------+
| AgenteConversacional     |
+--------------------------+
| + set_perfil()           |
| + ensinar()              |
+--------------------------+
```

---

## 💻 Exemplo de Implementação

```python
from abc import ABC, abstractmethod

class IMetodoEnsino(ABC):
    @abstractmethod
    def ensinar(self, topico: str, contexto: dict) -> str:
        pass

class EnsinoTeorico(IMetodoEnsino):
    def ensinar(self, topico, contexto):
        return f"Frações são partes de um todo. Por exemplo, 1/2 de uma pizza."

class EnsinoPratico(IMetodoEnsino):
    def ensinar(self, topico, contexto):
        return f"Vamos praticar: se você tem 8 pedaços e comeu 3, comeu 3/8 da pizza!"

class EnsinoLudico(IMetodoEnsino):
    def ensinar(self, topico, contexto):
        return f"Imagine dividir um chocolate entre amigos! Cada um fica com uma fração do total 🍫."

class UsuarioPerfil:
    def __init__(self, experiencia: str):
        self.experiencia = experiencia

class AgenteConversacional:
    def __init__(self, perfil: UsuarioPerfil):
        self.perfil = perfil
        self._strategy = self._escolher_strategy()

    def _escolher_strategy(self):
        if self.perfil.experiencia == "iniciante":
            return EnsinoLudico()
        elif self.perfil.experiencia == "intermediario":
            return EnsinoTeorico()
        else:
            return EnsinoPratico()

    def ensinar(self, topico, contexto=None):
        return self._strategy.ensinar(topico, contexto or {})

perfil = UsuarioPerfil("iniciante")
agente = AgenteConversacional(perfil)
print(agente.ensinar("frações"))
```

---

## 📂 Estrutura do Repositório

```
agente-frações/
├─ README.md
├─ .github/
│  └─ workflows/
│     └─ devsecops.yml
├─ src/
│  ├─ agent.py
│  ├─ strategies/
│  │  ├─ ensino_teorico.py
│  │  ├─ ensino_pratico.py
│  │  └─ ensino_ludico.py
│  └─ pipeline/
│     └─ n8n_flow.json
├─ tests/
│  └─ test_strategy.py
└─ requirements.txt
```

---

## 🧪 Testes

Testes automatizados com `unittest` verificam:
- Seleção correta da estratégia conforme o perfil do aluno;
- Comportamento independente de cada método de ensino;
- Troca dinâmica de estratégias durante a execução.

```bash
python -m unittest tests/test_strategy.py
```

---

## 🧠 Conclusão

A aplicação do **Strategy Pattern** neste projeto educacional mostrou-se ideal para criar um sistema **flexível, dinâmico e adaptável ao aprendizado infantil**.  
O agente consegue **ensinar frações de modo visual, prático e divertido**, ajustando sua linguagem conforme o perfil do estudante.  

A arquitetura baseada em **N8n + Lovable + Supabase + APIs de IA** garante escalabilidade e fácil manutenção, enquanto o **pipeline DevSecOps** automatiza testes, segurança e deploy.  
Assim, a solução une **pedagogia e tecnologia**, promovendo um ensino digital mais humano e personalizado.

---

## 👨‍💻 Autores
- Maicon Dias — 082210032  
- Pedro Vieira — 082210025  
- Thiago Baptistella — 082210010  

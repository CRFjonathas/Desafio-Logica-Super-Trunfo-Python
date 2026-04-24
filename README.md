<h1 align="center">🃏 Super Trunfo - Python OOP Architecture</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge" alt="Project Status">
  <img src="https://img.shields.io/badge/Paradigma-POO-orange?style=for-the-badge" alt="Paradigm">
  <img src="https://img.shields.io/badge/Arquitetura-Clean%20Code-brightgreen?style=for-the-badge" alt="Clean Code">
</p>

---

## 📌 Índice
- [Sobre o Projeto](#-sobre-o-projeto)
- [Arquitetura e Padrões (Under the Hood)](#-arquitetura-e-padrões-under-the-hood)
- [Demonstração Visual](#-demonstração-visual)
- [Funcionalidades](#-funcionalidades)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação e Execução](#-instalação-e-execução)
- [Estrutura de Pastas](#-estrutura-de-pastas)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## 📖 Sobre o Projeto

Este repositório é uma evolução completa do clássico jogo "Super Trunfo", reescrito em **Python**. O que começou como um script imperativo em níveis (Novato, Aventureiro, Mestre) foi totalmente refatorado para o paradigma de **Programação Orientada a Objetos (POO)**.

O objetivo principal desta versão é demonstrar um design de software maduro, com clara separação de responsabilidades, facilitando testes, manutenibilidade e escalabilidade do código.

---

## 🏗 Arquitetura e Padrões (Under the Hood)

A arquitetura do projeto foi dividida em classes especializadas, aplicando conceitos fundamentais de Engenharia de Software:

- **Separação de Responsabilidades (SRP):**
  - A interface com o usuário e a coleta de dados (I/O) foram isoladas na classe `Cadastrar`.
  - A lógica de menu e seleção de opções foi centralizada na classe `Menu`.
  - As regras de negócio e comparação de cartas vivem exclusivamente na classe `Jogo`.
- **Encapsulamento e Propriedades Virtuais:** A classe `Carta` protege seus atributos base (como `_populacao` e `_pib`) e utiliza decoradores `@property` para calcular atributos derivados dinamicamente, como `densidade_populacional`, `pib_per_capita` e `super_poder`.
- **Metaprogramação e Acesso Dinâmico:** Para evitar cadeias longas de `if/else` ou `match-case` na hora da comparação, a classe `Jogo` utiliza a função nativa `getattr()` do Python para recuperar dinamicamente o valor do atributo escolhido pelo jogador.
- **Magic Methods (Dunder Methods):** A classe `Baralho` implementa `__len__` e `__iter__`, permitindo que o objeto se comporte como uma coleção nativa do Python e seja iterado facilmente em loops. As representações textuais também foram sobrescritas com `__str__` e `__repr__` na classe `Carta`.
- **Mapeamento de Estruturas de Dados:** A classe `Menu` utiliza dicionários (Hash Maps) em vez de condicionais para mapear as entradas do usuário aos atributos internos das classes, garantindo uma busca O(1) e código mais limpo.

---

## 🖼 Demonstração Visual

### 📝 Cadastro de Cartas
<img width="313" height="375" alt="Cadastro de Cartas" src="https://github.com/user-attachments/assets/beacc86b-0f11-45ec-b24e-ef0ce279c17d" />

### 📊 Exibição dos Dados
<img width="308" height="413" alt="Exibição dos Dados" src="https://github.com/user-attachments/assets/b8957cf0-bdc5-46d9-b8fd-049a55bf15f9" />

### 🎛️ Menu Interativo
<img width="343" height="235" alt="Menu" src="https://github.com/user-attachments/assets/f3ac7072-f074-4af7-b94b-12f8f5e9972c" />

### ⚔️ Comparação de Atributos
<img width="347" height="333" alt="Comparação" src="https://github.com/user-attachments/assets/7f71ddb6-7592-4660-b37d-598b308655dc" />

---

## ✨ Funcionalidades

- [x] **Cadastro Dinâmico:** Inserção de dados de Cidades/Estados via linha de comando interativa.
- [x] **Cálculo de Super Poder:** Fórmula automática englobando População, Área, PIB, Pontos Turísticos, PIB per Capita e o inverso da Densidade Populacional.
- [x] **Lógica de Inversão:** Sistema de comparação inteligente, onde para o atributo "Densidade Populacional", a carta com o *menor* valor é declarada vencedora.
- [x] **Tratamento de Exceções:** Prevenção contra entradas inválidas (ex: strings onde números são esperados) durante a seleção de atributos.

---

## 🛠 Pré-requisitos

* [Python 3.10+](https://www.python.org/downloads/)
* Git para controle de versão

---

## 🚀 Instalação e Execução

### 1. Clonando o Repositório
```bash
git clone https://github.com/CRFjonathas/Desafio-Logica-Super-Trunfo-Python
cd Desafio-Logica-Super-Trunfo-Python
```

### 2. Rodando o Projeto

Com a arquitetura modular baseada no arquivo `__main__.py`, a execução ocorre na raiz do diretório de forma direta:

```bash
# Na raiz do projeto, execute:

python .

# Ou executando o entrypoint diretamente:

python __main__.py
```
Siga os prompts do terminal para cadastrar as duas primeiras cartas, analisar seus dados na tela e selecionar o atributo pelo qual as cidades devem duelar.

---

## 📂 Estrutura de Pastas

```text
📂 desafio-logica-super-trunfo-python
├── 📂 .github
│   └── 📄 PULL_REQUEST_TEMPLATE.md  # Template padronizado de Pull Request
├── 📂 classes                       # Core da arquitetura POO
│   ├── 📄 Baralho.py                # Implementação de coleção iterável
│   ├── 📄 Cadastrar.py              # Classe dedicada ao I/O de usuários
│   ├── 📄 Carta.py                  # Entidade com encapsulamento e propriedades
│   ├── 📄 Jogo.py                   # Motor dinâmico de regras e vitórias
│   └── 📄 Menu.py                   # Interface e router de comandos (CLI)
├── 📄 .gitignore                    # Regras para exclusão de cache do Python
├── 📄 __main__.py                   # Entrypoint orquestrador
└── 📄 README.md                     # Documentação de alto nível
```

---

## 🤝 Contribuindo

O código foi pensado de forma desacoplada para facilitar contribuições. Temos um template dedicado para tornar o review process o mais claro possível.

1. Faça um **Fork** do projeto.

2. Crie uma **Branch** descrevendo a nova feature (`git checkout -b feature/ImplementarPersistenciaDB`).

3. Dê um **Commit** evidenciando as mudanças (`git commit -m 'feat: Adiciona integração inicial com SQLite'`).

4. Faça um **Push** para a Branch (`git push origin feature/ImplementarPersistenciaDB`).

5. Abra um **Pull Request** detalhando sua implementação.

---

## 📄 Licença

Projeto distribuído sob a licença **MIT**. A utilização do código é livre para fins de estudo e aplicações em arquitetura de soluções.

---

## ✉️ Contato

Desenvolvido por **Jonathas Nicacio**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/crfjonathas)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jonathasnicacio-dev/)

<p align="center">Feito com 🐍 focando em boas práticas de Engenharia de Software.</p>

```

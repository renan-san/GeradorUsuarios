# 🎲 Gerador de Usuários Aleatórios (GUI)

Uma aplicação desktop simples desenvolvida em **Python** que gera perfis de usuários fictícios (com dados brasileiros) e os armazena automaticamente em um arquivo JSON.

## 📋 Sobre o Projeto

Este projeto utiliza a biblioteca `Faker` para criar dados realistas e `Tkinter` para a interface gráfica. O objetivo é fornecer uma ferramenta rápida para gerar "massa de dados" para testes ou preenchimento de bancos de dados, salvando o histórico das gerações.

### ✨ Funcionalidades

* **Geração de Dados:** Cria Nome, Idade (18-35) e Profissão.
* **Localização:** Dados gerados no padrão brasileiro (`pt-BR`).
* **Persistência:** Salva cada usuário gerado em uma lista acumulativa no arquivo `usuarios.json`.
* **Interface Gráfica:** Visualização imediata dos dados gerados na tela.

## 🛠️ Tecnologias Utilizadas

* [Python 3](https://www.python.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html) (Interface Gráfica)
* [Faker](https://faker.readthedocs.io/) (Geração de dados)
* [Pillow (PIL)](https://python-pillow.org/) (Manipulação de imagens/ícones)
* JSON (Armazenamento de dados)

## 🚀 Como Executar

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina.

### 1. Instalação das Dependências

Abra o terminal na pasta do projeto e instale as bibliotecas necessárias executando:

```bash
pip install faker Pillow

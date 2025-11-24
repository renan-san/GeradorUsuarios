
📘 Gerador de Usuários (Python + Tkinter)

Este projeto é um gerador de usuários utilizando a biblioteca Faker, com interface gráfica construída em Tkinter.
A cada clique no botão, o sistema cria uma pessoa aleatória com:

Nome completo

Idade

Profissão

E registra todos os usuários gerados em um arquivo JSON (usuarios.json).

🖼️ Interface (Tkinter)

A aplicação possui:

✔️ Janela gráfica
✔️ Botão para gerar novos usuários
✔️ Exibição dos dados criados
✔️ Ícone personalizado

🚀 Funcionalidades

Gera dados realistas utilizando Faker (nome e profissão brasileiros).

Interface intuitiva construída com Tkinter.

Salva todos os usuários criados em um arquivo usuarios.json.

Sistema totalmente offline.

Código simples e fácil de modificar.

📦 Tecnologias Utilizadas

Python 3

Tkinter (GUI)

Faker

Pillow (para carregar o ícone da janela)

📥 Instalação

Clone ou baixe o repositório:

git clone <seu-repositorio>


Instale as dependências:

pip install faker pillow


Tenha certeza de que o diretório contém a imagem:

images/imgpy.png


Execute o programa:

python app.py

🗂️ Estrutura do Projeto
📁 projeto/
├── app.py
├── usuarios.json
├── README.md
└── images/
    └── imgpy.png

📝 Como o Programa Funciona

O usuário clica no botão Gerar um usuário

A função criar_pessoa() gera:

Nome

Idade (entre 18 e 35)

Profissão

A interface atualiza os dados na tela

O usuário é salvo no usuarios.json através da função salvar_usuarios()

⚠️ Observações Importantes

Tkinter não funciona no Google Colab, então o projeto deve ser executado localmente.

Se a imagem não carregar, verifique o caminho: images/imgpy.png.

📄 Licença

Este projeto está sob a licença MIT.
Sinta-se à vontade para usar, estudar e modificar.

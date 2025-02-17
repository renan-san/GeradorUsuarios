from faker import Faker
from PIL import Image as PilImage, ImageTk
import random
import json
from tkinter import *
import tkinter as tk

usuarios = []  

def criar_pessoa():
    fake = Faker("pt-BR")
    idade = random.randint(18, 35)
    profissao = fake.job()

    pessoa = {
        "Nome": fake.name(),
        "Idade": idade,
        "Profissão": profissao,
    }

    usuarios.append(pessoa)
    
    texto_usuario.set(f"Nome: {pessoa['Nome']}\nIdade: {pessoa['Idade']}\nProfissão: {pessoa['Profissão']}")
    
    salvar_usuarios()

def salvar_usuarios():
    try:
        with open("usuarios.json", "w", encoding="utf-8") as f:
            json.dump(usuarios, f, ensure_ascii=False, indent=4)
        print("Usuários salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar os usuários: {e}")

janela = Tk()
janela.title("Gerador")
janela.geometry("800x400")
janela.config(background="#4682B4")

caminho_imagem = "images/imgpy.png"

try:
    img = PilImage.open(caminho_imagem)
    icon = ImageTk.PhotoImage(img)
    janela.wm_iconphoto(True, icon)
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")
  
texto_usuario = StringVar()

label_usuario = tk.Label(janela, textvariable=texto_usuario, justify="left", font=("Franklin Gothic Medium", 15),fg="white", bg="#4682B4")
label_usuario.config(background="#4682B4")
label_usuario.place(x=260, y=120)

botao = tk.Button(janela, text="Gerar um usuário", command=criar_pessoa, font=("Franklin Gothic Medium", 12))
botao.place(x=340, y=330)

janela.mainloop()

import tkinter as tk
from tkinter import messagebox
import db
import funcoes
import interface

def iniciar_interface_cadastro():
    global root

    def registrar_tutor():
        nome = nome_entry.get()
        cpf = cpf_entry.get()
        equipe = equipe_var.get()  # Alterado para pegar valor da OptionMenu

        # Verifica se todos os campos foram preenchidos
        if not nome or not cpf or not equipe:
            messagebox.showwarning("Campos faltando", "Por favor, preencha todos os campos.")
            return

        # Valida o CPF
        if not funcoes.validar_cpf(cpf):
            messagebox.showwarning("CPF inválido", "Por favor, insira um CPF válido.")
            return

        # Verifica se o tutor já existe
        if db.buscar_tutor_por_cpf(cpf):
            messagebox.showwarning("CPF já cadastrado", "Este CPF já está cadastrado.")
            return

        # Registra o tutor no banco de dados
        db.adicionar_tutor(nome, cpf, equipe)
        messagebox.showinfo("Sucesso", "Tutor registrado")
        encerrar_interface_cadastro()  # Encerra a janela após o cadastro
        interface.iniciar_interface_ponto()  # Abre a interface principal

    root = tk.Tk()
    root.title("Cadastro de Tutor")
    root.geometry("300x200")

    nome_label = tk.Label(root, text="Nome Completo")
    nome_label.pack()
    nome_entry = tk.Entry(root, justify='center')  # Centraliza o texto digitado
    nome_entry.pack()

    cpf_label = tk.Label(root, text="CPF")
    cpf_label.pack()
    cpf_entry = tk.Entry(root, justify='center')  # Centraliza o texto digitado
    cpf_entry.pack()

    equipe_label = tk.Label(root, text="Equipe")
    equipe_label.pack()
    equipe_var = tk.StringVar(root)
    equipe_var.set("Equipe 1")  # valor inicial
    equipe_options = ["Equipe "+str(i) for i in range(1, 11)]  # cria uma lista de equipes de "Equipe 1" a "Equipe 10"
    equipe_entry = tk.OptionMenu(root, equipe_var, *equipe_options)
    equipe_entry.pack()

    registrar_button = tk.Button(root, text="Registrar Tutor", command=registrar_tutor, bg='blue')  # Cor do botão alterada para azul
    registrar_button.pack(pady=5)  # Adiciona um pequeno espaço entre o widget "Equipe" e o botão "Registrar Tutor"

    root.mainloop()

def encerrar_interface_cadastro():
    global root
    root.quit()  # encerra o loop principal
    root.destroy()  # destrói a janela

if __name__ == "__main__":
    iniciar_interface_cadastro()

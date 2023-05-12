import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pytz
import funcoes
import db

# Criação da tabela de registros de ponto no banco de dados
db.criar_tabela_registros_ponto()

# Função para atualizar o relógio na interface
def update_clock():
    # Pega o horário atual e formata como uma string
    now = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%H:%M:%S")
    # Atualiza o texto do label do relógio
    data_hora_label.config(text=now)
    # Chama a função novamente após 1000 milissegundos
    root.after(1000, update_clock)

# Função para registrar o ponto
def registrar_ponto():
    # Pega as entradas do usuário
    funcionario_id = id_entry.get()
    cpf = cpf_entry.get()
    tipo = tipo_var.get()
    # Pega a data e hora atual
    data_hora = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%Y-%m-%d %H:%M:%S")

    # Verifica se todas as entradas necessárias foram preenchidas
    if not funcionario_id or not cpf or not tipo:
        # Se não, mostra uma mensagem de aviso
        messagebox.showwarning("Campos faltando", "Por favor, preencha todos os campos.")
        return

    # Registra o ponto no banco de dados
    funcoes.registrar_ponto(funcionario_id, cpf, tipo, data_hora)
    # Mostra uma mensagem de sucesso
    messagebox.showinfo("Sucesso", "Ponto registrado")

# Função para listar os pontos registrados
def listar_pontos():
    # Pega o ID do funcionário
    funcionario_id = id_entry.get()
    # Pega a lista de pontos do banco de dados
    pontos = funcoes.listar_pontos(funcionario_id)
    # Limpa a Listbox
    listbox.delete(0, tk.END)
    # Adiciona cada ponto na Listbox
    for i in pontos:
        listbox.insert(tk.END, i)

# Função para alterar a opção de tipo de ponto
def change_option(*args):
    # Dicionário para ciclar as opções
    options_cycle = {"1º Entrada": "1º Saída", "1º Saída": "2º Entrada", "2º Entrada": "2º Saída", "2º Saída": "1º Entrada"}
    # Altera a opção atual para a próxima do ciclo
    tipo_var.set(options_cycle[tipo_var.get()])

# Criação da janela principal
root = tk.Tk()
root.title("Ponto Eletrônico - Tutores")
root.geometry("400x400")

# Criação dos widgets da interface e adição deles na grid
id_label = tk.Label(root, text="Nome do Tutor")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = tk.Entry(root, justify='center')
id_entry.grid(row=0, column=1, padx=10)

cpf_label = tk.Label(root, text="CPF do Tutor")
cpf_label.grid(row=1, column=0, padx=10, pady=10)
cpf_entry = tk.Entry(root, justify='center')
cpf_entry.grid
cpf_entry.grid(row=1, column=1, padx=10)

# Configuração do rótulo para exibir a data e hora atual
data_hora_label = tk.Label(root, text="", font=("Helvetica", 48))
data_hora_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
# Chama a função para atualizar o relógio
update_clock()

# Configuração do campo de opções para o tipo de ponto
tipo_label = tk.Label(root, text="Tipo de Ponto")
tipo_label.grid(row=3, column=0, padx=10, pady=10)
tipo_var = tk.StringVar(root)
tipo_var.set("1º Entrada")  # valor inicial
tipo_options = ["1º Entrada", "1º Saída", "2º Entrada", "2º Saída"]
tipo_entry = tk.OptionMenu(root, tipo_var, *tipo_options)
tipo_entry.grid(row=3, column=1, padx=10)

# Configuração do botão para registrar ponto
registrar_button = tk.Button(root, text="Registrar Ponto", command=registrar_ponto)
registrar_button.config(width=15, bg='green')
registrar_button.grid(row=4, column=0, padx=10, pady=10)

# Configuração do botão para listar os pontos
listar_button = tk.Button(root, text="Listar Pontos", command=listar_pontos)
listar_button.grid(row=4, column=1, padx=10, pady=10)

# Configuração da listbox para listar os pontos
listbox = tk.Listbox(root)
listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

# Configuração das barras de rolagem para a listbox
scrollbar_y = tk.Scrollbar(listbox)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar_x = tk.Scrollbar(listbox, orient=tk.HORIZONTAL)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

# Configuração das barras de rolagem para interagir com a listbox
listbox.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
scrollbar_y.config(command=listbox.yview)
scrollbar_x.config(command=listbox.xview)

# Configuração da janela principal para expandir a listbox e as barras de rolagem conforme o tamanho da janela
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(1, weight=1)

# Inicialização do loop principal da interface
root.mainloop()

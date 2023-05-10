import tkinter as tk
from tkinter import messagebox
from datetime import datetime
try:
    import funcoes
    import db
    import pytz
except ImportError as e:
    print(f"Erro ao importar módulos: {e}")
    exit(1)

try:
    db.criar_tabela_registros_ponto()
except Exception as e:
    print(f"Erro ao criar tabela no banco de dados: {e}")
    exit(1)

def update_clock():
    try:
        now = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%H:%M:%S")
        data_hora_label.config(text=now)
        root.after(1000, update_clock)
    except Exception as e:
        print(f"Erro ao atualizar o relógio: {e}")

def registrar_ponto():
    try:
        funcionario_id = id_entry.get()
        cpf = cpf_entry.get()
        tipo = tipo_var.get()

        data_hora = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%Y-%m-%d %H:%M:%S")
        funcoes.registrar_ponto(funcionario_id, cpf, tipo, data_hora)
        messagebox.showinfo("Sucesso", "Ponto registrado")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao registrar ponto: {e}")

def listar_pontos():
    try:
        funcionario_id = id_entry.get()
        pontos = funcoes.listar_pontos(funcionario_id)
        listbox.delete(0, tk.END)

        for i in pontos:
            listbox.insert(tk.END, i)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao listar pontos: {e}")

def change_option(*args):
    try:
        options_cycle = {"1º Entrada": "1º Saída", "1º Saída": "2º Entrada", "2º Entrada": "2º Saída", "2º Saída": "1º Entrada"}
        tipo_var.set(options_cycle[tipo_var.get()])
    except KeyError:
        messagebox.showerror("Erro", "Tipo de ponto inválido.")

try:
    root = tk.Tk()
    root.title("Ponto Eletrônico - Tutores")
    root.geometry("400x400")

    id_label = tk.Label(root, text="Nome do Tutor")
    id_label.pack()
    id_entry = tk.Entry(root, justify='center')
    id_entry.pack()

    cpf_label = tk.Label(root, text="CPF do Tutor")
    cpf_label.pack()
    cpf_entry = tk.Entry(root, justify='center')
    cpf_entry.pack()

    data_hora_label = tk.Label(root, text="", font=("Helvetica", 48))
    data_hora_label.pack()
    update_clock()

    tipo_label = tk.Label(root, text="Tipo de Ponto")
    tipo_label.pack()

    # menu de opções para o tipo de ponto
    tipo_var = tk.StringVar(root)
    tipo_var.set("1º Entrada")  # valor inicial
    tipo_options = ["1º Entrada", "1º Saída", "2º Entrada", "2º Saída"]
    tipo_entry = tk.OptionMenu(root, tipo_var, *tipo_options)
    tipo_entry.pack()

    registrar_button = tk.Button(root, text="Registrar Ponto", command=registrar_ponto) 
    registrar_button.config(width=15, bg='green') 
    registrar_button.pack() 

    listar_button = tk.Button(root, text="Listar Pontos", command=listar_pontos)
    listar_button.pack()

    listbox = tk.Listbox(root)
    listbox.pack(fill=tk.BOTH, expand=True)

    # barras de rolagem
    scrollbar_y = tk.Scrollbar(listbox)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbar_x = tk.Scrollbar(listbox, orient=tk.HORIZONTAL)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    # barras de rolagem com a listbox
    listbox.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    scrollbar_y.config(command=listbox.yview)
    scrollbar_x.config(command=listbox.xview)

    root.mainloop()

except Exception as e:
    print(f"Erro ao iniciar a interface gráfica: {e}")
    exit(1)

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pytz
import funcoes
import db
import cadastro_tutor



def iniciar_interface_ponto():
    global root
    root = tk.Tk()
    root.title("Ponto Eletrônico - Tutores")
    root.geometry("350x400")

    # Criação da tabela de tutores e registros de ponto no banco de dados
    db.criar_tabela_tutores()
    db.criar_tabela_registros_ponto()

    def update_clock():
        now = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%H:%M:%S")
        data_hora_label.config(text=now)
        root.after(1000, update_clock)

    def registrar_ponto():
        cpf = cpf_entry.get()
        tipo = tipo_var.get()
        data_hora = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%Y-%m-%d %H:%M:%S")

        if not cpf or not tipo:
            messagebox.showwarning("Campos faltando", "Por favor, preencha todos os campos.")
            return

        # Verifica se o CPF está cadastrado no banco de dados
        if not db.buscar_tutor_por_cpf(cpf):
            messagebox.showwarning("CPF não cadastrado", "Este CPF não está cadastrado.")
            return

        funcoes.registrar_ponto(cpf, tipo, data_hora)
        messagebox.showinfo("Sucesso", "Ponto registrado")

    def listar_pontos():
        cpf = cpf_entry.get()
        pontos = funcoes.listar_pontos(cpf)
        listbox.delete(0, tk.END)
        if pontos:
            for ponto in pontos:
                horas_trabalhadas = ponto['horas_trabalhadas'].total_seconds() / 3600  # Converter segundos em horas
                horas_trabalhadas_formatadas = "{:02.0f}:{:02.0f}".format(*divmod(horas_trabalhadas * 60, 60))
                color = 'green' if horas_trabalhadas >= 8 else 'red'
                listbox.insert(tk.END, f"Nome: {ponto['nome']}, CPF: {ponto['cpf']}, Data e Hora: {ponto['data_hora']}, Tipo: {ponto['tipo']}, Horas Trabalhadas: {horas_trabalhadas_formatadas}")
                listbox.itemconfig(tk.END, {'bg': color})

        else:
            messagebox.showinfo("Sem pontos", "Não há pontos registrados para esse CPF.")


    def abrir_janela_cadastro():
        encerrar_interface_ponto()
        cadastro_tutor.iniciar_interface_cadastro()

    cpf_entry = tk.Entry(root, justify='center')
    cpf_entry.insert(0, "CPF do Tutor")  # Adiciona o texto 'CPF do Tutor' no campo de entrada
    cpf_entry.bind("<FocusIn>", lambda args: cpf_entry.delete('0', 'end') if cpf_entry.get() == "CPF do Tutor" else None)  # Limpa o campo somente se o texto for 'CPF do Tutor'
    cpf_entry.grid(row=0, column=0, padx=10, pady=5, columnspan=2)  # Centraliza o campo de entrada do CPF

    data_hora_label = tk.Label(root, text="", font=("Helvetica", 48))
    data_hora_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
    update_clock()

    tipo_var = tk.StringVar(root)
    tipo_var.set("1º Entrada")  # valor inicial
    tipo_options = ["1º Entrada", "1º Saída", "2º Entrada", "2º Saída"]

    tipo_entry = tk.OptionMenu(root, tipo_var, *tipo_options)
    tipo_entry.grid(row=2, column=0, padx=10, pady=5, columnspan=2)

    registrar_button = tk.Button(root, text="Registrar Ponto", command=registrar_ponto)
    registrar_button.config(width=15, bg='green')
    registrar_button.grid(row=3, column=0, padx=10, pady=5, columnspan=2)

    listar_button = tk.Button(root, text="Listar Pontos", command=listar_pontos)
    listar_button.grid(row=4, column=1, padx=10, pady=5)

    listbox = tk.Listbox(root, height=10)  # Increased the height of the listbox
    listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

    cadastro_button = tk.Button(root, text="Cadastre-se", command=abrir_janela_cadastro)
    cadastro_button.grid(row=6, column=0, padx=10, pady=5, columnspan=2)  # Move the 'Register' button below the listbox

    scrollbar_y = tk.Scrollbar(listbox)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar_x = tk.Scrollbar(listbox, orient=tk.HORIZONTAL)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    listbox.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    scrollbar_y.config(command=listbox.yview)
    scrollbar_x.config(command=listbox.xview)

    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()

def encerrar_interface_ponto():
    global root
    root.quit()  # encerra o loop principal
    root.destroy()  # destrói a janela

if __name__ == "__main__":
    iniciar_interface_ponto()


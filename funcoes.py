import db
from tkinter import messagebox
from datetime import datetime

# Função para verificar se um CPF é válido
def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(c for c in cpf if c.isdigit())

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum((int(a) * b) for a, b in zip(cpf[:9], range(10, 1, -1)))
    d1 = (soma * 10 % 11) % 10
    if d1 != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = sum((int(a) * b) for a, b in zip(cpf[:10], range(11, 1, -1)))
    d2 = (soma * 10 % 11) % 10
    if d2 != int(cpf[10]):
        return False

    return True

def registrar_ponto(cpf, tipo, data_hora):
    # Verifica se o tutor existe
    if not db.buscar_tutor_por_cpf(cpf):
        messagebox.showwarning("Tutor não cadastrado", "Este CPF não está cadastrado. Por favor, clique no botão 'Cadastre-se'.")
        return

    # Busca o ID do tutor a partir do CPF
    funcionario_id = db.buscar_id_do_funcionario_por_cpf(cpf)
    if not funcionario_id:
        messagebox.showwarning("Erro", "Não foi possível encontrar um ID de funcionário para este CPF.")
        return

    conn = db.conectar()
    query = "INSERT INTO registros_ponto (funcionario_id, data_hora, tipo) VALUES (?, ?, ?)"
    db.executar_query(conn, query, (funcionario_id, data_hora, tipo))
    conn.close()


def listar_pontos(cpf):
    funcionario = db.buscar_id_nome_cpf_do_funcionario_por_cpf(cpf)
    if funcionario is None:
        return None

    conn = db.conectar()
    query = "SELECT * FROM registros_ponto WHERE funcionario_id = ? ORDER BY data_hora"
    registros = db.buscar_query(conn, query, (funcionario['id'],))
    conn.close()

    # Agora vamos calcular o tempo trabalhado e adicionar aos registros
    registros_formatados = []
    for i in range(0, len(registros), 2):  # Vamos iterar a cada dois registros (entrada e saída)
        if i+1 < len(registros):  # Verificar se há um par para o registro atual
            entrada = datetime.strptime(registros[i]['data_hora'], '%Y-%m-%d %H:%M:%S')
            saida = datetime.strptime(registros[i+1]['data_hora'], '%Y-%m-%d %H:%M:%S')
            horas_trabalhadas = saida - entrada
            registros[i].update({'horas_trabalhadas': horas_trabalhadas})

            # Formatando o registro para melhor apresentação
            registro_formatado = {'nome': funcionario['nome'], 'cpf': funcionario['cpf'], 'data_hora': registros[i]['data_hora'], 'tipo': registros[i]['tipo'], 'horas_trabalhadas': horas_trabalhadas}
            registros_formatados.append(registro_formatado)

    return registros_formatados


def remover_ponto(id):
    conn = db.conectar()
    query = "DELETE FROM registros_ponto WHERE id = ?"
    db.executar_query(conn, query, (id,))
    conn.close()

def atualizar_ponto(id, funcionario_id, data_hora, tipo):
    conn = db.conectar()
    query = "UPDATE registros_ponto SET funcionario_id = ?, data_hora = ?, tipo = ? WHERE id = ?"
    db.executar_query(conn, query, (funcionario_id, data_hora, tipo, id))
    conn.close()

def deletar_todos_registros():
    tabelas = ['registros_ponto', 'tutores']  # Lista de todas as tabelas para deletar registros
    for tabela in tabelas:
        conn = db.conectar()
        query = f"DELETE FROM {tabela}"
        db.executar_query(conn, query)
        conn.close()
    messagebox.showinfo("Sucesso", "Todos os registros foram excluídos.")


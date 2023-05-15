import sqlite3

# Função para estabelecer uma conexão com o banco de dados SQLite
def conectar():
    conn = sqlite3.connect("ponto_eletronico.db")
    return conn

# Função para criar a tabela tutores no banco de dados SQLite
def criar_tabela_tutores():
    conn = conectar()
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS tutores (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        equipe TEXT NOT NULL
    )''')

    conn.commit()
    conn.close()

def criar_tabela_registros_ponto():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS registros_ponto (
        id INTEGER PRIMARY KEY,
        funcionario_id INTEGER NOT NULL,
        data_hora TEXT NOT NULL,
        tipo TEXT NOT NULL,
        FOREIGN KEY (funcionario_id) REFERENCES funcionarios (id)
    )''')
    conn.commit()
    conn.close()

# Função para executar qualquer query SQL no banco de dados SQLite
def executar_query(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()

# Função para buscar qualquer query SQL no banco de dados SQLite
def buscar_query(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    col_names = [description[0] for description in cursor.description]  # pega o nome das colunas
    rows = cursor.fetchall()
    result = [dict(zip(col_names, row)) for row in rows]  # transforma cada tupla em um dicionário
    return result


def adicionar_tutor(nome, cpf, equipe):
    conn = conectar()
    query = "INSERT INTO tutores (nome, cpf, equipe) VALUES (?, ?, ?)"
    executar_query(conn, query, (nome, cpf, equipe))
    conn.close()

def buscar_tutor_por_cpf(cpf):
    conn = conectar()
    query = "SELECT * FROM tutores WHERE cpf = ?"
    resultado = buscar_query(conn, query, (cpf,))
    conn.close()
    return resultado

def buscar_id_do_funcionario_por_cpf(cpf):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tutores WHERE cpf = ?", (cpf,))
    id = cursor.fetchone()
    conn.close()
    return id[0] if id else None

def buscar_id_nome_cpf_do_funcionario_por_cpf(cpf):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, cpf FROM tutores WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchone()
    conn.close()
    return {'id': resultado[0], 'nome': resultado[1], 'cpf': resultado[2]} if resultado else None




import sqlite3

# Função para estabelecer uma conexão com o banco de dados SQLite
def conectar():
    conn = sqlite3.connect("folha_de_ponto.db")
    return conn

# Função para criar tabelas no banco de dados SQLite a partir de um arquivo SQL
def criar_tabelas(conn):
    with open("create_tables.sql", "r") as f:
        # Executa o conteúdo do arquivo SQL para criar as tabelas
        conn.executescript(f.read())

# Função para executar qualquer query SQL no banco de dados SQLite
def executar_query(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()

# Função para buscar resultados de uma query SQL no banco de dados SQLite
def buscar_query(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    # Retorna todos os registros encontrados
    return cursor.fetchall()

# Função para criar a tabela 'registros_ponto' no banco de dados SQLite se ela não existir
def criar_tabela_registros_ponto():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros_ponto (
            id INTEGER PRIMARY KEY,
            funcionario_id TEXT NOT NULL,
            data_hora TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

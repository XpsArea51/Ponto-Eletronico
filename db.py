import sqlite3

def conectar():
    conn = sqlite3.connect("folha_de_ponto.db")
    return conn

def criar_tabelas(conn):
    with open("create_tables.sql", "r") as f:
        conn.executescript(f.read())

def executar_query(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()

def buscar_query(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()

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

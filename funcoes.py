import db

def registrar_ponto(funcionario_id, cpf, tipo, data_hora):
    conn = db.conectar()
    query = "INSERT INTO registros_ponto (funcionario_id, data_hora, tipo) VALUES (?, ?, ?)"
    db.executar_query(conn, query, (funcionario_id, data_hora, tipo))
    conn.close()

def listar_pontos(funcionario_id=None):
    conn = db.conectar()
    if funcionario_id:
        query = "SELECT * FROM registros_ponto WHERE funcionario_id = ?"
        resultado = db.buscar_query(conn, query, (funcionario_id,))
    else:
        query = "SELECT * FROM registros_ponto"
        resultado = db.buscar_query(conn, query)
    conn.close()
    return resultado

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

def validar_cpf(cpf):
    # Remove pontos, traços e espaços
    cpf = ''.join(c for c in cpf if c.isdigit())

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    return True

def is_valid_cpf(cpf):
   
    return len(cpf) == 11 and cpf.isdigit()

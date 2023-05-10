import funcoes

def menu():
    print("1. Registrar ponto")
    print("2. Listar pontos")
    print("3. Remover ponto")
    print("4. Atualizar ponto")
    print("5. Sair")
    return int(input("Selecione uma opção: "))

def main():
    while True:
        opcao = menu()
        if opcao == 1:
            funcionario_id = int(input("ID do funcionário: "))
            data_hora = input("Data e hora (formato YYYY-MM-DD HH:MM:SS): ")
            tipo = input("Tipo (entrada/saida): ")
            funcoes.registrar_ponto(funcionario_id, data_hora, tipo)
        elif opcao == 2:
            funcionario_id = int(input("ID do funcionário (ou 0 para todos): "))
            if funcionario_id == 0:
                funcionario_id = None
            pontos = funcoes.listar_pontos(funcionario_id)
            for p in pontos:
                print(p)

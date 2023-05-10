Projeto de Sistema de Ponto Eletrônico
Este é um projeto simples de um sistema de ponto eletrônico desenvolvido em Python, utilizando a biblioteca Tkinter para interface gráfica e SQLite como banco de dados.

Funcionalidades
Registro de ponto: O sistema permite que os funcionários registrem seus pontos, informando seu ID e CPF, e selecionando o tipo de ponto (1º Entrada, 1º Saída, 2º Entrada, 2º Saída).

Lista de pontos: É possível visualizar a lista de todos os pontos registrados.

Relógio em tempo real: A interface gráfica exibe um relógio em tempo real, atualizado a cada segundo.

Como executar
Para executar este projeto, você precisará ter Python instalado em sua máquina. Siga os passos abaixo:

Clone este repositório em sua máquina local.
Navegue até a pasta do projeto via terminal.
Execute o comando python main.py (ou python3 main.py, dependendo de sua configuração do Python).
Dependências
Este projeto utiliza as seguintes bibliotecas:

Tkinter para a criação da interface gráfica.
SQLite para a gestão do banco de dados.
pytz para lidar com fusos horários.
Arquivos do projeto
main.py: É o script principal que executa a interface gráfica do sistema de ponto.

db.py: Contém funções para lidar com a conexão ao banco de dados e a execução de consultas SQL.

funcoes.py: Contém as funções que manipulam os dados dos funcionários e seus registros de ponto.

create_tables.sql: Script SQL para criar a tabela de registros de ponto no banco de dados SQLite.

Futuras melhorias
Adicionar uma funcionalidade para editar um registro de ponto.
Implementar um sistema de autenticação para melhorar a segurança.
Adicionar mais informações sobre o funcionário (por exemplo, nome, departamento).
Contribuindo
Sinta-se à vontade para fazer um fork deste repositório e propor suas próprias melhorias via Pull Request.

Licença
Este projeto está licenciado sob a licença MIT.

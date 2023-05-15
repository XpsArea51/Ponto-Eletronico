Ponto Eletrônico - Tutores

Este projeto consiste em um sistema simples de registro de ponto para os tutores. Ele foi desenvolvido em Python utilizado a biblioteca Tkinter para a interface gráfica e SQLite para o banco de dados.
Descrição dos Arquivos
interfac.py
Este é o arquivo principal que executa o programa. Ele contém a interface gráfica do usuário e os comandos que interagem com o banco de dados.
cadastro_tutor.py
Este arquivo possui uma interface gráfica para o cadastro dos tutores. Nele há as funções de verificação dos digitos do CPF, utilizando a lógica de criação desses números. Há também a função que verifica se o CPF já foi cadastrado e impede que ele seja cadastrado novamente.
funcoes.py
Este arquivo contém as funções que são utilizadas para interagir com o banco de dados. As funções incluem registrar ponto, listar pontos, remover ponto, atualizar ponto e validar CPF.
db.py
Este arquivo contém as funções que interagem diretamente com o banco de dados SQLite. As funções incluem conectar ao banco de dados, executar queries, buscar queries e criar tabelas.
create_tables.sql
Este é o script SQL que é usado para criar as tabelas no banco de dados SQLite.
Como Usar

1.	Clone ou baixe este repositório.
2.	Execute o arquivo main.py.
3.	Insira o ID do tutor e CPF no respectivo campo.
4.	Escolha o tipo de ponto que deseja registrar.
5.	Clique no botão "Registrar Ponto" para registrar o ponto.
6.	Clique no botão "Listar Pontos" para visualizar os pontos registrados.

Contribuindo
Contribuições são bem-vindas! Por favor, sinta-se à vontade para corrigir bugs, melhorar as coisas, fornecer documentação. Apenas faça um fork e crie um pull request.
Licença
Este projeto é licenciado sob a Licença MIT.


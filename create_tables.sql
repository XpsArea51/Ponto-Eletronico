-- Cria a tabela 'funcionarios'
CREATE TABLE IF NOT EXISTS funcionarios (
  id INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  cargo TEXT NOT NULL
);

-- Cria a tabela 'registros_ponto'
CREATE TABLE IF NOT EXISTS registros_ponto (
  id INTEGER PRIMARY KEY,
  funcionario_id INTEGER NOT NULL,
  data_hora TEXT NOT NULL,
  tipo TEXT NOT NULL,
  FOREIGN KEY (funcionario_id) REFERENCES funcionarios (id)
);

-- Cria a tabela 'tutores'
CREATE TABLE IF NOT EXISTS tutores (
  id INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  cpf TEXT NOT NULL,
  equipe TEXT NOT NULL
);

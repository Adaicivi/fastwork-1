# Comando para criar a tabela de ordem de serviço (OS)
CREATE_TABLE_OS = """
CREATE TABLE IF NOT EXISTS ordem_servico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empregador INTEGER NOT NULL,
    avaliacao REAL,
    freelancer INTEGER NOT NULL,
    valor REAL NOT NULL,
    FOREIGN KEY (empregador) REFERENCES usuario (id),
    FOREIGN KEY (freelancer) REFERENCES usuario (id)
);
"""

# Comando para exibir todas as ordens de serviço
EXIBIR_OS = """
SELECT * FROM ordem_servico;
"""

# Comando para inserir uma nova ordem de serviço
INSERIR_OS = """
INSERT INTO ordem_servico (empregador, avaliacao, freelancer, valor)
VALUES (?, ?, ?, ?);
"""

# Comando para inserir ou atualizar a avaliação de uma ordem de serviço
INSERIR_AVALIACAO = """
UPDATE ordem_servico
SET avaliacao = ?
WHERE id = ?;
"""
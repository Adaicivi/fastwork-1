import sqlite3
from contextlib import closing
from sql.tarefa_sql import *
from dataclasses import dados


DATABASE_PATH = dados.db


# Função para criar a tabela de tarefas
def criar_tabela_tarefa():
    with sqlite3.connect(DATABASE_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(CREATE_TABLE_TAREFA)
            conn.commit()

# Função para listar tarefas em uma sessão de 20 tarefas (paginação)
def listar_tarefas_paginadas(offset):
    with sqlite3.connect(DATABASE_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(LISTAR_TAREFAS_PAGINADAS, (offset,))
            return cursor.fetchall()

# Função para inserir uma nova tarefa
def inserir_tarefa(descricao, empregador, endereco, valor, data, status):
    with sqlite3.connect(DATABASE_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(
                INSERIR_TAREFA,
                (descricao, empregador, endereco, valor, data, status),
            )
            conn.commit()

# Função para editar uma tarefa para inserir valor e freelancer
def editar_tarefa_valor_freelancer(id_tarefa, valor, freelancer):
    with sqlite3.connect(DATABASE_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(
                EDITAR_TAREFA_VALOR_FREELANCER,
                (valor, freelancer, id_tarefa),
            )
            conn.commit()

# Função para buscar uma tarefa pelo ID
def buscar_tarefa_por_id(id_tarefa):
    with sqlite3.connect(DATABASE_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(BUSCAR_TAREFA_POR_ID, (id_tarefa,))
            return cursor.fetchone()

# Função para listar tarefas por empregador
def listar_tarefas_por_empregador(empregador_id):
    with sqlite3.connect(DATABASE_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(LISTAR_TAREFAS_POR_EMPREGADOR, (empregador_id,))
            return cursor.fetchall()

# Função para listar tarefas por freelancer
def listar_tarefas_por_freelancer(freelancer_id):
    with sqlite3.connect(DATABASE_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(LISTAR_TAREFAS_POR_FREELANCER, (freelancer_id,))
            return cursor.fetchall()
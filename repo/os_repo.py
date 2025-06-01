import sqlite3
from contextlib import closing
from sql.os_sql import *
from dataclasses import dados


DATABASE_PATH = dados.db


# Função para criar a tabela de ordens de serviço (OS)
def criar_tabela_os():
    with sqlite3.connect(DATABASE_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(CREATE_TABLE_OS)
            conn.commit()


# Função para exibir todas as ordens de serviço
def exibir_os():
    with sqlite3.connect(DATABASE_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(EXIBIR_OS)
            return cursor.fetchall()


# Função para inserir uma nova ordem de serviço
def inserir_os(empregador, avaliacao, freelancer, valor):
    with sqlite3.connect(DATABASE_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(
                INSERIR_OS,
                (empregador, avaliacao, freelancer, valor),
            )
            conn.commit()


# Função para inserir ou atualizar a avaliação de uma ordem de serviço
def inserir_avaliacao(id_os, avaliacao):
    with sqlite3.connect(DATABASE_PATH) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(
                INSERIR_AVALIACAO,
                (avaliacao, id_os),
            )
            conn.commit()
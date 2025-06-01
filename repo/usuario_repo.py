import sqlite3
from contextlib import closing
from sql.usuario_sql import *
from data.database import obter_conexao


# Função para criar a tabela de usuários
def criar_tabela_usuario():
    with sqlite3.connect(obter_conexao) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(CREATE_TABLE_USUARIO)
            conn.commit()


# Função para inserir um novo usuário
def inserir_usuario(nome, email, habilidades):
    with sqlite3.connect(obter_conexao) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(BUSCAR_USUARIO_POR_NOME, (nome, email, habilidades))
            conn.commit()


# Função para buscar um usuário pelo nome
def buscar_usuario_por_nome(nome):
    with sqlite3.connect(obter_conexao) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(INSERIR_USUARIO, (nome,))
            return cursor.fetchone()


# Função para listar usuários por habilidades
def listar_usuarios_por_habilidades(habilidade):
    with sqlite3.connect(obter_conexao) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(LISTAR_USUARIOS_POR_HABILIDADES, (f"%{habilidade}%",))
            return cursor.fetchall()


# Função para deletar um usuário pelo ID
def deletar_usuario(id_usuario):
    with sqlite3.connect(obter_conexao) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(DELETAR_USUARIO, (id_usuario,))
            conn.commit()


# Função para editar informações de um usuário
def editar_usuario(id_usuario, nome, email, senha, telefone, data_nascimento, habilidade):
    with sqlite3.connect(obter_conexao) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(EDITAR_USUARIO, (nome, email, senha, telefone, data_nascimento, habilidade, id_usuario))
            conn.commit()


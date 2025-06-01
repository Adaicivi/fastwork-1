from sql.usuario_sql import *
from data.database import obter_conexao
from datetime import datetime
from models.usuario import Usuario


# Função para criar a tabela de usuários
def criar_tabela_usuario():
    """Cria a tabela Usuario se ela não existir."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(CREATE_TABLE_USUARIO)
    conexao.commit()
    conexao.close()

def inserir_usuario(usuario: Usuario) -> Usuario:
    """Insere um novo Usuario no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(INSERIR_USUARIO, 
        (usuario.nome, usuario.cpf, usuario.telefone, usuario.email, usuario.data_nascimento))
    usuario.id = cursor.lastrowid
    conexao.commit()
    conexao.close()
    return Usuario

def editar_Usuario(usuario: Usuario) -> bool:
    """Atualiza um Usuario existente no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(EDITAR_USUARIO, 
        (usuario.nome, usuario.cpf, usuario.telefone, usuario.email, usuario.data_nascimento, usuario.id))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)

def excluir_Usuario(id: int) -> bool:
    """Exclui um Usuario do banco de dados pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(DELETAR_USUARIO, (id,))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)

def obter_Usuario_por_nome(nome: str) -> Usuario:
    """Obtém um Usuario pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(BUSCAR_USUARIO_POR_NOME, (nome,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return Usuario(
            id=resultado[0],
            nome=resultado[1],
            cpf=resultado[2],
            telefone=resultado[3],
            email=resultado[4],
            data_nascimento=datetime.strptime(resultado[5], "%Y-%m-%d").date())
    return None

def obter_usuarios_por_pagina(limite: int, offset: int) -> list[Usuario]:
    """Obtém uma lista de Usuarios com paginação."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(LISTAR_USUARIOS_POR_PAGINA, (limite, offset))
    resultados = cursor.fetchall()
    conexao.close()
    return [Usuario(
        id=resultado[0],
        nome=resultado[1],
        cpf=resultado[2],
        telefone=resultado[3],
        email=resultado[4],
        data_nascimento=datetime.strptime(resultado[5], "%Y-%m-%d").date())
    for resultado in resultados]
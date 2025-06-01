from dataclasses import dataclass

@dataclass

class usuario:
    id: int
    nome: str
    email: str
    senha: str
    telefone: str
    data_nascimento: str
    habilidade: str
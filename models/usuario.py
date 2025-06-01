from pydantic import BaseModel

class usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str
    telefone: str
    data_nascimento: str
    habilidade: str
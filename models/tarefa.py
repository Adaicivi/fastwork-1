from pydantic import BaseModel

class Tarefa(BaseModel):    
        id: int
        descricao: str
        empregador: str
        avaliacao: str
        endereco: str
        valor: float
        data: str
        status: str
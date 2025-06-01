from pydantic import BaseModel
    
class Ordemservico(BaseModel):
    id: int
    empregador: str
    avaliacao: float
    freelancer: str
    valor: float  
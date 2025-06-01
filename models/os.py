from pydantic import BaseModel
    
class OrdemServico(BaseModel):
    id: int
    empregador: str
    avaliacao: float
    freelancer: str
    valor: float  
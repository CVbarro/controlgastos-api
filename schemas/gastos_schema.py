from pydantic import BaseModel, Field
from datetime import date


class GastoCreate(BaseModel):
    descricao: str
    valor: float = Field(gt=0)
    data: date
    categoria_id: int


class GastoResponse(BaseModel):
    id: int
    descricao: str
    valor: float
    data: date
    categoria_id: int
    nome_categoria: str
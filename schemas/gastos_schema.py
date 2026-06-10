from pydantic import BaseModel, Field


class GastoCreate(BaseModel):
    descricao: str
    valor: float = Field(gt=0)
    data: str
    categoria_id: int


class GastoResponse(BaseModel):
    id: int
    descricao: str
    valor: float
    data: str
    categoria_id: int
    nome_categoria: str
from pydantic import BaseModel, Field, field_validator
from datetime import date


class GastoCreate(BaseModel):
    descricao: str
    valor: float = Field(gt=0)
    data: date
    categoria_id: int

    @field_validator("data")
    @classmethod
    def validar_data_nao_futura(cls, valor: date) -> date:
        if valor > date.today():
            raise ValueError("A data do gasto não pode ser futura.")
        return valor


class GastoResponse(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    descricao: str
    valor: float
    data: date
    categoria_id: int
    nome_categoria: str

class ResumoCategoriaResponse(BaseModel):
    nome_categoria: str
    total: float
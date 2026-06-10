from pydantic import BaseModel


class CategoriaCreate(BaseModel):
    nome: str


class CategoriaResponse(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    nome: str
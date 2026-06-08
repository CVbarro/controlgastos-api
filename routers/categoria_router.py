from fastapi import APIRouter
from core.dependencies import database
from repositories.categoria_repository import (CategoriaRepository)
from services.categoria_service import (CategoriaService)
from schemas.categoria_schema import (CategoriaCreate)

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)

categoria_repository = CategoriaRepository(database)

categoria_service = CategoriaService(categoria_repository)


@router.post("/")
def cadastrar_categoria(
    categoria: CategoriaCreate
):
    return categoria_service.cadastrar(
        categoria.nome
    )


@router.get("/")
def listar_categorias():
    return categoria_service.listar()

@router.get("/id/{id}")
def buscar_categoria_id(
    categoria_id: int
):
    return categoria_service.buscar_id(categoria_id)

@router.get("/nome/{nome}")
def buscar_categoria_nome(
    nome: str
):
    return categoria_service.buscar_nome(nome)
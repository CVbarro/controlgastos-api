from fastapi import APIRouter, Depends, HTTPException
from core.dependencies import database
from repositories.categoria_repository import CategoriaRepository
from services.categoria_service import CategoriaService
from schemas.categoria_schema import CategoriaCreate, CategoriaResponse  # ← adicionado

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)


def get_service() -> CategoriaService:
    return CategoriaService(CategoriaRepository(database))


@router.post("/", response_model=CategoriaResponse, status_code=201)
def cadastrar_categoria(
    categoria: CategoriaCreate,
    service: CategoriaService = Depends(get_service)
):
    categoria_id = service.cadastrar(categoria.nome) 
    return service.buscar_id(categoria_id)           


@router.get("/", response_model=list[CategoriaResponse])
def listar_categorias(
    service: CategoriaService = Depends(get_service) 
):
    return service.listar()  


@router.get("/nome/{nome}", response_model=CategoriaResponse)
def buscar_categoria_nome(
    nome: str,
    service: CategoriaService = Depends(get_service)  
):
    categoria = service.buscar_nome(nome)  
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria


@router.get("/id/{categoria_id}", response_model=CategoriaResponse)
def buscar_categoria_id(
    categoria_id: int,
    service: CategoriaService = Depends(get_service)  
):
    categoria = service.buscar_id(categoria_id) 
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria
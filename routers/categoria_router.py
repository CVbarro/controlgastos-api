from fastapi import APIRouter, Depends, HTTPException
from core.dependencies import database
from repositories import CategoriaRepository, GastosRepository
from services import CategoriaService
from schemas import CategoriaCreate, CategoriaResponse

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)


def get_service() -> CategoriaService:
    categoria_repository = CategoriaRepository(database)
    gastos_repository = GastosRepository(database)
    return CategoriaService(categoria_repository, gastos_repository)

@router.post("/", response_model=CategoriaResponse, status_code=201)
def cadastrar_categoria(
    categoria: CategoriaCreate,
    service: CategoriaService = Depends(get_service)
):
    try:
        categoria_id = service.cadastrar(categoria.nome)
        return service.buscar_id(categoria_id)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e)) 


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

@router.delete("/{nome}", status_code=200)
def remover_categoria_por_nome(
    nome: str,
    service: CategoriaService = Depends(get_service)
):

    try:
        service.remover(nome)

        return {
             "mensagem": "Categoria removida com sucesso."
        }
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail= str(e))
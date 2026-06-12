from fastapi import APIRouter, Depends, HTTPException
from core.dependencies import database
from repositories import GastosRepository, CategoriaRepository
from services import GastoService
from schemas import GastoCreate, GastoResponse

router = APIRouter(
    prefix="/gastos",
    tags=["Gastos"]
)


def get_service() -> GastoService:

    gasto_repository = GastosRepository(database)

    categoria_repository = CategoriaRepository(database)

    return GastoService(
        gasto_repository,
        categoria_repository
    )

@router.post("/", response_model=GastoResponse, status_code=201)
def cadastrar_gasto(
    gasto: GastoCreate,
    service: GastoService = Depends(get_service)
    ):
    try:
        gasto_id = service.cadastrar(gasto.descricao, gasto.valor, gasto.data, gasto.categoria_id)
        return service.buscar_gasto_id(gasto_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[GastoResponse])
def listar_gastos(
    service: GastoService = Depends(get_service)
    ):
    return service.listar_gastos()

@router.get("/id/{gasto_id}", response_model=GastoResponse)
def listar_gasto_por_id(
    gasto_id: int, service: GastoService = Depends(get_service)
    ):
    gasto = service.buscar_gasto_id(gasto_id)

    if not gasto:
        raise HTTPException(status_code=404, detail="Gasto não encontrado.")
    return gasto

@router.get("/categoria/{nome_categoria}", response_model=list[GastoResponse])
def listar_gastos_por_categoria(
    nome_categoria: str, service: GastoService = Depends(get_service)
    ):
    try:
        return service.buscar_gastos_categoria(nome_categoria)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.put("/{gasto_id}", response_model=GastoResponse)
def atualizar_gasto(
    gasto_id: int,
    gasto: GastoCreate,
    service: GastoService = Depends(get_service)
):
    try:
        return service.atualizar(gasto_id, gasto.descricao, gasto.valor, gasto.data, gasto.categoria_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{gasto_id}", status_code=200)
def remover_gasto(
    gasto_id: int, service: GastoService = Depends(get_service)
    ):
    
    try:
        service.remover(gasto_id)

        return {
            "mensagem": "Gasto removido com sucesso."
        }
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail= str(e))
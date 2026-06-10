from repositories import GastosRepository, CategoriaRepository
from models import Gastos
from datetime import date



class GastoService:

    def __init__(self, repository: GastosRepository, categoria_repository: CategoriaRepository) -> None:
        self.repository = repository
        self.categoria_repository = categoria_repository

    
    def cadastrar(self, descricao: str, valor: float, data: date, categoria_id: int) -> int:
        categoria = (self.categoria_repository.buscar_por_id(categoria_id))

        if not categoria:
            raise ValueError("Categoria não encontrada.")
        
        return self.repository.cadastrar_gasto(
            descricao,
            valor,
            data,
            categoria_id
        )
    
    def buscar_gasto_id(self, gasto_id: int) -> Gastos | None:
        return self.repository.buscar_gasto_id(gasto_id)
    
    def listar_gastos(self) -> list[Gastos]:
        return self.repository.listar_todos_gastos()
    
    def remover(self, gasto_id: int):
        removido = self.repository.remover_gasto(gasto_id)

        if not removido:
            raise ValueError("Gasto não encontrado.")
        return True
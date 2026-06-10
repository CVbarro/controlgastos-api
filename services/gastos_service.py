from repositories.gastos_repository import GastosRepository
from repositories.categoria_repository import CategoriaRepository


class GastoService:

    def __init__(self, repository: GastosRepository, categoria_repository: CategoriaRepository) -> None:
        self.repository = repository
        self.categoria_repository = categoria_repository

    
    def cadastrar(self, descricao: str, valor: float, data: str, categoria_id: int):
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria_id = categoria_id

        categoria = (self.categoria_repository.buscar_por_id(categoria_id))

        if not categoria:
            raise ValueError("Categoria não encontrada.")
        
        return self.repository.cadastrar_gasto(
            descricao,
            valor,
            data,
            categoria_id
        )
    
    def buscar_gasto_id(self, gasto_id: int):
        return self.repository.buscar_gasto_id(gasto_id)
    
    def listar_gastos(self):
        return self.repository.listar_todos_gastos()
    
    def remover(self, gasto_id: int):
        removido = self.repository.remover_gasto(gasto_id)

        if not removido:
            raise ValueError("Gasto não encontrado.")
        return True
from repositories import CategoriaRepository, GastosRepository
from models import Categoria

class CategoriaService:
    def __init__(self, repository: CategoriaRepository, gastos_repository: GastosRepository) -> None:
        self.repository = repository
        self.gastos_repository = gastos_repository

    
    def cadastrar(self, nome: str) -> int:
        existente = (self.repository.buscar_por_nome(nome.strip()))

        if existente:
            raise ValueError("Categoria já existe.")

        return self.repository.cadastrar_categoria(nome.strip())
        

    def listar(self) -> list[Categoria]:
        return self.repository.listar_todas()
    

    def buscar_nome(self, nome: str) -> Categoria | None:
        return self.repository.buscar_por_nome(nome)
    
    def buscar_id(self, categoria_id: int) -> Categoria | None:
        return self.repository.buscar_por_id(categoria_id)
    
    
    def remover(self, nome: str) -> bool:
        categoria = self.repository.buscar_por_nome(nome)

        if not categoria:
            raise ValueError("Categoria não encontrada")

        self.gastos_repository.remover_gastos_por_categoria(categoria.id)

        removido = self.repository.remover_categoria(nome)

        return removido
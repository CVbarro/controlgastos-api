from repositories import CategoriaRepository
from models import Categoria

class CategoriaService:
    def __init__(self, repository: CategoriaRepository) -> None:
        self.repository = repository

    
    def cadastrar(self, nome: str) -> int:
        return self.repository.cadastrar_categoria(nome)
        

    def listar(self) -> list[Categoria]:
        return self.repository.listar_todas()
    

    def buscar_nome(self, nome: str) -> Categoria | None:
        return self.repository.buscar_por_nome(nome)
    
    def buscar_id(self, categoria_id: int) -> Categoria | None:
        return self.repository.buscar_por_id(categoria_id)
    
    def remover(self, nome: str) -> bool:
        removido = self.repository.remover_categoria(nome)

        if not removido:
            raise ValueError("Categoria não encontrada")
        return True
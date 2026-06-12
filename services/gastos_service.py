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
    
    def buscar_gastos_categoria(self, nome_categoria: str) -> list[Gastos]:
        categoria = (self.categoria_repository.buscar_por_nome(nome_categoria))

        if not categoria:
            raise ValueError("Categoria não encontrada.")
        return self.repository.buscar_gastos_categoria(nome_categoria)
    
    def listar_gastos(self) -> list[Gastos]:
        return self.repository.listar_todos_gastos()
    
    def atualizar(self, gasto_id: int, descricao: str, valor: float, data: date, categoria_id: int) -> Gastos:
        categoria = self.categoria_repository.buscar_por_id(categoria_id)

        if not categoria:
            raise ValueError("Categoria não encontrada.")

        atualizado = self.repository.atualizar_gasto(gasto_id, descricao, valor, data, categoria_id)

        if not atualizado:
            raise ValueError("Gasto não encontrado.")

        gasto = self.repository.buscar_gasto_id(gasto_id)

        if gasto is None:
            raise RuntimeError("Erro inesperado ao buscar gasto atualizado.")

        return gasto
    
    def remover(self, gasto_id: int):
        removido = self.repository.remover_gasto(gasto_id)

        if not removido:
            raise ValueError("Gasto não encontrado.")
        return True
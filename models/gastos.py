class Gastos:

    def __init__(self, id: int, descricao: str, valor: float, data: str, categoria_id: int, nome_categoria: str) -> None:
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria_id = categoria_id
        self.nome_categoria = nome_categoria
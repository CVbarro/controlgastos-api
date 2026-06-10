from core.database import Database
from models.gastos import Gastos
from datetime import date

class GastosRepository:

    def __init__(self, database: Database) -> None:
        self.database = database

    def cadastrar_gasto(self, descricao: str, valor: float, data: date, categoria_id: int) -> int:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
        """
        INSERT INTO gastos (
            descricao,
            valor,
            data,
            categoria_id
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            descricao,
            valor,
            data,
            categoria_id
        )
    )

        conn.commit()

        if cursor.lastrowid is None:
            raise RuntimeError(
            "Não foi possível obter o ID do gasto criada."
            )
        
        return cursor.lastrowid
    

    def buscar_gasto_id(self, gasto_id: int) -> Gastos | None:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT gastos.*, categorias.nome AS nome_categoria
        FROM gastos
        JOIN categorias ON gastos.categoria_id = categorias.id
        WHERE gastos.id = ?
        """, (gasto_id,))

        row = cursor.fetchone()

        return Gastos(
            id=row["id"],
            descricao=row["descricao"],
            valor=row["valor"],
            data=row["data"],
            categoria_id=row["categoria_id"],
            nome_categoria=row["nome_categoria"]
        ) if row else None
    
    def listar_todos_gastos(self) -> list[Gastos]:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT gastos.*, categorias.nome AS nome_categoria
        FROM gastos
        JOIN categorias ON gastos.categoria_id = categorias.id
        """)

        return [
            Gastos(
                id=row["id"],
                descricao=row["descricao"],
                valor=row["valor"],
                data=row["data"],
                categoria_id=row["categoria_id"],
                nome_categoria=row["nome_categoria"]
            )
            for row in cursor.fetchall()
        ]
    
    def remover_gasto(self, gasto_id: int) -> bool:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
        "DELETE FROM gastos WHERE id = ?",
        (gasto_id,)
        )

        conn.commit()

        return cursor.rowcount > 0


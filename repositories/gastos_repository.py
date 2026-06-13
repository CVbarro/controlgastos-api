from core.database import Database
from models import Gastos
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
            "Não foi possível obter o ID do gasto criado."
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
    
    def buscar_gastos_categoria(self, nome_categoria: str) -> list[Gastos]:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT gastos.*, categorias.nome AS nome_categoria
        FROM gastos
        JOIN categorias ON gastos.categoria_id = categorias.id
        WHERE categorias.nome = ?
        """, (nome_categoria,))


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

    
    def atualizar_gasto(self, gasto_id: int, descricao: str, valor: float, data: date, categoria_id: int) -> bool:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE gastos
            SET descricao = ?, valor = ?, data = ?, categoria_id = ?
            WHERE id = ?
            """,
            (descricao, valor, data, categoria_id, gasto_id)
        )

        conn.commit()

        return cursor.rowcount > 0

    def remover_gasto(self, gasto_id: int) -> bool:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
        "DELETE FROM gastos WHERE id = ?",
        (gasto_id,)
        )

        conn.commit()

        return cursor.rowcount > 0
    
    def remover_gastos_por_categoria(self, categoria_id: int) -> int:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM gastos WHERE categoria_id = ?",
            (categoria_id,)
        )

        conn.commit()

        return cursor.rowcount  

    def resumo_por_categoria(self) -> list[dict]:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT categorias.nome AS nome_categoria, SUM(gastos.valor) AS total
            FROM gastos
            JOIN categorias ON gastos.categoria_id = categorias.id
            GROUP BY categorias.id, categorias.nome
        """)

        return [
            {"nome_categoria": row["nome_categoria"], "total": row["total"]}
            for row in cursor.fetchall()
        ]

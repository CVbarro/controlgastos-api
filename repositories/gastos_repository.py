from core.database import Database

class GastosRepository:

    def __init__(self, database: Database) -> None:
        self.database = database

    def cadastrar_gasto(self, descricao: str, valor: float, data: str, categoria_id: int) -> int:
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
    

    def buscar_gasto_id(self, gasto_id: int) -> dict | None:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM gastos WHERE id = ?",
            (gasto_id,)
        )

        row = cursor.fetchone()

        return dict(row) if row else None
    
    def listar_todos_gastos(self) -> list[dict]:
        conn = self.database.get_connection()

        cursor = conn. cursor()

        cursor.execute(
            "SELECT * FROM gastos"
        )

        return [
            dict(row)
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


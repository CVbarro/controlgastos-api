from core.database import Database


class CategoriaRepository:

    def __init__(self, database: Database) -> None:
        self.database = database


    def cadastrar_categoria(self, nome: str) -> int:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO categorias (nome) VALUES (?)",
            (nome,)
        )

        conn.commit()

        if cursor.lastrowid is None:
            raise RuntimeError(
            "Não foi possível obter o ID da categoria criada."
            )

        return cursor.lastrowid


    def buscar_por_nome(self, nome: str) -> dict | None:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM categorias WHERE nome = ?",
            (nome,)
        )

        row = cursor.fetchone()

        return dict(row) if row else None
    

    def buscar_por_id(self, categoria_id: int) -> dict | None:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM categorias WHERE id = ?",
            (categoria_id,)
        )

        row = cursor.fetchone()

        return dict(row) if row else None
    

    def listar_todas(self) -> list[dict]:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM categorias"
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]
    
    def remover_categoria(self, nome: str) -> bool:
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM categoria WHERE nome = ?",
            (nome,)
        )

        conn.commit()

        return cursor.rowcount > 0

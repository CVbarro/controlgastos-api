from core.database import Database


class CategoriaRepository:

    def __init__(self,database: Database) -> None:
        self.database = database


    def cadastrar_categoria(self, nome: str):
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO categorias (nome) VALUES (?)",
            (nome,)
        )

        conn.commit()

        return cursor.lastrowid



    def buscar_por_nome(self,nome: str):
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM categorias WHERE nome = ?",
            (nome,)
        )

        row = cursor.fetchone()

        return dict(row) if row else None
    

    def buscar_por_id(self, id: int):
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM categorias WHERE id = ?",
            (id,)
        )

        row = cursor.fetchone()

        return dict(row) if row else None
    

    def listar_todas(self):
        conn = self.database.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM categorias"
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]
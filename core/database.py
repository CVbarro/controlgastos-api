import sqlite3


class Database:
    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(
            db_path,
            check_same_thread=False
        )
        self.connection.row_factory = sqlite3.Row

    def criar_tabelas(self):
        cursor = self.connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            data TEXT NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (categoria_id)
                REFERENCES categorias(id)
        )
        """)

        self.connection.commit()

    def get_connection(self):
        return self.connection

    def fechar(self):
        self.connection.close()
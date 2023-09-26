import sqlite3

class SQLite:
    def __init__(self, database) -> None:
        self.conexion = sqlite3.connect(database)
        self.cursor = self.conexion.cursor()

    def insert_data(self, tabla, **campo_dato):
        campos = ", ".join(list(campo_dato.keys()))
        datos = "'" + "', '".join(list(campo_dato.values())) + "'"
        query = f"INSERT INTO {tabla}({campos}) VALUES ({datos})"
        self.cursor.execute(query)
        self.conexion.commit()

    def select_data(self, tabla):
        query = f"SELECT * FROM {tabla}"
        resultado = self.cursor.execute(query)
        return resultado.fetchall()
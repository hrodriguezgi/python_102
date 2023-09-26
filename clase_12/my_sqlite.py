import sqlite3

conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

# Insertar datos
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Juan', 30))

# Consultar datos
cursor.execute("SELECT * FROM usuarios")
filas = cursor.fetchall()
for fila in filas:
    print(fila)

conexion.commit()
conexion.close()

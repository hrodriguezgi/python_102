import sqlite3

conexion = sqlite3.connect('mi_bbdd.db')

# Ejemplo de la biblioteca:
# Donde almacenar los libros
# Donde almacenar los usuarios

# Query para crear una tabla
crear_tabla_libros = """CREATE TABLE IF NOT EXISTS libros(
     id INTEGER PRIMARY KEY
    ,titulo TEXT
    ,autor TEXT
    ,fecha_publicacion TEXT
)"""

crear_tabla_usuarios = """
CREATE TABLE IF NOT EXISTS usuarios
(
     documento INTEGER PRIMARY KEY
    ,nombre TEXT
    ,fecha_registro TEXT
)
"""

# Variable es para ejecutar queries en la bbdd
cursor = conexion.cursor()

# Ejecución de los queries de creación de tablas
cursor.execute(crear_tabla_libros)
cursor.execute(crear_tabla_usuarios)

# Inserción de registros
libro1 = """
INSERT INTO libros
(titulo, autor, fecha_publicacion)
VALUES
('Cien años de soledad', 'Gabriel Garcia Marquez', '1989-12-01')
"""

#cursor.execute(libro1)
#conexion.commit()

libro2 = """
INSERT INTO libros
(titulo, autor, fecha_publicacion)
VALUES
('Hábitos atómicos', 'Pedro Perez', '2019-01-14')
"""

#cursor.execute(libro2)
#conexion.commit()

usuario1 = """
INSERT INTO usuarios
(documento, nombre, fecha_registro)
VALUES
('12345', 'Harvey Rodriguez', '2023-09-26')
"""

#cursor.execute(usuario1)
#conexion.commit()

# Cosultar los libros que tengo registrados:
consulta_libros = """SELECT * FROM libros"""
resultado = cursor.execute(consulta_libros)
print(resultado.fetchall()) # read()

consulta_usuarios = """SELECT * FROM usuarios"""
for registro in cursor.execute(consulta_usuarios):
    print(registro[1]) # readlines()
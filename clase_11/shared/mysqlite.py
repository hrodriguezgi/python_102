import sqlite3

class MySqlite:
    def __init__(self, database) -> None:
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def create(self, table_name, **colum_value):
        str_columns = ", ".join(list(colum_value.keys()))
        str_values = "', '".join(map(lambda x: str(x), list(colum_value.values())))
        query = f"insert into {table_name}({str_columns}) values ('{str_values}')"
        self.conn.execute(query)
        self.conn.commit()
        print('Datos ingresados correctamente')


    def read(self, table_name, **kwargs):
        list_params = list(kwargs.items())
        params = ' and '.join([ f"{param[0]} = '{param[1]}'" for param in list_params ])
        query = f"select * from {table_name} where {params}"
        return self.cursor.execute(query)


    def update(self):
        pass

    def delete(self):
        pass
    
    

sql = MySqlite('../python_102.db')
# create
# Estudiantes
#sql.create('estudiantes', nombre='Carlos', apellido='Castro', identificacion='12345')
# Materias
#sql.create('materias', nombre='Español')
# Notas
#sql.create('notas', id_estudiante=1, id_materia=1)

# read
#res = sql.read('estudiantes', identificacion='12345')
#for r in res:
#    print(r)
#res = sql.read('materias', nombre='Español')
#for r in res:
#    print(r)

"""
C -> conexion.execute("insert into estudiantes(nombre, apellido) values ('Carlos', 'Castro')"), conexion.commit()
R -> resultado = conexion.execute('select * from estudiantes')
U -> conexion.execute("update estudiantes set apellido = 'Lopez', nombre = 'Pedro' where identificacion = 1"), conexion.commit()
D -> conexion.execute("delete from estudiantes where id = 2"), conexion.commit()
"""
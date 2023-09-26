from shared.mi_sqlite import SQLite

conexion = SQLite('mi_bbdd.db')

print(conexion.select_data('usuarios'))


conexion.insert_data('usuarios', 
                     documento='23456', 
                     nombre='Carlos Aguirre', 
                     fecha_registro='2023-09-26')


print(conexion.select_data('usuarios'))
"""
Gestor de notas.
1. Menú de inicio: crear, leer (CRUD)
2. Nuestra "BBDD" será una bbdd sqlite
3. Crear: existe una tabla llamada estudiantes, materias y notas. Crear será
   insertar un registro en alguna de las tablas.
4. Leer: acceder a la información del usuario para presentarla
5. Opción de salir
"""

from shared.mysqlite import MySqlite

mysqlite = MySqlite('python_102.db')

while True:
   print("""
   Bienvenidos al sistema de gestión

   Qué desea realizar:
   1. Insertar un estudiante
   2. Crear una materia
   3. Insertar una nota
   4. Consultar la información de un estudiante
   5. Salir
   """)

   opcion = input("Seleccione un valor: ")

   if opcion == '1':
      i_nombre = input('Ingrese el nombre:')
      i_apellido = input('Ingrese el apellido:')
      i_identificacion = input('Digite la identificacion:')
      mysqlite.create('estudiantes', nombre=i_nombre, apellido=i_apellido, identificacion=i_identificacion)
   elif opcion == '2':
      i_nombre = input('Ingrese el nombre de la materia:')
      mysqlite.create('materias', nombre=i_nombre)
   elif opcion == '3':
      i_identificacion = input('Digite la identificacion del estudiante:')
      # estudiante existe?
      estudiante = mysqlite.read('estudiantes', identificacion=i_identificacion).fetchall()
      print(estudiante)
      if estudiante:
         i_nombre = input('Digite el nombre de la materia:')
         # materia existe?
         materia = mysqlite.read('materias', nombre=i_nombre).fetchall()
         print(materia)
         if materia:
            i_nota = input('Digite la nota:')
            mysqlite.create('notas', id_estudiante=estudiante[0][0], id_materia=materia[0][0], nota=i_nota)
         else:
            print('materia no valida')
      else:
         print('estudiante no valido')
   elif opcion == '4':
      i_identificacion = input('Digite la identificacion del estudiante:')
      estudiante = mysqlite.read('estudiantes', identificacion=i_identificacion).fetchall()
      print(f'El nombre completo del estudiante es: {estudiante[0][1]} {estudiante[0][2]}')
      print(f'La identificación es: {estudiante[0][3]}')
      # :TODO:
      # Presentar la información de las notas de cada materia
   elif opcion == '5':
      break



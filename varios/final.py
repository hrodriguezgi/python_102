"""
Gestor de notas.
1. Menú de inicio: crear, actualizar, leer, borrar (CRUD)
2. Nuestra "BBDD" será una bbdd sqlite
3. Crear: cada estudiante tiene su propio archivo json
4. Actualizar: agregar notas a las materias de mat, esp, cie
5. Leer: leer el registro del estudiante (leer el archivo json)
6. Borrar: eliminar el registro del estudiante (eliminar el archivo json)
7. Opción de salir
"""

import os
import json


class Estudiante:
    materias = {'mat': [], 'esp': [], 'cie': []}

    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.filename = self.cedula + '.json'

    def crear(self):
        with open(self.filename, 'w') as f:
            json.dump(self.materias, f)
        return 'Alumno creado'

    def actualizar(self, **kwargs):
        notas = self.__leer_datos()

        for materia, nota in kwargs.items():
            notas_actuales = notas.get(materia)
            notas_actuales.append(nota)
            notas[materia] = notas_actuales

        with open(self.filename, 'w') as f:
            json.dump(notas, f)
        return 'Notas actualizadas'

    def leer(self):
        notas = self.__leer_datos()
        print(json.dumps(notas, indent=4))

    def borrar(self):
        os.remove(self.filename)

    def __leer_datos(self):
        with open(self.filename, 'r') as f:
            notas = json.load(f)
        return notas


def menu():
    print("-"*100)
    print('\tGestión de Usuarios')
    choice = input("""1. Crear nuevo estudiante\n2. Leer información de estudiante\n3. Adicionar una nota\n4. Eliminar estudiante\n5. Salir\n""")
    print("-"*100)
    if choice in ("1","2","3","4","5"):
        return choice
    else:
        print("Opcion invalida")
        return "5"

def main():
    condicion = True

    while condicion:
        choice = menu()
        if choice == '5':
            condicion = False
        elif choice == '1':
            name = input('Digite el nombre: ')
            surname = input('Digite el apellido: ')
            document = input('Digite el documento: ')
            #student = Students(name, surname, document)
            #student.create_new_student()
        elif choice == '2':
            document = input('Digite el documento: ')
            #student = Students().search_student(document)
            #print(json.dumps(student, indent=4))
        elif choice == '3':
            pass
        elif choice == '4':
            pass


if __name__ == '__main__':
    main()
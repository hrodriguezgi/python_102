# Serialización
import pickle

# contamos con un diccionario con datos almacenados en él
informacion = {
    'id': 1,
    'nombres': 'Harvey',
    'apellidos': 'Rodriguez',
    'telefono': 12345678,
    'ciudad': 'Envigado'
}

# almacenarmos la información en un fichero binario:
with open('info_serial.pickle', 'wb') as f:
    pickle.dump(informacion, f)



## De serialización
# import pickle

# abrir el archivo de modo lecura y almacenamos el contenido en una variable
with open('info_serial.pickle', 'rb') as f:
    nueva_informacion = pickle.load(f)

print(nueva_informacion)

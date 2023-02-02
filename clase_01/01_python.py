# Recuento de python 101
import this

print(f'''
Python como lenguaje
--------------------
Python es de tipado dinámico, y esto significa que las variables no requeiren
ser declaradas del tipo al que pertenecen al momento de su creación ya que
Python lo identificará. También nos permite cambiar el tipo de una variable 
cuando hacemos una asignación. Ejemplo:\n''')

# Creamos una variable con el valor de 10
var = 10
print(f'var:\t{var}\ntype(var):\t{type(var)}\n')

# Ahora modificamos la variable y le asignamos el valor 'diez'
var = 'diez'
print(f'var:\t{var}\ntype(var):\t{type(var)}')

print(f'''
Como se pudo ver en el ejemplo, Python no requiere que sea definido un tipo de
variable al momento crear una, y nos permite poder asignar cualquier valor y 
esto afectará el tipo de ella.

Sin embargo, Python cuenta con tres forma de crear una variable:
1. Dinámico -> variable = 10
2. Referencia -> variable:int = 10
3. Constructor -> variable = int('10')

La más utilizada es la definición dinámica, sin embargo vamos a ver que en
algunas funciones, encontraremos que los parámetros o argumentos son declarados
por medio de referencia, con el fin de transmitir al lector del código el tipo
correcto de dato que debe enviar al utilizar la función. El último método es
utilizado para hacer casteos (conversión de datos entre tipos)''')

print(f'''
Comentarios
-----------
Los comentarios en Python se realizan con el símbolo # al principio de cada
linea. Si queremos hacer un comentario multilinea, podemos utilizar """ (triple
comilla doble o sencilla) al inicio y otra al final.''')
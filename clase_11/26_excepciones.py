# Pedir al usuario que ingrese un número
try:
    num = int(input("Ingrese un número: "))
    resultado = 10 / num
    print(f"El resultado de la operación es: {resultado}")

# Manejar una excepción si ocurre un error al convertir a entero
except ValueError:
    print("Error: el valor a ingresar debe ser numérico")

# Manejar una excepción si ocurre un error al dividir entre cero
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")

# Manejar una excepción genérica en caso de cualquier otro error
except Exception as e:
    print(f"Error inesperado: {e}")

# Este bloque se ejecutará siempre, sin importar si se produce una excepción o no
finally:
    print("Fin del programa")



# Pedir al usuario que ingrese un número
try:
    num = int(input("Por favor, ingrese un número entero: "))
    resultado = 10 / num

# Manejar una excepción si ocurre un error al convertir a entero
except ValueError:
    print("Error: el valor a ingresar debe ser numérico")

# Manejar una excepción si ocurre un error al dividir entre cero
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")

# Este bloque se ejecuta si no se producen excepciones en el bloque try
else:
    print(f"El resultado de la operación es: {resultado}")

# Este bloque se ejecutará siempre, sin importar si se produce una excepción o no
finally:
    print("¡Programa terminado!")
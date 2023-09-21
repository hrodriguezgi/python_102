# Excepciones

Las excepciones son eventos inesperados o errores que pueden ocurrir durante la ejecución de un programa.
Cuando ocurre una excepción, el flujo normal de ejecución del programa se detiene y se busca un bloque
`except` correspondiente para manejar la excepción de manera adecuada en lugar de que el programa se bloquee
por completo.


Algunas de las razones por las cuales utilizar `try` y `except` son:
1. **Manejo de errores:** este es el principal propósito, ya que permite controlar los errores de una manera
elegante y controlada
2. **Mensajes de error significativos:** con ayuda de estos comandos, se puede proporcionar mensajes de error
significativos al usuario en lugar de que aparezca un mensaje de error genérico.
3. **Prevención de fallas inesperadas:** se puede anticipar y manejar situaciones excepcionales o inesperadas
que puedan surgir durante la ejecución del programa.
4. **Recuperación y limpieza:** también puede ser utilizado para realizar acciones de recuperación o limpieza
después de que ocurra una excepción.
5. **Robustez de código:** el manejo de excepciones contribuye a que el código sea más robusto y resistente
a errores


Ejemplos:
```python
try:
    num = int(input("Ingrese un número: "))
    resultado = 10 / num
    print(f"El resultado de la operación es: {resultado}")
except ValueError:
    print("Error: el valor a ingresar debe ser numérico")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    print("Fin del programa")
```
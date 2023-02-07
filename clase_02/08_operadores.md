# Operadores

## Operadores Aritméticos
Un operador aritmético toma dos operandos como entrada, realiza un cálculo y devuelve el resultado.

Considera la expresión, `a = 2 + 3`. Aquí, `2` y `3` son los operandos y `+` es el operador aritmético. El resultado de la operación se almacena en la variable `a`

| **Operador** | **Descripción** | **Ejemplo** |
|--------------|-----------------|-------------|
| `+` | Realiza Adición entre los operandos | 2 + 3 = 5
| `-` | Realiza Substracción entre los operandos | 5 - 3 = 2
| `*` | Realiza Multiplicación entre los operandos | 4 * 3 = 12
| `/` | Realiza División entre los operandos | 12 / 3 = 4
| `%` | Realiza un módulo entre los operandos | 16 % 3 = 1
| `**` | Realiza la potencia de los operandos | 3 ** 3 = 27
| `//` | Realiza la división con resultado de número entero | 18 // 5 = 3


## Operadores Relacionales
Un operador relacional se emplea para comparar y establecer la relación entre ellos. 

Devuelve un valor booleano (true o false) basado en la condición.

| **Operador** | **Descripción** | **Ejemplo** |
|--------------|-----------------|-------------|
| `>` | Devuelve `True` si el operador de la izquierda es mayor que el operador de la derecha | 12 > 3 devuelve True
| `<` | Devuelve `True` si el operador de la derecha es mayor que el operador de la izquierda | 12 < 3 devuelve False
| `==` | Devuelve `True` si ambos operandos son iguales | 12 == 3 devuelve False
| `>=` | Devuelve `True` si el operador de la izquierda es mayor o igual que el operador de la derecha | 12 >= 3 devuelve True
| `<=` | Devuelve `True` si el operador de la derecha es mayor o igual que el operador de la izquierda | 12 <= 3 devuelve False
| `!=` | Devuelve `True` si ambos operandos no son iguales | 12 != 3 devuelve True


## Operadores Bit a Bit
Un operador bit a bit realiza operaciones en los operandos bit a bit.

Consideremos a = 2 (en binario = 10) y b = 3 (en binario = 11) para los siguientes casos.

| **Operador** | **Descripción** | **Ejemplo** |
|--------------|-----------------|-------------|
| `&` | Realiza bit a bit la operación AND en los operandos | `a & b = 2` (Binario: 10 & 11 = 10)
| `\|` | Realiza bit a bit la operación OR en los operandos | `a \| b = 3` (Binario: 10 \| 11 = 11)
| `^` | Realiza bit a bit la operación XOR en los operandos | `a ^ b = 1` (Binario: 10 ^ 11 = 01)
| `~` | Realiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando | `~a = -3` (Binario: ~(00000010) = (11111101))
| `>>` | Realiza un desplazamiento a la derecha bit a bit. Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha | `a >> b = 0` (Binario: 00000010 >> 00000011 = 0)
| `<<` | Realiza un desplazamiento a la izquierda bit a bit. Desplaza los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha | `a << b = 16` (Binario: 00000010 << 00000011 = 00001000)


## Operadores de Asignación
Se utiliza un operador de asignación para asignar valores a una variable. Esto generalmente se combina con otros operadores (como aritmética, bit a bit) donde la operación se realiza en los operandos y el resultado se asigna al operando izquierdo.

Considera los siguientes ejemplos,

`a = 18`. Aquí `=` es un operador de asignación, y el resultado se almacena en la variable `a`.

`a += 10`. Aquí `+=` es un operador de asignación, y el resultado se almacena en la variable `a`. Es lo mismo que `a = a + 10`.

| **Operador** | **Descripción** |
|--------------|-----------------|
| `=` | `a = 5` El valor `5` es asignado a la variable `a`
| `+=` | `a += 5` es equivalente a `a = a + 5`
| `-=` | `a -= 5` es equivalente a `a = a - 5`
| `*=` | `a *= 3` es equivalente a `a = a * 3`
| `/=` | `a /= 3` es equivalente a `a = a / 3`
| `%=` | `a %= 3` es equivalente a `a = a % 3`
| `**=` | `a **= 3` es equivalente a `a = a ** 3`
| `//=` | `a //= 3` es equivalente a `a = a // 3`
| `&=` | `a &= 3` es equivalente a `a = a & 3`
| `\|=` | `a \|= 3` es equivalente a `a = a | 3`
| `^=` | `a ^= 3` es equivalente a `a = a ^ 3`
| `>>=` | `a >>= 3` es equivalente a `a = a >> 3`
| `<<=` | `a <<= 3` es equivalente a `a = a << 3`


## Operadores Lógicos
Se utiliza un operador lógico para tomar una decisión basada en múltiples condiciones. Los operadores lógicos utilizados en Python son `and`, `or` y `not`.

| **Operador** | **Descripción** | **Ejemplo** |
|--------------|-----------------|-------------|
| `and` | Devuelve True si ambos operandos son True | `a and b`
| `or` | Devuelve True si alguno de los operandos es True | `a or b`
| `not` | Devuelve True si alguno de los operandos False | `not a`
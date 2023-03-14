# Clases

Las clases proveen una forma de empaquetar datos y funcionalidad juntos. Al
crear una nueva clase, se crea un nuevo tipo de objeto, permitiendo crear nuevas
instancias de ese tipo. Cada instancia de clase puede tener atributos adjuntos
para mantener su estado. Las instancias de clase también pueden tener métodos
para modificar su estado.

Python provee las caracteristicas normales de Programación Orientada a Objetos:
el mecanismo de la herencia de clases permite múltiples clases base, una clase
derivada puede sobre escribir cualquier métodos de su clase base, y un método
puede llamar al método de la clase base con el mismo nombre.

La sintaxix de una clase es de la siguiente forma:

```python
class ClassName:
    pass
```

Al igual que las funciones, declarar una función no implica su uso, por lo que
es necesario instanciarlas.

Un ejemplo de una clase sencilla es la siguiente:

```python
class MyClass:
    """Ejemplo de una clase simple"""
    i = 12345

    def f(self):
        return "hello world"
```

En la clase anterior, se cuentan con un atributo `i` y un método `f`. Como
veremos más adelante es normal encontrarse la palabra `self` al momento de
declarar variables o funciones dentro de las clases, esto significa que
pertenecen a la clase y a la instancia de la clase.

## Métodos de la clase

### Constructor

La operación de instanciar una clase crea un objeto vacío. Muchas clases
necesitan crear objetos con un estado inicial particular. Para
realizar esto, Python cuenta con un método especial llamado `__init__()` de la
siguiente forma:

```python
def __init__(self):
    self.data = []
```

De esta forma, al invocar una clase, inmediatamente es invocado el método 
`__init__`.

### Métodos Regulares

Los métodos regulares son aquellos que pueden realizar acciones con los atributos
de las clases y variables externas también. Estos métodos toman la instancia
como primer argumento, de ahí que tienen `self`.

Ejemplo:

```python
class Employee:
    def __init__(self, name, last, salary):
        self.name = name
        self.last = last
        self.email = name + '.' + last + '@company.com'
        self.salary = salary

    def fullname(self):
        return f'{self.name} {self.last}'
```

El método `fullname` utiliza dos atributos de la clase para realizar una acción
de concatenar.

### Métodos de clase

Los métodos de clase son aquellos que en lugar de tomar la instancia como primer
argumento, toman es la clase. Para esto, es necesario realizar el uso del
decorador `@classmethod` y de `cls` como primer argumento del método.

Ejemplo:

```python
class Employee:
    raise_amount = 1.04

    def __init__(self, name, last, salary):
        self.name = name
        self.last = last
        self.email = name + '.' + last + '@company.com'
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
```


### Métodos Estáticos

Los métodos estáticos, son métodos dentro de la clase que no requieren de `self`
dado que no dependen de nada de la clase (variables u otras funciones). Estos
utilizan el decorador `@staticmethod` antes de su declaración.

Ejemplo:

```python
import datetime

class Employee:
    raise_amount = 1.04

    def __init__(self, name, last, salary):
        self.name = name
        self.last = last
        self.email = name + '.' + last + '@company.com'
        self.salary = salary

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
```

### Métodos Especiales

En los métodos especiales podemos nombrar: `__str__()` y `__repr__()` los cuales
permiten realizar una representación de la instancia de la clase para presentar
al usuario final y para hacer debug, respectivamente.

Ejemplo:

```python
class Employee:
    raise_amount = 1.04

    def __init__(self, name, last, salary):
        self.name = name
        self.last = last
        self.email = name + '.' + last + '@company.com'
        self.salary = salary

    def __repr__(self):
        return f"Employee('{self.name}', '{self.last}', '{self.salary}')"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'
```
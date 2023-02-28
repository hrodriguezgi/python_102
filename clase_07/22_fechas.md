# Manejo de Fechas

Python cuenta con una librería llamada `datetime` que permite realizar las
diferentes actividades en relación a las fechas. Una de ellas puede ser tan
sencilla como el imprimir el valor de la fecha actual en nuestro sistema:

```python
>>> import datetime
>>> print(datetime.datetime.now())
2020-01-01 19:02:19.873921
```

Los tipos disponibles son los siguientes:
- `date`: retorna año, mes y fecha
- `time`: retorna hora, minuto, segundo y microsegundo
- `datetime`: retorna una combinación de `date` y `time`
- `timedelta`: retorna una diferencia entre dos `date`, `time` o `datetime`

## Acceso a las propiedades de una fecha
Los objetos de python poseen propiedades que nos permiten acceder a diferentes
valores como:
- `year`: acceso al año
- `month`: acceso al mes
- `day`: acceso al día
- `hour`: acceso a la hora
- `minute`: acceso al minuto
- `second`: acceso al segundo
- `microsecond`: acceso al microsegundo

## Acceso a las funciones de una fecha
### Aplicables para `date` y `datetime`
- `weekday()`: retorna el día de la semana. Lunes es 0 y Domingo es 6.
- `isoweekday()`: retorna el día de la semana. Lunes es 1 y Domingo es 7
- `isocalendar()`: retorna una tupla con el año, semana y día de la semana.
- `isoformat()`: retorna una cadena en el formato `YYYY-MM-DD`
- `strftime()`: retorna una cadena representando la fecha de acuerdo al formato
definido.

### Aplicables para `datetime`
- `date()`: retorna un objeto de tipo `date` con el año, mes y día
- `time()`: retorna un objeto de tipo `time` con la hora, minuto, segundo y
microsegundo
- `replace()`: retorna un objeto de tipo `datetime`con los mismos atributos,
excepto por aquellos que han sido modificados.
- `timestamp()`: retorna una fecha POSIX que corresponde a la fecha ingresada.

### Aplicables para `time`
- `replace`: retorna un objeto de tipo `time`con los mismos atributos, excepto
por aquellos que han sido modificados.
- `isoformat()`: retorna una cadena en el formato `HH:MM:SS`
- `strftime()`: retorna una cadena representando el tiempo de acuerdo al formato


## `strftime` y `strptime`

Los objetos `date`, `datetime` y `time` soportan el método `strftime` para crear
una cadena que represente el objeto origen. Por otro lado el método `strptime`
permite construir un objeto de tipo `datetime` a partir de una cadena,

En la siguiente tabla se puede  revisar todos los códigos de los formatos que
pueden ser utilizados:

| **Formato** | **Descripción** | **Ejemplo** |
|-------------|-----------------|-------------|
| `%a` | Día de la semana, versión corta | Wed
| `%A` | Día de la semana, nombre completo | Wednesday
| `%w` | Día de la semana como numero 0-6, 0 es Domingo | 3
| `%d` | Día del mes 01-31 | 31
| `%b` | Nombre del mes, versión corta | Dec
| `%B` | Nombre del mes, nombre completo | December
| `%m` | Mes como número 01-12 | 12
| `%y` | Año, versión corta | 18
| `%Y` | Año, versión larga | 2018
| `%H` | Hora 00-23 | 17
| `%I` | Hora 00-12 | 05
| `%p` | AM/PM | PM
| `%M` | Minuto 00-59 | 41
| `%S` | Segundo 00-59 | 08
| `%f` | Microsegundo 000000-999999 | 548513
| `%z` | Desfase UTC | +0100
| `%Z` | Zona horaria | CST
| `%j` | Número del día del año 001-366 | 365
| `%U` | Número de semana del año, el Domingo se toma como inicio de la semana, 00-53 | 52
| `%W` | Número de la semana del año, el Lunes se toma como inicio de la semana, 00-53 | 52
| `%c` | Versión de fecha y hora local | Mon Dec 31 17:41:00 2018
| `%C` | Siglo | 20
| `%x` | Versión local de la fecha | 12/31/18
| `%X` | Versión local de la hora | 17:41:00
| `%%` | Caracter % | %
| `%G` | Año ISO 8601 | 2018
| `%u` | Día de la semana ISO 8601 (1-7) | 1
| `%V` | Número de la semana ISO 8601 (01-53) | 01


## Operaciones entre fechas
Con ayuda de `timedelta` se pueden hacer operaciones como adicionar o disminuir
lapsos de tiempo a una fecha. Los argumentos que acepta esta función son: 
- `days`
- `seconds`
- `microseconds`
- `miliseconds`
- `minutes`
- `hours`
- `weeks`

Todos los argumentos son opcionales y tienen un valor por defecto de `0`. Estos
pueden ser enteros o flotantes y positivos o negativos.

Ejemplo:

```python
>>> from datetime import datetime, timedelta
>>> hoy = datetime.today()
>>> print(hoy.date())
2023-02-27
>>> mañana = hoy + timedelta(days=1)
>>> print(mañana.date())
2023-02-28
>>> print(hoy)
2023-02-27 23:05:11.076514
>>> hoy_2 = hoy + timedelta(minutes=-360)
>>> print(hoy_2)
2023-02-27 17:35:11.076514
```

De igual forma, Python también nos permite realizar la diferencia entre dos
objetos de tipo fecha de la siguiente forma

```python
>>> print(hoy)
2023-02-27 23:05:11.076514
>>> print(hoy_2)
2023-02-27 17:35:11.076514
>>> print(hoy - hoy_2)
6:00:00
```
π
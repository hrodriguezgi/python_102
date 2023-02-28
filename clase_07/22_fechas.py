# Manejo de Fechas
print(f"{5*'*'} Manejo de Fechas {5*'*'}\n")

print('Ejemplo 1:')
import datetime
print(datetime.datetime.now())


print('\nEjemplo 2:')
from datetime import datetime, timedelta
hoy = datetime.today()
print(hoy.date())

print('\nEjemplo 2:')
mañana = hoy + timedelta(days=1)
print(mañana.date())

print('\nEjemplo 4:')
print(hoy)

print('\nEjemplo 5:')
hoy_2 = hoy + timedelta(minutes=-360)
print(hoy_2)

print('\nEjemplo 6:')
print(f'hoy: {hoy}')
print(f'hoy_2: {hoy_2}')
print(f'hoy - hoy_2: {hoy - hoy_2}')

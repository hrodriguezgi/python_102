deportes = ['futbol', 'baloncesto', 'tenis', 'ajedrez']
jugadores = [22, 5, 2, 1]

deportes_dict = { deporte: jugador for (deporte, jugador) in zip(deportes, jugadores) }

print(deportes_dict)

# print(deportes_dict.items())
deportes_validos = ['tenis', 'ajedrez']

deportes_multijugador = { deporte: jugador for deporte, jugador in deportes_dict.items() if deporte in deportes_validos }

print(deportes_multijugador)
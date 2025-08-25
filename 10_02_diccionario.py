#Iniciar un diccionario vacio
jugador = {}
print(jugador)

#Agregar nombre
jugador['nombre'] = 'Luan'
jugador['puntaje'] = 10
print(jugador)

#Incrementa su puntaje
jugador['puntaje'] = 15
print(jugador)

#Acceder a un valor 
print(jugador.get('consola','No existe ese valor'))

#Usando Iterador en el diccionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)

#Eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntaje']
print(jugador)

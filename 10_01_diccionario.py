#Creando diccionario simple
cancion = {
    'artista' : 'Nirvana',
    'cancion' : 'Lithium',
    'lanzamiento' : 1985,
    'likes' : 3000000
}        
print(cancion)

#Acceder alos elementos del diccionario
print(cancion['cancion'])

#Mezclar con un string
artista = cancion['artista']
print(f'Estoy escuchando a {artista}')

#agregar nuevos valores

cancion['nacimiento'] = 1975
print(cancion)

#Cambiar un valor por otro 
cancion['cancion'] = 'Come As You Are'
print(cancion)

#Eliminar un valor 
del cancion['likes']
print(cancion)


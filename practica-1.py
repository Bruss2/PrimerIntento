playlist = {} #Diccionario vacio
playlist['Canciones'] = [] #Lista vacia dentro del diccionario

#Funcion principal
def app():

    #Agregar playslist
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Ingresa el nombre de la playlist: \r\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

            #Ya tenemos un nombre, de la playlist desactivar el True
            agregar_playlist = False

           

            agregar_canciones()
            
def agregar_canciones():
    

    #Bandera para agregar cancion
    agregar_canciones = True
    while agregar_canciones:
       nombre_playlist = playlist['nombre']
       pregunta = f'\r\nAgregar canciones para la playlist {nombre_playlist}:\r\n'
       pregunta += 'Escribe "CERRAR" Para dejar de agregar canciones\r\n'

       cancion = input(pregunta) #Solicitar cancion
       if cancion == 'CERRAR':
           print(f'Playlist: {nombre_playlist}\r\n')
           print(f'Canciones: \r\n')
           for cancion in playlist['Canciones']:#Iterar sobre las canciones
               print(f'- {cancion}')
           agregar_canciones = False #Salir del ciclo
       else:
           playlist['Canciones'].append(cancion)
           print(f'Cancion {cancion} agregada a la playlist {nombre_playlist}')
           print(f'Playlist actual: {playlist}') 

app()

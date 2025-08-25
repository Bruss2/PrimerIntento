def app():
    #Crear el archivo
    archivo = open("14_01_archivos.txt", "w")

    for i in range(0, 21):
        archivo.write('Linea ' + str(i) + "\n")

    archivo.close()

app()
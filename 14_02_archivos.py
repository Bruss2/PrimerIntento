def app():
    with open('14_01_archivos.txt') as archivo:
        for contenido in archivo:
            print(contenido.rstrip())  # Imprime cada línea en vertical, sin saltos extra
app()
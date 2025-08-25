import os
CARPETA = 'contacto/' # carpeta de contacto
EXTENSION = '.txt' # extension de los archivos

#contacto
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():

    #Revisar si la carpeta existe
    crear_directorio()

    mostrar_menu()

    #Preguntar a nuestro usuario la opcion a elegio
    preguntar = True
    while preguntar:
        opcion = input('Ingrese una opcion: \r\n ')
        if not opcion.isdigit():
            print('Por favor ingrese un número válido.')
            continue
        opcion = int(opcion)
        # ...resto del código...
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo.')
        
def eliminar_contacto():
    nombre = input('Escribe el nombre del contacto a eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Contacto eliminado con exito!')
    except IOError:
        print('No existe el contacto')
        print(IOError)

    app()

def buscar_contacto():
    nombre = input('Escribe el nombre del contacto a buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('Contacto no encontrado.')
        print(IOError)

    app()

def mostrar_contacto():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
        
def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
    
    #REVISAR SI YA EXISTE EL CONTACTO PARA EDITARLO
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION,'w') as archivo:
            
            #RESTO DE LOS CAMPOS
            nombre_contacto = input('Agregar el nuevo nombre del contacto: \r\n')
            telefono_contacto = input('Agregar el nuevo numero del contacto: \r\n')
            categoria_contacto = input ('Agregar la nueva categoria del contacto: \r\n')

            #INSTANCIAR LA CLASE

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #ESCRIBIR EN EL ARCHIVO 
            archivo.write('Nombre: '+ contacto.nombre + '\n')
            archivo.write('Telefono: '+ contacto.telefono + '\n')
            archivo.write('Categoria: '+ contacto.categoria + '\n')

            

            #MOSTRAR UN MENSAJE DE EXITO
            print(' Contacto editado con exito! \r\n') 
        #RENOMBRAR EL ARCHIVO
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
    
    else:
        print('El contacto no existe, por favor intente con otro nombre.')

    #REINICIAR LA APP 
    app()

def agregar_contacto():
    print('Escribe los datos para agregar nuevo contacto')
    nombre_contacto = input('Nombre del contacto: \r\n')

    #REVISAR SI YA EXISTE EL CONTACTO
    existe = existe_contacto(nombre_contacto)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION,'w') as archivo:
           

            #RESTO DE LOS CAMPOS
            telefono_contacto = input('Numero de telefono: \r\n')
            categoria_contacto = input ('Categoria del contacto: \r\n')

            #INSTANCIAR LA CLASE

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #ESCRIBIR EN EL ARCHIVO 
            archivo.write('Nombre: '+ contacto.nombre + '\n')
            archivo.write('Telefono: '+ contacto.telefono + '\n')
            archivo.write('Categoria: '+ contacto.categoria + '\n')

            #MOSTRAR UN MENSAJE DE EXITO
            print('\r\n Contacto Creado Correctamente \r\n')
    
    else:
        print('El contacto ya existe, por favor intente con otro nombre.')

    #REINICIAR LA APP 
    app()
    
def mostrar_menu():
    print('Bienvenido al gestor de contactos')
    print('1) Agregar contacto')
    print('2) Editar contacto')
    print('3) Ver contacto')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()  # Iniciar la aplicación
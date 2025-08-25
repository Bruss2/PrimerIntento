class Restaurant:

    def __init__(self, nombre, categoria, precio):
        #Inicializar atributos
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio # Atributo privado

        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre} Categoria: {self.categoria} Precio: {self.__precio}')

#GETTER AND SETTERS - get = obtener un valor, set = para modificar el valor
    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio  
    
#Creando una clase Hijo del Restaurante
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel California', '5 estrellas', 500)
hotel.mostrar_informacion()
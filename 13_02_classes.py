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

#Instanciar la clase
restaurant = Restaurant('El Buen Sabor', 'Comida Mexicana', 150)
restaurant.mostrar_informacion()    
restaurant.set_precio(200)  # Modificar el atributo privado usando el setter
precio = restaurant.get_precio()  # Obtener el valor del atributo privado usando el getter
print(f'El precio  del restaurant es: {precio}')

restaurant2 = Restaurant('La Casa de la Pasta', 'Comida Italiana', 200 )
restaurant2.mostrar_informacion()
restaurant2.set_precio(300)  # Modificar el atributo privado usando el setter
precio = restaurant2.get_precio()  # Obtener el valor del atributo privado usando el getter
print(f'El precio  del restaurant es: {precio}')

restaurant3 = Restaurant('Sushi Place', 'Comida Japonesa', 250)
restaurant3.mostrar_informacion()
restaurant3.set_precio(350)  # Modificar el atributo privado usando el setter
precio = restaurant3.get_precio()  # Obtener el valor del atributo privado usando el getter
print(f'El precio del restaurant es: {precio}')
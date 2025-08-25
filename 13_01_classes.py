class Restaurant:

    def __init__(self, nombre, categoria, precio):
        #Inicializar atributos
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre} Categoria: {self.categoria} Precio: {self.precio}')

#Instanciar la clase
restaurant = Restaurant('El Buen Sabor', 'Comida Mexicana', 150)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('La Casa de la Pasta', 'Comida Italiana', 200 )
restaurant2.mostrar_informacion()

restaurant3 = Restaurant('Sushi Place', 'Comida Japonesa', 250)
restaurant3.mostrar_informacion()

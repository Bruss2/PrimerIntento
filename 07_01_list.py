lenguajes = ['PHP','C++','Python','Java']
print(lenguajes)

#Los arrays (lists) comienzan en la posicion 0 
print(lenguajes[0])

#Ordenar los arreglos alfabeticamente
lenguajes.sort()
print(lenguajes)

#Acceder a un elemento del  arreglo dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#Modifica un elemento de un texto
lenguajes[0] = 'Python'
print(lenguajes)

lenguajes[3] = 'C++'
print(lenguajes)

#Agregar un elemento al arreglo ( lists )
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar un elemento del arreglo ( lists)
del lenguajes[1]
print(lenguajes)

#Eliminar el ultimo elemento del arreglo ( lists ) 
lenguajes.pop()
print(lenguajes)

#Eliminar con pop un elemento especifico
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre 
lenguajes.remove('C++')
print(lenguajes)
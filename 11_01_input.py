#nombre = input('Cual es tu nombre? ')
#print(f'Hola {nombre}')
#print(9/2)
#Leer datos que seran numeros

edad = input('Cual es tu edad? ')
#Convertir string a entero
edad = int(edad)
if edad >= 18:
    print('Ya puedes acceder al sistema')
else:
    print('Aun no puedes acceder al sistema')

#Mezclar con operadores

numero = input('Agregar un numero y te dire si es par o inpar: \r\n')
numero = int(numero)

if numero % 2 == 0:
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')
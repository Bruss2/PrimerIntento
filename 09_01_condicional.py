#Revisar si una condicion es mayor o menor
balance = 500
if balance > 501:
    print('Puedes pagar')
else:
    print('No puedes pagar')

#Likes
likes = 200
if likes != 200:
    print('Felicidades, llegaste a los 200 likes')
else:
    print('Sigue esforzandote')


#if con texto
lenguaje = 'Python'
if lenguaje != 'Python':
    print('Buena decision')
else:
    print('Puede servir')

#Evaluar un Boolean
usuario_autenticado = False
if usuario_autenticado:
    print('Ingresaste al sistema')
else:
    print('Contraseña incorrecta')

#Evaluar un elemento de la lista
lenguajes = ['PHP', 'C++', 'Python', 'Java' ]
if 'Ruby' in lenguajes:
    print('Si existe PHP')
else:
    print('El programa no existe')

#IF anidados ( un if dentro de otro if)
usuario_autenticado = False
usuario_admin = False
if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Accediste al sistema')
else:
    print('Contraseña incorrecta')
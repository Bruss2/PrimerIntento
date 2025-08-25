#RETO 1 : HACER UN EXAMEN DE 3 PREGUNTAS CADA PREGUNTA CORRECTA VALE 2 PUNTOS  
#NOTA APROBATORIA ES DE 3 A 6

print('EXAMEN PARCIAL ')
print('Cada pregunta vale 2 puntos')
pregunta1 = input('2+2 es 4?: \r\n')
pregunta1= str(pregunta1)
numero = 0
if pregunta1 == 'si':
    print('Tu respuesta es correcta')
    numero += 2
    print(f' Tienes {numero} punto(s)')
else:
    print('Tu respuesta es incorrecta')
    print(f'Tienes {numero} punto(s)' )

pregunta2 = input('4 x 4 es 8? \r\n')
pregunta2= str(pregunta2)

if pregunta2 == 'si':
    print('Tu respuesta es correcta')
    numero += 2
    print(f' Tienes {numero} punto(s)')
else:
    print('Tu respuesta es incorrecta')
    print(f'Tienes {numero} punto(s)' )

pregunta3 = input('10/5 es 2? \r\n')
pregunta3= str(pregunta3)

if pregunta3 == 'si':
    print('Tu respuesta es correcta')
    numero += 2
    print(f' Tienes {numero} punto(s)')
else:
    print('Tu respuesta es incorrecta')
    print(f'Tienes {numero} punto(s)' )
    
print(f'Tu nota final es {numero}')

if numero >=3:
    print('APROBASTE')
else:
    print('DESAPROBASTE')

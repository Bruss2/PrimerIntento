#Ejemplo de elif
Ocupacion = 'Nuevo estudiante'

if Ocupacion == 'Estudiante':
    print('Tienes un descuento de 50%')
elif Ocupacion == 'Hijo de trabajador':
    print('Tienes un descuento de 30%')
elif Ocupacion == 'Ex Alumno':
    print('Tienes un descuento de 70%')
else:
    print('Paga 100%')
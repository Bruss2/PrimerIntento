#Operador and y or

usuario_loqueado = False
usuario_administrador = True

if usuario_loqueado or usuario_administrador:
    print('Se ha iniciado como Administrador')
elif usuario_loqueado:
    print('Usuario iniciado')
else:
    print('Contraseña o usuario incorrecto')
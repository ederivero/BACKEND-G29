def saludar():
    print('Bienvenido')

saludar()
saludar()
saludar()
saludar()

# a las funciones le podemos poner parametros con valores predeterminados y estos siempre van al final (despues de los parametros sin valores pred)
def saludar_con_nombre(nombre, estilo='Formal'):
    if estilo == 'Formal':
        print('Buenas noches',nombre)
    else:
        print('Habla',nombre)

saludar_con_nombre('Eduardo')
saludar_con_nombre('Roberto','Informal')

parametros = {
    'nombre':'Max',
    'estilo': 'Informal'
}

# si quiero utilizar un diccionario como parametros tengo que declarar ** en el parametro
saludar_con_nombre(**parametros)
# El diccionario DEBE DE TENER los mismos nombre de los parametros que las llaves, si no es lo mismo lanzara un error, esto sirve para convertir las llaves del diccionario en el nombre de los parametros y sus valores en el contenido de los parametros

# Se puede crear funciones que reciban un numero ilimitado de valores 
def sumar(*args):
    # Todos los parametros pasados se almacenaran en una tupla (inmutable y ordenada)
    print(args)

sumar(10,20,50,100,250,320,580)
####### Listas (Lists) #######
# Mutable (puede cambiar su contenido) y ordenada (se maneja por indices)
numeros_telefonicos = ['105', '104', '935472982', 123]

numeros_telefonicos.append('*123#')
numeros_telefonicos.append(True)

# podemos acceder por sus indices (el cual siempre empieza en 0)
print(numeros_telefonicos[0])

# se puede obtener una sub lista de los elementos usando limites
# que vaya desde >=1 hasta <3
print(numeros_telefonicos[1:3])

print(numeros_telefonicos[2:])
print(numeros_telefonicos[:3])
print(numeros_telefonicos[-1])

# La forma en la cual se puede retirar elementos
# Con el metodo pop lo quitamos de la lista y podemos almacenar el elemento quitado en otra variable 
elemento_eliminado = numeros_telefonicos.pop(0)

# del > elimina el elemento y ya no se puede recuperar
del numeros_telefonicos[0]

# clear limpia toda la lista y la deja en blanco
numeros_telefonicos.clear()


# Crear una lista llamada menu_postres en la cual se tenga los siguientes elementos:
# Croissant
# torta de manzana
# Voladores
# Luego quitar los Croissant de la lista
# Agregar el postre Alfajores
# Imprimir la lista para ver que postres hay
menu_postres = ['Croissant', 'torta de manzana', 'voladores']
del menu_postres[0]
menu_postres.append('Alfajores')
print(menu_postres)

######## TUPLAS ########
# Ordenadas pero no se pueden editar (una vez creadas ahi quedan)
usuarios = ('eduardo', 'jhonatan', 'roxana', 'marta')

# Yo puedo solicitar si un valor esta o no en la tupla con la palabra in (estar de contenido)
print('eduardo' in usuarios)



######## Diccionarios ########
# Es una coleccion de datos que se manejan por llave-valor en vez de indices y tbn son editables
persona = {
    "nombre":"eduardo",
    "apellido":"perez",
    "nacionalidad":"peruana",
    "direccion": {
        "calle":"av primavera",
        "numero": "1250",
        "referencia": "a media cuadra del semaforo"
    },
    "hobbies": ["jugar futbol", "pescar", "programar"]
}

print(persona["nombre"])

# como podria saber cual es la calle donde vivo?
print(persona["direccion"]["calle"])
# bailar es uno de mis hobbies? (in)
print("bailar" in persona["hobbies"])
# me gustaria saber mi ultimo hobbie
print(persona["hobbies"][-1])

articulos = {
    "cafe": {
        "cantidad": 10,
        "precio": 4.5,
        "disponible": True
    },
    "leche":{
        "cantidad": 2,
        "precio": 2.3,
        "disponible": False
    },
    "te": {
        "cantidad": 0,
        "precio": 0.5,
        "disponible":False
    },
    "observaciones": ("Falta te", "Agregar azucar", "Mejorar presentacion")
}

# Cuantas cantidades de leche tengo
print(articulos['leche']['cantidad'])
# Cual es la segunda observacion
print(articulos['observaciones'][1])
# Cual es el precio del cafe
print(articulos['cafe']['precio'])


######## COJUNTOS (SET) ########
# No es ordena pero si es modificable
planetas = {'Tierra', 'Marte', 'Jupiter', 'Uranio'}

# asi se puede agregar elementos al conjunto
planetas.add('Neptuno')

# asi se elimina elementos del conjunto
planetas.remove('Tierra')

print('Tierra' in planetas)
print(planetas)
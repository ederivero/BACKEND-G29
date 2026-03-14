edad = 10

# if CONDICION(ES) : 
if edad > 18 :
    print('Eres mayor de edad')
else:
    # Si la condicion no se verdad 
    print('Eres menor de edad')


print('Gracias')

# Se puede agregar varias condicionales and , or
# and > todas las condicionales tienen que ser verdadero para que sea verdadero
# or > basta con que una de ellas sea verdadera para que sea considerado como v

# Tengo mi pagina de ventas en la cual tengo productos que vendo a personas solo de Peru
# entonces si al momento de pagar esa persona es peruana entonces el envio es gratis, si no es de peru entonces el envio es 100 dolares
nacionalidad = 'peruana'

# mostrar cuanto es el envio
nacionalidad = 'boliviana'

# Cuando hacemos comparacion en el if se usa doble igual 
# == comparacion
# = asignacion
if nacionalidad == 'peruana':
    print('Envio gratis')
else:
    print('Envio de 100 dolares')

# Tengo un restaurante y genero promociones si el dia es jueves y la hora es las 11:00 o las 15:00 entonces mostrar que el "broaster sale a 5.00",si el dia es sabado mostrar que hay 2x1 en bebidas y sino indicar que no hay promociones vigentes
dia = 'jueves'
hora = '20:00'

if dia == 'jueves' and (hora == '11:00' or hora =='15:00'):
    print('broaster sale a 5.00')
# sino si CONDICIONAL
elif dia == 'sabado':
    print('2x1 en bebidas')
else:
    print('No hay promos') 

# Tengo una tienda de ropa en la cual tengo las siguientes caracteristicas
# Si el genero es Masculino solo tengo stock en las tallas XL o L
# Si es femenino tengo stock en las tallas L o M
genero = 'Masculino'
talla ='XL'
# Mostrar al usuario si tengo o no tengo stock en mi ropa
if genero == 'Masculino' and (talla == 'XL' or talla == 'L'):
    print('Hay stock')
elif genero =='Femenino' and (talla == 'L' or talla == 'M') :
    print('Hay stock')
else:
    print('No hay stock')
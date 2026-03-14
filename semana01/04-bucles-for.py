alumnos = ['Eduardo','Pedro', 'Juan','Gilberto', 'Felipe']

for alumno in alumnos:
    # cada vuelta o cada elemento que se itere se almacenara en esa variable del for

    if alumno == 'Eduardo':
        # si quiero saltarme una iteracion usaremos el continue
        continue
    # si quiero terminar de manera abrupta la iteacion uso el break
    if alumno == 'Gilberto':
        break
    print(alumno)


# range(valor_inicial, valor_final, incrementador)
# si el valor inicial es 0 podemos prescindir de el
# si el contador es +1 podemos prescindri de el

for numero in range(1,10):
    print(numero)

# tambien se usar para poder iterar texto
texto = 'Hola a todos mi nombre es eduardo'
for letra in texto:
    print(letra)



# tengo yo los siguientes precios
productos = [10.5, 11.2, 14, 20]
# Me gustaria saber el precio con su igv (al precio actual agregarle el 18%, multiplicar el valor x 1.18)
for producto in productos:
    print('Valor original:')
    print(producto)
    print('Valor con igv:')
    print(producto * 1.18)


# tengo los siguientes productos de mis ventas
ventas = [
    {
        "producto":"Cafe", 
        "precio": 12.5
    }, 
    {
        "producto":"Agua mineral", 
        "precio": 5
    }, 
    {
        "producto": "Manjar", 
        "precio":8.4
    }]
total = 0
# Me gustaria saber cuanto eh vendido (25.9)

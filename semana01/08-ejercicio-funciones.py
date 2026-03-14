# crear una funcion en la cual sirva para calcular la propina de una cuenta, en esta funcion se recibira la cuenta y el porcentaje de propina, es decir, el monto y cuanto de ese monto debe de darse como propina. 
# calcular_propina(100,15)
# el resultado debe ser: "Propina es de 15 soles"
# El valor predeterminado del porcentaje es 10
def calcular_propina(monto,porcentaje=10):
    resultado = monto * porcentaje / 100
    print("Propina es de",resultado,"soles")

calcular_propina(20,50)

# Hacer el fizzbuzz 
# FizzBuzz es un popular ejercicio de programación que consiste en imprimir los números del 1 al 100. Se sustituyen los múltiplos de 3 por "Fizz", los múltiplos de 5 por "Buzz" y los múltiplos de ambos (como 15) por "FizzBuzz". Se suele usar para evaluar la lógica básica en entrevistas de desarrollo
# procesar_numero(15)
# Devolver "Fizz" si el numero es divisible entre 3
# Devolver "Buzz" si el numero es divisible entre 5
# Devolver "FizzBuzz" si el numero es divisible entre 3 y 5
# 30 % 3 > True 
def procesar_numero(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print("No es divisible")

procesar_numero(3)
procesar_numero(5)
procesar_numero(30)

# Funcion que reciba un operador que puede "Suma", "Resta", "Multiplicacion" y n cantidad de numeros y retorne el resultado en base a su operador 
# super_funcion("Suma", 10,20,30,40,50,...) > 150
# super_funcion("Multiplicaion", 5,4,6,7) > 840

def super_funcion(operador, *valores):
    # valores > tupla
    total = 0
    if operador == 'Suma':
        for numero in valores:
            total = total + numero

    elif operador == 'Resta':
        for numero in valores:
            total = total - numero

    elif operador =='Multiplicacion':
        total = 1
        for numero in valores:
            total = total * numero
    
    else:
        print('Operador incorrecto')
    print(total)

super_funcion('Suma',10,20,30,40,50)
super_funcion("Multiplicacion", 5,4,6,7)


def es_par(numero):
    # En las funciones se puede retornar un resultado para que este pueda ser almacenado en una variable o ser usado posteriormente
    return numero % 2 == 0


resultado = es_par(11)
print(resultado)

# Operador ternarias
numero = 4
# VALOR_VERDADERO if CONDICIONAL false VALOR_FALSO
es_impar = True if numero % 2 != 0 else False
print(es_impar)
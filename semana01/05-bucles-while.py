numero = 20

while numero > 0:
    print(numero)
    # numero = numero - 1
    numero -= 1

# Todos los valores ingresados siempre seran string 
variable = input("Ingresa un numero: ")
print(type(variable))
# Para convertir un valor ingresado a un numero 
variable_numerica = int(variable)
print(type(variable_numerica))
print(variable)


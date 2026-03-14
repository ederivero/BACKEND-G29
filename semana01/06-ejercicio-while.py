# Se tiene un numero ganador y el usuario tiene que intentar adivinarlo, si el numero ganador es 10 y el usuario ingresa 20 entonces indicarle que el numero es menor, si el usuario ingresa 5 indicarle que el numero es mayor y si el usuario adivina el numero entonces felicitarlo y terminar el juego

numero_ganador = 10
# Crear un while hasta que el usuario adivine el numero, para finalizar un while de manera abrupta se usa el break

while True:
    numero = int(input('Ingresa un numero: '))
    if numero == numero_ganador:
        print('Felicitaciones! Adivinaste')
        break
    else:
        if numero > numero_ganador:
            print('El numero es menor')
        else:
            print('El numero es mayor')

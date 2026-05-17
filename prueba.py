A = 10

B = 30

SUMA = A + B

print("La suma de A y B es:", SUMA)

# Hace un intervalo de del resultado de la suma
INTERVALO = range(SUMA - 5, SUMA + 5)

print("El intervalo alrededor de la suma es:", list(INTERVALO))

# Verifica si la suma es un número par o impar

if SUMA %  2 == 0:
    print("La suma es un número par.")
else:
    print("La suma es un número impar.")

# Calcula el cuadrado de la suma

CUADRADO = SUMA ** 2
print("El cuadrado de la suma es:", CUADRADO)

#  piedra papel tijera

import random

opciones = ["piedra", "papel", "tijera"]

jugador = input("Elige piedra, papel o tijera: ").lower()

computadora = random.choice(opciones)

print("La computadora eligió:", computadora)

if jugador == computadora:
    print("Empate!")
elif (jugador == "piedra" and computadora == "tijera") or \
     (jugador == "papel" and computadora == "piedra") or \
     (jugador == "tijera" and computadora == "papel"):
    
    print("¡Ganaste!")

else:
    print("¡Perdiste!")

numero = int(input("Ingresa un número para verificar si es primo: "))

print ("El número ingresado es:", numero)

print("Verificando si el número es primo...")
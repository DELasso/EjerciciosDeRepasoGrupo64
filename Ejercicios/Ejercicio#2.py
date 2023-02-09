#2. Escribir una función que calcule el área de un círculo dado su radio.
import math
print("Ingrese un número para el área del círculo:")
radio = float(input())
pi= math.pi * (radio*radio)
print("El círculo tiene radio:",radio,".", " Y el área del círculo es de:", pi)
#Si usamos round podemos redondear.
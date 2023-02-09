#6.Crear un programa que calcule la suma de los números en una lista dada.
import random

num=int(input("Ingrese la cantidad de números de la lista:"))
sumar=0
aleatorios = [random.randint(0,1000) for i in range(num)]
for j in aleatorios:
    sumar=sum(aleatorios)
print("Sus números aleatorios son:", aleatorios)
print("La suma de sus números es:", sumar)
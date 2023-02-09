#14. Escribir una función que calcule la media aritmética de una lista de números.
import random
from numpy import mean
def media_aritmetica(num):
    aleatorios = [random.randint(0,5) for i in range(num)]
    print("La lista de números es:", aleatorios)
    return print("La media aritmetica de la lista es:", mean(aleatorios))



num=int(input("Ingrese la cantidad de números de la lista:"))
media_aritmetica(num)
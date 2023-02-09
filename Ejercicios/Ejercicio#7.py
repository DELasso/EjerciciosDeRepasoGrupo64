#7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.
import random

cantidad_num=int(input("Ingrese la cantidad de números de la lista:"))
lista_num = [random.randint(0,1000) for i in range(cantidad_num)]
print("Sus números aleatorios son:", lista_num)
print("El número más grande de la lista es:", max(lista_num))
print("El número más pequeño de la lista es:", min(lista_num))
# 9. Crear un programa que genere una matriz de números y la imprima en pantalla.

from random import randint


def numeros_de_matriz(n):
    matriz = []

    for i in range(n):
        fila = []

        for j in range(n):
            fila.append(randint(1, 100))

        matriz.append(fila)
    return matriz


n = int(input("Ingresar una cantidad de números para la matriz:"))
resultado = numeros_de_matriz(n)
print("Sus matrices son:", resultado)
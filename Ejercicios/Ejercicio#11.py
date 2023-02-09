#11. Crear un programa que genere una lista de números pares entre 1 y 100.
numeros_pares=[]
numero = 1
while numero <= 100:
    if numero % 2 == 0:
        numeros_pares.append(numero)

    numero = numero + 1
print(numeros_pares)
#3. Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random
Numeros_Aleatorios = []
for i in range(0,5):
  Numeros_Aleatorios.append([0]*20)
for i in range(0,5):
    for j in range(0,20):
        Numeros_Aleatorios[i][j] = random.randint(0,20000)
print(Numeros_Aleatorios)
#4. Escribir un programa que determine si un número dado es par o impar.
numero=int(input("Ingrese un número:"))
if numero % 2 == 0:
    print("El número", numero,"es par")
else:
    print("El número", numero, "es impar")
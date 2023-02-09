#10. Escribir una función que calcule el factorial de un número dado.

numero=int(input("Ingresar un número para convertirlo a factorial:"))
factorial= 1
for i in range(1,numero+1):
    factorial*=i
print("Su número en factorial es:", factorial)
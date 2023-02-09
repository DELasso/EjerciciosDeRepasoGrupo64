# 15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.

def palindromo(texto):
    posicion_izquierda = 0
    posicion_derecha = len(texto) - 1

    while posicion_derecha >= posicion_izquierda:
        if not texto[posicion_izquierda] == texto[posicion_derecha]:
            return False

        posicion_izquierda += 1
        posicion_derecha -= 1

    return True


print(palindromo("david"))
print(palindromo("adan"))
print(palindromo("oso"))
print(palindromo("somos"))
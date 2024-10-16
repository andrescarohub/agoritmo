def solicitar_numero():
    """Solicita un número entero positivo al usuario."""
    return int(input("Ingresa un número entero positivo: "))

def contar_regresivamente(numero):
    """Imprime los números desde el número dado hasta 1."""
    contador = numero
    while contador >= 1:
        print(contador)
        contador -= 1

# Programa principal
numero = solicitar_numero()

if numero > 0:
    contar_regresivamente(numero)
else:
    print("Por favor, ingresa un número entero positivo.")

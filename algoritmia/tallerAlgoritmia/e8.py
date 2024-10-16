def main():
    """Función principal del programa."""
    suma = 0
    contador = 0

    while True:
        try:
            numero = float(input("Ingresa un número positivo (o un número negativo para terminar): "))
            if numero < 0:
                break  # Termina el bucle si se ingresa un número negativo
            
            suma += numero
            contador += 1

        except ValueError:
            print("Por favor, ingresa un número válido.")

    if contador > 0:
        promedio = suma / contador
        print(f"El promedio de los números ingresados es: {promedio:.2f}")
    else:
        print("No se ingresaron números positivos.")

if __name__ == "__main__":
    main()

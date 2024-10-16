def solicitar_numero():
    """Solicita al usuario ingresar un número."""
    while True:
        try:
            numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
            return numero
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def mostrar_tabla_multiplicar(numero):
    """Muestra la tabla de multiplicar del número ingresado."""
    print(f"Tabla de multiplicar de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    """Función principal del programa."""
    numero = solicitar_numero()
    mostrar_tabla_multiplicar(numero)

if __name__ == "__main__":
    main()

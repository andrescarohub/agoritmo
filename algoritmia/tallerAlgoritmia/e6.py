def solicitar_longitudes():
    """Solicita al usuario ingresar tres longitudes."""
    while True:
        try:
            a = float(input("Ingresa la longitud del primer lado: "))
            b = float(input("Ingresa la longitud del segundo lado: "))
            c = float(input("Ingresa la longitud del tercer lado: "))
            return a, b, c
        except ValueError:
            print("Por favor, ingresa valores numéricos válidos.")

def es_triangulo(a, b, c):
    """Verifica si las longitudes pueden formar un triángulo válido."""
    return (a + b > c) and (a + c > b) and (b + c > a)

def main():
    """Función principal del programa."""
    a, b, c = solicitar_longitudes()
    if es_triangulo(a, b, c):
        print("Las longitudes pueden formar un triángulo válido.")
    else:
        print("Las longitudes no pueden formar un triángulo válido.")

if __name__ == "__main__":
    main()

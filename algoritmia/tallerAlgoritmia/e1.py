def solicitar_edad():
    """Solicita al usuario su edad y devuelve un entero."""
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if edad >= 0:  # Verificamos que la edad no sea negativa
                return edad
            else:
                print("La edad no puede ser negativa. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Debes ingresar un número entero.")

def verificar_mayoria_edad(edad):
    """Verifica si la edad es mayor o igual a 18."""
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

# Programa principal
edad_usuario = solicitar_edad()
verificar_mayoria_edad(edad_usuario)

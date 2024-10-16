def solicitar_calificacion():
    """Solicita al usuario ingresar su calificación."""
    while True:
        try:
            calificacion = float(input("Ingresa tu calificación en el examen: "))
            return calificacion
        except ValueError:
            print("Por favor, ingresa un número válido.")

def verificar_aprobacion(calificacion):
    """Verifica si la calificación es suficiente para aprobar."""
    if calificacion >= 60:
        return "Has aprobado"
    else:
        return "Has reprobado"

def main():
    """Función principal del programa."""
    calificacion = solicitar_calificacion()
    resultado = verificar_aprobacion(calificacion)
    print(resultado)

if __name__ == "__main__":
    main()

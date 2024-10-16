from datetime import datetime

def solicitar_informacion_empleado():
    """Solicita la información del empleado."""
    nombre = input("Ingresa el nombre del empleado: ")
    apellidos = input("Ingresa los apellidos del empleado: ")
    fecha_ingreso = input("Ingresa la fecha de ingreso (formato: YYYY-MM-DD): ")
    
    return nombre, apellidos, fecha_ingreso

def calcular_antiguedad(fecha_ingreso):
    """Calcula la antigüedad en años desde la fecha de ingreso."""
    fecha_ingreso_dt = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
    fecha_actual = datetime.now()
    antiguedad = fecha_actual.year - fecha_ingreso_dt.year
    
    if (fecha_actual.month, fecha_actual.day) < (fecha_ingreso_dt.month, fecha_ingreso_dt.day):
        antiguedad -= 1
    
    return antiguedad

def main():
    """Función principal del programa."""
    nombre, apellidos, fecha_ingreso = solicitar_informacion_empleado()
    antiguedad = calcular_antiguedad(fecha_ingreso)
    
    print(f"\nInformación del empleado:")
    print(f"Nombre: {nombre}")
    print(f"Apellidos: {apellidos}")
    print(f"Antigüedad: {antiguedad} años")

if __name__ == "__main__":
    main()

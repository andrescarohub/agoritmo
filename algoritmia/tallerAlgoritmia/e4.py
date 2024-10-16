def solicitar_contraseña():
    """Solicita al usuario ingresar una contraseña."""
    return input("Ingresa una contraseña: ")

def verificar_contraseña(contraseña):
    """Verifica si la contraseña cumple con los requisitos."""
    if len(contraseña) >= 8 and any(char.isdigit() for char in contraseña):
        return "Contraseña válida"
    else:
        return "Contraseña inválida"

def main():
    """Función principal del programa."""
    contraseña = solicitar_contraseña()
    resultado = verificar_contraseña(contraseña)
    print(resultado)

if __name__ == "__main__":
    main()

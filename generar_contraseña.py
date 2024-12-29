import random
import string

def generar_contraseña():
    # Solicitar longitud de la contraseña
    longitud = int(input("¿Qué longitud quieres para la contraseña? "))

    # Preguntar al usuario qué tipos de caracteres desea incluir
    # Cambiar las comparaciones para aceptar tanto "sí" como "si"
    incluir_mayusculas = input("¿Incluir mayúsculas? (sí/no): ").strip().lower() in ['sí', 'si']
    incluir_minusculas = input("¿Incluir minúsculas? (sí/no): ").strip().lower() in ['sí', 'si']
    incluir_numeros = input("¿Incluir números? (sí/no): ").strip().lower() in ['sí', 'si']
    incluir_simbolos = input("¿Incluir símbolos especiales? (sí/no): ").strip().lower() in ['sí', 'si']


    # Conjuntos de caracteres posibles
    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase  # Mayúsculas (A-Z)
    if incluir_minusculas:
        caracteres += string.ascii_lowercase  # Minúsculas (a-z)
    if incluir_numeros:
        caracteres += string.digits  # Números (0-9)
    if incluir_simbolos:
        caracteres += string.punctuation  # Símbolos especiales (!, @, #, etc.)

    # Verificar si al menos una opción fue seleccionada
    if not caracteres:
        print("¡Error! Debes elegir al menos un tipo de carácter.")
        return

    # Generar una contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

    return contraseña

# Generar y mostrar la contraseña
contraseña_generada = generar_contraseña()
print(f"La contraseña generada es: {contraseña_generada}")

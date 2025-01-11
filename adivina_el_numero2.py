# Ahora el numero lo va a adivinar la computadora

import random


def advina_el_numero_PC(x):
    
    print("======================")
    print(" Bienvenido al juego! ")
    print("======================")
    print(f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo...")
    
    limite_inferior = 1
    limite_superior = x
    
    respuesta_usuario = ""
    while respuesta_usuario != "c":
        # Generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior # Tambien podria ser el limite superior
            
        # Obtener una respuesta del usuario
        respuesta_usuario = input(f"Mi prediccion es: {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C)").lower()
        
        if respuesta_usuario == "a":
            limite_superior = prediccion - 1
        elif respuesta_usuario == "b":
            limite_inferior = prediccion + 1
            
    print(f"La computadora logró adivinar tu numero correctamente: {prediccion} !!!")
    
advina_el_numero_PC(10)
    
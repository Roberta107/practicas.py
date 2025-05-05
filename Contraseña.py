import re
def validar_contraseña(contraseña):
    # Verifica que tenga al menos 8 caracteres, una mayuscula, una minuscula y un numero 
    if (len(contraseña) >=8 and
    re.search(r"[A-Z]", contraseña) and
    re.search(r"[a-z]", contraseña) and
    re.search(r"\d", contraseña)):
     return True
     return False
     #Pedir al ususario que cree una contraseña
     while True:
        nueva_contraseña = input("Crea una contraseña (minimo 8 caracteres, con mayusculas, minusculas y numeros): ")

        if:
        validar_contraseña(nueva_contraseña):
        print("Contraseña creada con exito.")
        break
     else:
        print("La contraseña no cumple con los requisitos")
    
    
    
    
    def buscar_y_reemplazar(nombre_archivo, contraseña_buscar, contraseña_reemplazar, nuevo_archivo=None):
   
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        contenido_modificado = contenido.replace(contraseña_buscar, contraseña_reemplazar)
        
        archivo_salida = nuevo_archivo if nuevo_archivo else nombre_archivo
        
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido_modificado)
            
        print(f" **Se reemplazó** '{contraseña_buscar}' por '{contraseña_reemplazar}' en '{archivo_salida}'.")
    except FileNotFoundError:
        print(f" Error: El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f" Ocurrió un error: {e}")

# Ejemplo de uso:
if __name__ == "__main__":
    print("////Buscar y Reemplazar en Archivo TXT////// ")
    archivo = input("Ingresa la ruta donde tengas el archivo seguido por \su nombre.txt(ej: 'datos.txt'): ")
    buscar = input("Palabra a buscar: ")
    reemplazar = input("Palabra de reemplazo: ")
    opcion = input("¿Guardar en nuevo archivo? (s/n): ").strip().lower()
    
    nuevo_archivo = None
    if opcion == 's':
        nuevo_archivo = input("ingresa la ruta donde quieres que se guarde el archivo seguido por \su nuevo nombre.txt (ej: 'modificado.txt'): ")
    
    buscar_y_reemplazar(archivo, buscar, reemplazar, nuevo_archivo)
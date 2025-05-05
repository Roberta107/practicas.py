def validar_curp(curp):
    """Validad el formato de una CURP"""
    patron = r"^[A-Z]{4}\d{6}[HM][A-Z]{2}[A-Z]{3}\d{2}$"
    return re.match(patron, curp)is not None

    #Solicitar CURP al usuario 
    curp = input("Introducir tu CURP:").strip().upper()
    #Validad CURP
    if validar_curp(curp):
        print("CURP valida.")
    else: 
        print("CURP Iinvalida.")

def buscar_y_reemplazar(nombre_archivo, curp_buscar, curp_reemplazar, nuevo_archivo=None):
   
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        contenido_modificado = contenido.replace(curp_buscar, curp_reemplazar)
        
        archivo_salida = nuevo_archivo if nuevo_archivo else nombre_archivo
        
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido_modificado)
            
        print(f" **Se reemplazó** '{telefono_buscar}' por '{telefono_reemplazar}' en '{archivo_salida}'.")
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
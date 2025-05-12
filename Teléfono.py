def VerificarNumero(telefono):
    if len (telefono) != 13:
        return False 
        for i in range(1,2):
            if not telefono[i].isdecimal():
                return False
                if telefono[0] !="(":
                    return False
                    if telefono[3] !=")":
                        return False
                        for i in range(4,7):
                            if not telefono[i].isdecimal():
                                return False
                                if telefono[8] !="-":
                                    return False 
                                    for i in range(9,13):
                                        if not telefono[i].isdecimal():
                                            return False 
                                            return True
                                            telefono = input("Ingresa un numero de telefono")
                                            print(VerificarNumero(telefono))

    def buscar_y_reemplazar(nombre_archivo, telefono_buscar, telefono_reemplazar, nuevo_archivo=None):
   
     try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        contenido_modificado = contenido.replace(telefono_buscar, telefono_reemplazar)
        
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
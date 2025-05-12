def ordenamiento_insercion(arr):
    # Recorremos la lista desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        # Guardamos el valor actual para compararlo
        valor_actual = arr[i]
        # Iniciamos un índice para comparar con los elementos anteriores
        j = i - 1
        # Movemos los elementos mayores que el valor actual hacia la derecha
        while j >= 0 and valor_actual < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Insertamos el valor actual en su posición correcta
        arr[j + 1] = valor_actual
    return arr

def main():
    # Pedimos al usuario que ingrese los datos
    datos = input("Ingresa una lista de números separados por espacios: ")
    # Convertimos los datos a una lista de enteros
    lista = list(map(int, datos.split()))
    # Ordenamos la lista usando el método de inserción
    lista_ordenada = ordenamiento_insercion(lista)
    # Mostramos la lista ordenada
    print("Lista ordenada:", lista_ordenada)

if __name__ == "__main__":
    main()
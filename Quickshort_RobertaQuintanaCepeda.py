def quicksort(arr):
   
    if len(arr) <= 1:
        return arr
    else:
       
        pivot = arr[0]
        menores = [x for x in arr[1:] if x <= pivot]
        mayores = [x for x in arr[1:] if x > pivot]
        return quicksort(menores) + [pivot] + quicksort(mayores)

def main():
    datos = input("Ingresa una lista de números separados por espacios: ")
    lista = list(map(int, datos.split()))
    lista_ordenada = quicksort(lista)
    print("Lista ordenada:", lista_ordenada)

if __name__ == "__main__":
    main()

def m_burbuja(con):
    n = len(con)
    for i in range(n):
        aux = False
        for j in range(0, n-i-1):
            if con[j] > con[j+1]:
                con[j], con[j+1] = con[j+1], con[j]
                aux = True
        if not aux:
            break
    
lista = []
print("Ingresa los números uno por uno. Escribe 'fin' para terminar.")

while True:
    valor = input("Ingresa un número (o 'fin' para terminar): ")
    if valor.lower()== 'fin':  # Terminar si el usuario escribe 'fin'
        break
    try:
        # Convertir el valor a entero y agregarlo a la lista
        numero = int(valor)
        lista.append(numero)
    except ValueError: # Si ingresa algo que no es un numero sale error
        print("Entrada inválida. Por favor, ingresa un número válido.")

m_burbuja(lista)

print("Lista ordenada:", lista)
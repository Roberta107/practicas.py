#Basica Complete Search: Milk Pails
# Lectura de la entrada
with open("pails.in", "r") as fin:
    X, Y, M = map(int, fin.readline().split())

max_leche = 0

# Iterar sobre todas las posibles cantidades de llenados de la cubeta X
for i in range(M // X + 1):
    # Para cada i, calcular cuántas veces se puede llenar la cubeta Y
    for j in range((M - i * X) // Y + 1):
        total = i * X + j * Y
        if total <= M:
            max_leche = max(max_leche, total)

# Escribir el resultado en el archivo de salida
with open("pails.out", "w") as fout:
    fout.write(f"{max_leche}\n")
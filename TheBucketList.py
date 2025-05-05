#Simulation: The Bucket List
# Lectura de la entrada
with open("blist.in", "r") as fin:
    n = int(fin.readline())
    cows = [tuple(map(int, fin.readline().split())) for _ in range(n)]

# Inicializar un arreglo para llevar el seguimiento de las cubetas necesarias
time_buckets = [0] * 1001  # Índices de 0 a 1000

# Iterar sobre cada vaca
for s, t, b in cows:
    for time in range(s, t + 1):
        time_buckets[time] += b

# Determinar el máximo número de cubetas necesarias en cualquier unidad de tiempo
max_buckets = max(time_buckets)

# Escribir el resultado en el archivo de salida
with open("blist.out", "w") as fout:
    fout.write(f"{max_buckets}\n")
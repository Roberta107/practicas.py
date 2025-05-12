# Complete Search With Recursion: Livestock Lineup 
from itertools import permutations

# Lista de vacas en orden lexicográfico
cows = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]

# Leer las restricciones desde el archivo de entrada
with open("lineup.in", "r") as fin:
    n = int(fin.readline())
    constraints = []
    for _ in range(n):
        parts = fin.readline().strip().split()
        cow1 = parts[0]
        cow2 = parts[-1]
        constraints.append((cow1, cow2))

# Generar todas las permutaciones posibles
for perm in permutations(cows):
    valid = True
    for cow1, cow2 in constraints:
        idx1 = perm.index(cow1)
        idx2 = perm.index(cow2)
        if abs(idx1 - idx2) != 1:
            valid = False
            break
    if valid:
        # Escribir la permutación válida en el archivo de salida
        with open("lineup.out", "w") as fout:
            for cow in perm:
                fout.write(cow + "\n")
        break

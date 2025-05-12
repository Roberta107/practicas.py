def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

# Solicitar al usuario que ingrese un número válido
x = int(input("Ingrese el número para calcular su factorial: "))

# Verificar que el número sea válido
while x < 1:
    print("Error: el número debe ser un entero positivo (mayor o igual a 1).")
    x = int(input("Ingrese el número para calcular su factorial: "))
val = factorial(x)

# Mostrar el resultado
print(f"El resultado del factorial de {x} es: {val}")
# 8. Algoritmo que pide tres números al usuario y decide cuál es el mayor.
# -----------------------------------------------------------------------
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

# Comparación para encontrar el número mayor entre los tres
if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3

print(f"El número mayor es: {mayor}")
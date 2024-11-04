# 1. Algoritmo que lee un número y dice si es positivo o negativo.
# ---------------------------------------------------------------
numero = float(input("Introduce un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")  # Caso para el número 0
# 5. Algoritmo que lee dos números y los suma si alguno de ellos es positivo.
# --------------------------------------------------------------------------
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
if numero1 > 0 or numero2 > 0:
    suma = numero1 + numero2
    print(f"La suma de los números es: {suma}")  # Suma si uno de los números es positivo
else:
    print("Ninguno de los números es positivo.")  # Caso en que ambos números son no positivos
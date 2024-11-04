# 6. Algoritmo que lee dos números y los suma si ambos son negativos.
# -------------------------------------------------------------------
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
if numero1 < 0 and numero2 < 0:
    suma = numero1 + numero2
    print(f"La suma de los números es: {suma}")  # Suma si ambos números son negativos
else:
    print("Ambos números no son negativos.")  # Caso en que al menos uno no es negativo
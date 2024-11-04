# 7. Algoritmo que presenta un menú al usuario con las operaciones de suma, resta y multiplicación y realiza la operación elegida sobre dos números que también los decide el usuario.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Elige una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
opcion = int(input("Introduce el número de la operación que deseas realizar: "))

# Se piden los dos números para realizar la operación seleccionada
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Se realiza la operación seleccionada por el usuario
if opcion == 1:
    resultado = numero1 + numero2
    print(f"La suma es: {resultado}")
elif opcion == 2:
    resultado = numero1 - numero2
    print(f"La resta es: {resultado}")
elif opcion == 3:
    resultado = numero1 * numero2
    print(f"La multiplicación es: {resultado}")
else:
    print("Opción no válida.")  # Caso de opción de operación no válida
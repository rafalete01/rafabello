# 9. Algoritmo que pide tres números al usuario y los muestra ordenados de mayor a menor.
# ---------------------------------------------------------------------------------------
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

numeros = [numero1, numero2, numero3]
numeros.sort(reverse=True)  # Ordena la lista de números de mayor a menor

print(f"Los números ordenados de mayor a menor son: {numeros}")
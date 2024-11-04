# 1. Mostrar los 10 primeros números
def mostrar_10_numeros():
    i = 1
    while i <= 10:
        print(i)
        i += 1
        
        

# 2. Mostrar la suma de los 10 primeros números
def suma_10_numeros():
    i = 1
    suma = 0
    while i <= 10:
        suma += i
        i += 1
    print(f"La suma de los 10 primeros números es: {suma}")
    
    

# 3. Mostrar una serie de números desde un inicio y fin definidos por el usuario
def mostrar_serie():
    inicio = int(input("Introduce el número inicial: "))
    fin = int(input("Introduce el número final: "))
    i = inicio
    while i <= fin:
        print(i)
        i += 1



# 4. Mostrar la suma de una serie de números definidos por el usuario
def suma_serie():
    inicio = int(input("Introduce el número inicial: "))
    fin = int(input("Introduce el número final: "))
    i = inicio
    suma = 0
    while i <= fin:
        suma += i
        i += 1
    print(f"La suma de los números entre {inicio} y {fin} es: {suma}")
    
    

# 5. Mostrar la suma de los números pares entre un inicio y fin definidos por el usuario
def suma_pares():
    inicio = int(input("Introduce el número inicial: "))
    fin = int(input("Introduce el número final: "))
    suma = 0
    i = inicio
    while i <= fin:
        if i % 2 == 0:
            suma += i
        i += 1
    print(f"La suma de los números pares entre {inicio} y {fin} es: {suma}")
    
    

# 6. Calcular la media de una serie de 10 números
def media_10_numeros():
    i = 1
    suma = 0
    while i <= 10:
        numero = float(input(f"Introduce el número {i}: "))
        suma += numero
        i += 1
    media = suma / 10
    print(f"La media de los 10 números es: {media}")
    
    

# 7. Mostrar la tabla de multiplicar de un número entre 1 y 10
def tabla_multiplicar():
    numero = int(input("Introduce un número entre 1 y 10: "))
    if 1 <= numero <= 10:
        i = 1
        while i <= 10:
            print(f"{numero} x {i} = {numero * i}")
            i += 1
    else:
        print("Número fuera de rango. Debe estar entre 1 y 10.")
        
        

# 8. Calcular el factorial de un número mayor a 0
def factorial():
    numero = int(input("Introduce un número mayor que 0: "))
    if numero > 0:
        i = 1
        resultado = 1
        while i <= numero:
            resultado *= i
            i += 1
        print(f"El factorial de {numero} es: {resultado}")
    else:
        print("El número debe ser mayor que 0.")



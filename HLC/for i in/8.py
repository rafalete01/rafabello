#8 Diseñar un algoritmo que muestra el factorial de un número pedido al usuario. El número debe ser mayor de 0.

def main(args):
    
    n = int(input("introduce el numero factorial "))
    multiplicador = 1
    for i in range(1,n + 1):
        multiplicador =  multiplicador * i
    print(multiplicador)
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
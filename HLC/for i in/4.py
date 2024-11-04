#4. Diseñar un algoritmos que pida el inicio y el fin de una serie y muestre su suma.

def main(args):
    suma = 0
    inicio = int(input("introduce el numero de inicio "))
    final = int(input("introduce el numero de final "))
    
    for i in range(inicio,final):
        suma = suma + i
    print(suma)
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
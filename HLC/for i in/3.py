#3. Diseñar un algoritmo que pida el inicio y el fin de una serie y la muestre.

def main(args):
    inicio = int(input("introduce el numero de inicio "))
    final = int(input("introduce el numero de final "))
    
    for i in range(inicio,final):
        print(i)
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
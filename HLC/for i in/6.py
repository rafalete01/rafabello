#Diseñar un algoritmo que calcula la media de una serie de 10 números. 
def main(args):
    suma = 0
    inicio = int(input("introduce el numero de inicio "))
    final = int(input("introduce el numero de final "))
    
    for i in range(inicio, final):
        suma = suma + i
    resultado = suma / i
    print(resultado)
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
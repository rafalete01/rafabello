#Diseñar un algoritmo que muestre la suma de los pares que hay entre un inicio y un final definidos por el usuario
def main(args):
    suma = 0
    inicio = int(input("introduce el numero de inicio "))
    final = int(input("introduce el numero de final "))
    
    for i in range(inicio,final):
        if i%2==0:
            suma = suma + i
    print(suma)
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
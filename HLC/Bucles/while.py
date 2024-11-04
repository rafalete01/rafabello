#6. Algoritmo que lee 5 números y muestra la media aritmética.
def main(args):
    contador=0
    num2=0
    while contador<5:
        num = int(input("Introduce un número entero: "))
        num2=num+num2
        contador=contador+1
        
        print(num2)
        
        return 0
    
    
    if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))
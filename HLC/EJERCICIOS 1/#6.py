#6. Algoritmo que lee 5 números y muestra la media aritmética.
def main(args):
    num1=int(input("introduce el primer sumero"))
    num2=int(input("introduce el segundo numero"))
    num3=int(input("introduce el tercero numero"))
    num4=int(input("introduce el cuarto numero"))
    num5=int(input("introduce el quinto numero"))

    resultado=(num1+num2+num3+num3+num4+num5)/5
    print(resultado)
    
    if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))
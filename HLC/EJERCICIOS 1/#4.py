#4. Muestra por pantalla la división de dos números definidos por el usuario.

def main(args):
    num1=int(input("introduce el primer sumero"))
    num2=int(input("introduce el segundo numero"))

    resultado=num1/num2
    print(resultado)

    if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))
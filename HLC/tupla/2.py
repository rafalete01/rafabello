def main(args):
    def menu():
        print("1-suma")
        print("2-resta")
        print("3-salir")
        op=int(input("que desea hacer:"))
        return op
    operacion=menu()
    while operacion>3 or operacion==0:
        print("no has escrito una opción correcta")
        operacion=menu()
    if (operacion == 1):
        suma=int(input("que numero desea sumar "))
        suma2=int(input("que otro numero desea sumar "))
        re=suma + suma2
        print(re)
    elif (operacion == 2):
        resta=int(input("que numero desea restar "))
        resta2=int(input("que otro numero desea restar "))
        re=resta - resta2
        print(re)
    else :
        res=int(input)("¿desea salir? (yes/no)")
        if res == "yes":
            print("has salido del menu")
        else:
            operacion=menu()
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
def main(args):
    asi1=input("Dime una asignatura ")
    asi2=input("Dime una asignatura ")
    asi3=input("Dime una asignatura ")
    asi4=input("Dime una asignatura ")
    asi5=input("Dime una asignatura ")
    lista = [asi1, asi2, asi3, asi4, asi5]
    lista.sort()
    print(lista)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
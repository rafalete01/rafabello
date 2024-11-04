#. Diseñar un algoritmo que muestre la tabla de multiplicar de un número que pide al usuario y que debe estar entre 1 y 10 (ambos inclusive).
def main(args):
    
    n = int(input("introduce el numero multiplicador "))
   
    for i in range(11):
        multiplicador = n * i
        print("EL RESULTADO DE ",i,"x",n,"=",multiplicador)
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
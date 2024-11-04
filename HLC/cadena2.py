# Contar los espacios en blanco de una cadena de caracteres introducida por teclado.

def main(args):
	contador=0
	frase = input("Introduzca la frase para contar los espacios: ")
	for i in range(len(frase)):
		if frase[i] == " ":
			contador = contador + 1
	print(contador)
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

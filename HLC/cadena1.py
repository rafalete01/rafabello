def main(args):
	frase = input("Escribe la frase que desee: ")
	for letra in frase:
		print(letra)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

def sacarip(usuario):
    return(usuario[3])
            
            
def main(args):
    usuario = ("rafa", "asir", "192.168.8.16","rafa@bello.com")
    ip=sacarip(usuario)
    print(ip)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
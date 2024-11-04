def main(args):
    cliente = (("mauel", "345453443","pato"),("pepe", "685417727","pata"))
    for i in range(len(cliente)):
        user2=cliente[i]
        print(" ")
        for j in range(len(user2)):
            print(user2[j])
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
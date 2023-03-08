def busca():
    print("Digite a palavra a ser procurada: ")
    args = input().split()
    caractere = str(args[0])
    print("Digite a string a ser procurado: ")
    args = input()
    string = str(args)

    if caractere not in string:
        print("A frase não tem " + caractere)
    else:
        print("A frase tem " + caractere)
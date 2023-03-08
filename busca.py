def busca():
    lista = [1,2,3,4,5]
    print("Digite o caracter a ser procurado: ")
    args = input().split()
    caractere = str(args[0])
    string = str(args[1])
    if caractere not in string:
        print("A frase não tem " + caractere)
    else:
        print("A frase tem " + caractere)
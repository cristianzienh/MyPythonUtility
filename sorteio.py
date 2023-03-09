import random

def sorteionumero():
    inicio = int(input("Informe o valor inicial do intervalo: "))
    fim = int(input("Informe o valor final do intervalo: "))


    numero_aleatorio = random.randint(inicio, fim)


    print(f"O número aleatório gerado foi: {numero_aleatorio}")
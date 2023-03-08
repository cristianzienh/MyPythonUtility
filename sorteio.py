import random

numero = int(input("Escolha a opção 7 para gerar um numero aleatorio dentro de um intervalo"))

if numero == 7:

  inicio = int(input("Informe o valor inicial do intervalo: "))
fim = int(input("Informe o valor final do intervalo: "))


numero_aleatorio = random.randint(inicio, fim)


print(f"O número aleatório gerado foi: {numero_aleatorio}")
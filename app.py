import sys
from calculadora import *
#Seleciona função
#1 - Calculadora
#2 - Inverte string
#3 - Ordena caracters da string
#4 - Retorna dia da semana para data
#5 - Detecta palíndromos
#6 - Retorna se é número é par ou impar
#7 - Sorteia um número aleatório para um dado intervalo numérico
#8 - Verifica se palavra/caracter existe na string
#9 - Imprime o número Pi com x casas decimais 
#Enter - Sair


import random

print("informe a funcão:\n7 - Calculadora" + 
      "\nEnter - Sair")
funcao = input()
if (funcao == ""):
    calculate()
elif (funcao == ""): 
    pass
else:
    print("Função não implementada!")


inicio = int(input("Informe o valor inicial do intervalo: "))
fim = int(input("Informe o valor final do intervalo: "))


numero_aleatorio = random.randint(inicio, fim)


print(f"O número aleatório gerado foi: {numero_aleatorio}")




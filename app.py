
import sys
from calculadora import *
from busca import *
from pi import *
from parouimpar import *
from sorteio import *
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

print("informe a funcão:\n7 - Calculadora" +)
print("informe a funcão:\n1 - Calculadora" + "\n8 - Busca" + "\n9 - Pi" +
      "\n5 - Palíndromo" + 
      "\nEnter - Sair")
funcao = input()
if (funcao == ""):
    calculate()
elif (funcao == "5"): 
    palindromo()
elif (funcao == "8"):
    busca()
elif (funcao == "9"):
    piFunction()
elif (funcao =="6"):
    parouimpar()
elif (funcao == ""): 
    pass
else:

  





import sys
from calculadora import *
from po import *
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
print("informe a funcão:\n1 - Calculadora" + "\n3 - Ordena caracters da string"
      "\nEnter - Sair")
funcao = input()
if (funcao == "1"):
    calculate()
elif (funcao == "3"): 
    ordena()
else:
    print("Função não implementada!")
#Encerra   
print("Bye!")




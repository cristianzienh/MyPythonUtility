import sys
from calculadora import *
from busca import *
from pi import *
from parouimpar import *
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
<<<<<<< HEAD


import random

print("informe a funcão:\n7 - Calculadora" + 
=======
print("informe a funcão:\n1 - Calculadora" + "\n8 - Busca" + "\n9 - Pi" +
      "\n5 - Palíndromo" + 
>>>>>>> 014e07ca7da0d750f770b909ade9e3d7461a5d26
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
<<<<<<< HEAD
    print("Função não implementada!")


inicio = int(input("Informe o valor inicial do intervalo: "))
fim = int(input("Informe o valor final do intervalo: "))


numero_aleatorio = random.randint(inicio, fim)


print(f"O número aleatório gerado foi: {numero_aleatorio}")

=======
    print("Função não implementada!") 
print("Bye!")
>>>>>>> 014e07ca7da0d750f770b909ade9e3d7461a5d26





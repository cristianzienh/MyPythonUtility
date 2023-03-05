import sys
from calculadora import *

print("informe a funcão:\n1-Calculadora\n9-Sair")
#Seleciona função
funcao = input()
if (funcao == "1"):
    calculate()
elif (funcao == "9"): 
    pass
else:
    print("Função não implementada!")
#Encerra   
print("Bye!")



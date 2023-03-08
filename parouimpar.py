def parouimpar(): 
    numero = int(input("digite um numero:"))
    resultado = numero % 2
    if resultado == 0:
        print("0 numero {} é par" .format(numero))
    else:
        print("0 numero {} é impar" .format(numero))
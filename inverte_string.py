def inverte_string(texto):
    return texto[::-1]

texto_original = (input("Digite a String: "))
texto_invertido = inverte_string(texto_original)

print("-------------------------------")
print("Texto original: ", texto_original)
print("Texto invertido: ", texto_invertido)
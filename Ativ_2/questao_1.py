# 1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

def filtrar_impares(lista):
    return [x for x in lista if x % 2 != 0]

entrada = input("Digite os números separados por espaço ou vírgula: ")
#Substitui vírgulas por espaços e divide a string
numeros = [int(n) for n in entrada.replace(',', ' ').split()]
resultado = filtrar_impares(numeros)
print(f"Os números ímpares digitados são: {resultado}")

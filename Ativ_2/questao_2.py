# 2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(lista):
    return [x for x in lista if eh_primo(x)]

try:
    entrada = input("Digite uma lista de números separados por espaço: ")
    numeros = [int(n) for n in entrada.split()]
    resultado = filtrar_primos(numeros)
    
    print(f"\nDos números digitados, os primos são: {resultado}")

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros separados por espaços.")

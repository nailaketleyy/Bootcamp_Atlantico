# 3. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.

def filtrar_exclusivos(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    
    resultado = list(set1 ^ set2)
    return resultado

try:
    entrada1 = input("Digite os números da primeira lista (separados por espaço): ")
    entrada2 = input("Digite os números da segunda lista (separados por espaço): ")

    lista1 = [int(x) for x in entrada1.split()]
    lista2 = [int(x) for x in entrada2.split()]

    resultado = filtrar_exclusivos(lista1, lista2)    
    print(f"\nElementos presentes em apenas uma das listas: {resultado}")

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros separados por espaços.")

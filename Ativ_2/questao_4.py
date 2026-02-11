# 4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

def segundo_maior(lista):
    numeros_unicos = list(set(lista))    
    if len(numeros_unicos) < 2:
        return None
  
    numeros_unicos.sort() 
    return numeros_unicos[-2]

try:
    entrada = input("Digite uma lista de números separados por espaço: ")
    numeros = [int(x) for x in entrada.split()]
    resultado = segundo_maior(numeros)
    if resultado is not None:
        print(f"O segundo maior valor é: {resultado}")
    else:
        print("A lista precisa de pelo menos dois números diferentes.")

except ValueError:
    print("Erro: Digite apenas números inteiros.")

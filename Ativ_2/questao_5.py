# 5. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

def ordenar_por_nome(lista_pessoas):
    return sorted(lista_pessoas, key=lambda p: p[0])

pessoas = []
print("Digite os dados das pessoas (ou 'sair' para finalizar):")

while True:
    nome = input("Nome: ")
    if nome.lower() == 'sair':
        break
    try:
        idade = int(input(f"Idade de {nome}: "))
        pessoas.append((nome, idade))
    except ValueError:
        print("Idade inválida! Tente novamente.")

resultado = ordenar_por_nome(pessoas)
print("\nLista ordenada por nome:")
for p in resultado:
    print(f"- {p[0]}, {p[1]} anos")

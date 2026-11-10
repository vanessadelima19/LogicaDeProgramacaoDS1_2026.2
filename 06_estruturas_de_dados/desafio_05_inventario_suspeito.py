"""
DESAFIO 05: O INVENTÁRIO SUSPEITO DO LABORATÓRIO
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
Elimine duplicatas usando conjuntos (set) e previna o erro KeyError em dicionários
usando o método .get().

SUA MISSÃO:
1. Obtenha a lista de itens únicos a partir de uma lista com duplicatas.
2. Consulte chaves no dicionário de forma segura sem quebrar o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:
itens = "Mouse", "Teclado", "Monitor", "Mouse"
itens_unicos = set(itens)
print("Itens_unicos:", itens_unicos)
inventario = {
    "Mouse": 1,
    "Teclado": 6,
    "Monitor": 9
}
consulta = input("Digite o nome do item: ")
quantidade = inventario.get(consulta,"Item não encontrado")
print("quantidade:", quantidade)
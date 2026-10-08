"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo
def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    preco_com_desconto = preco_base - (preco_base * taxa_desc)
    preco_final = preco_com_desconto + (preco_com_desconto * taxa_imp)
    return preco_final


def exibir_relatorio_item(numero_item, preco_final):
    print(f"Item {numero_item}: R$ {preco_final:.2f}")

#Teste das funções refatoradas
preco_final = calcular_preco_final(100, 0.1, 0.2)
exibir_relatorio_item(1, preco_final)

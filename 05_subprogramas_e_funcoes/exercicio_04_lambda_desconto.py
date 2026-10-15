"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo: 
desconto = lambda preco : preco * 0.85
print(desconto(100))  # Deve imprimir 85.0
print(desconto(200))  # Deve imprimir 170.0
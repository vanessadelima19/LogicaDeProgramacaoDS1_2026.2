"""
EXERCÍCIO 04: Casting de Dados e Idade em 2026
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba do usuário o ano de nascimento como texto (str).
Converta essa entrada para inteiro (int) utilizando o conceito de casting
e calcule a idade que a pessoa completará até o final de 2026.
Imprima a idade calculada com uma mensagem personalizada.
"""

# TODO: Desenvolva o algoritmo abaixo:
from tarfile import data_filter
data = str(input("Digite seu ano de nascimento: "))
nome = str(input("Digite seu nome: "))
nascimento = int(data)
idade_final = 2026-nascimento
print(f"Olá {nome}, até o final de 2026 você terá: {idade_final} anos")

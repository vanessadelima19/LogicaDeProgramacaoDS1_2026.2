"""
EXERCÍCIO 03: Fórmula de Bhaskara 
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
if a == 0:
    print("Impossivel calcular")
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Impossivel calcular")
    else:
        r1 = (-b + delta**0.5) / (2 * a)
        r2 = (-b - delta**0.5) / (2 * a)
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")
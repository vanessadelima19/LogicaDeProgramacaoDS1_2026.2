"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo
Distância = float(input("Digite a distância percorrida(km): "))
Combustivel = float(input("Digite o total de combustível gasto(litros): "))
Consumo = Distância / Combustivel
print(f"O consumo médio da motocicleta é: {Consumo:.2f} Km/L")

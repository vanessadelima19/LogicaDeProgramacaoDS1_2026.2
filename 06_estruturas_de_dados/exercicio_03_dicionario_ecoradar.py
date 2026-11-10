"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:

dicionario = {
    1: "Designer",
    2: "Programador",
    2: "Analista"
    }
matricula =int(input("Qual a sua matricula? "))
if matricula in dicionario:
    print("Cargo:", dicionario[matricula])
else:
    print("Matricula não encontrada.")
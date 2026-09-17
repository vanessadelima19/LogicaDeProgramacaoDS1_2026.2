"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
Nota1 =float(input("Digite sua primeira nota: "))
Nota2 =float(input("Digite sua segunda nota: "))
Nota3 =float(input("Digite susa terceira nota: "))
calc1=Nota1*2
calc2=Nota2*3
calc3=Nota3*5
soma_calc=(calc1+calc2+calc3)
média= soma_calc/(2+3+5)
print("A media final é de: ", média)

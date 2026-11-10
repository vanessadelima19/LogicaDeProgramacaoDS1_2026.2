"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma matriz com 3 alunos [nome, nota1, nota2].
Percorra a matriz, calcule a média de cada um e exiba:
"Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]"
(Critério: Média >= 6.0 aprovado).
"""

# TODO: Desenvolva o algoritmo abaixo:
alunos = [
    ["Ana", 8.0, 7.0],
    ["Luiz", 6.0, 5.0],
    ["Clara", 9.0, 10.0]
]
for aluno in alunos:
    media = (aluno[1] + aluno[2]) / 2
    if media >=6:
        situacao = "Aprovado"
    else:
        situacao = "Prova Final"
print("Aluno:", aluno[0], 
    "| Média:", media,
    "| Situação:", situacao)

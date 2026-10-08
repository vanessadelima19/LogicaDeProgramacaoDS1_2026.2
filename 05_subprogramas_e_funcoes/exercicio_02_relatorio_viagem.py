"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    custo_transporte = (distancia_km / consumo_kml) * preco_combustivel
    return custo_transporte

def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    custo_alimentacao = qtd_pessoas * dias * diaria_alimentacao
    return custo_alimentacao

# Programa principal
distancia = float(input("Digite a distância da viagem em km: "))
consumo = float(input("Digite o consumo do veículo em km/l: "))
preco_combustivel = float(input("Digite o preço do combustível em R$: "))
qtd_pessoas = int(input("Digite o número de pessoas na viagem: "))
dias = int(input("Digite o número de dias da viagem: "))
diaria = float(input("Digite o valor da diária de alimentação em R$: "))

custo_transporte = calcular_custo_transporte(distancia, consumo, preco_combustivel)
custo_alimentacao = calcular_custo_alimentacao(qtd_pessoas, dias, diaria)

print(f"Custo total da viagem: R$ {custo_transporte + custo_alimentacao:.2f}")
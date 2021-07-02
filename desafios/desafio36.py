"""DESAFIO 36"""
casa = float(input('Qual o valor do imóvel desejado? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
ano = int(input('Em quantos anos deseja financiar a casa? '))

salarioc = casa / (ano*12)
salarios = salario * 0.3

if salarioc < salarios:
    print('\nPARABÉNS, seu financiamento foi provado.\nA casa no valor de R${:.2f} reais,\nserá financiado em {} meses,com parcelas de R${:.2f} reais ' .format(casa, ano*12, salarioc))
else:
    print('\nFINANCIAMENTO NEGADO, no momento não foi possível financiar seu imóvel')

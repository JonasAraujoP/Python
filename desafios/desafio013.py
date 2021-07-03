"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento."""

salario = float(input('Qual o salário do funcionário? R$ '))
novo = salario * 1.15
print(f'O funcionário ganhava R${salario:.2f} reais, com o aumento de 15%, passa a receber R${novo:.2f} reais')
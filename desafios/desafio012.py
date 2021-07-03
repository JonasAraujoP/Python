"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

valor = float(input('Qual o valor do produto? R$ '))
des = valor * 0.95
print(f'O produto que custava R$ {valor:.2f} reais, com o desconte de 5% sai por R$ {des:.2f} reais')
"""Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado."""

print('-=-'*15)
dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km rodado? '))

total = (km * 0.15) + (dias * 60)

print('-=-'*15)
print(f'O valor total a pagar é de R${total:.2f} reais')
print('-=-'*15)

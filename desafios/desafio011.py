"""
Faça um programa que leia a largura e a altura de uma parece em metros.
Calcule a sua área e a quantidade de tinta necessária para pinta-lá.
Sabendo que a cada litro de tinta, pinta uma área de 2m²
"""

print('-=-'*15)
larg = float(input('Qual a largura em metros da parede? '))
alt = float(input('Qual a altura em metros da parece? '))

area = larg * alt
tinta = area / 2

print('-=-'*15)
print(f'Para pintar a parede tem a dimensões de {larg}m x {alt}m, tendo uma área de {area:.2f}m²')
print(f'para pintar sua parede é necessário {tinta:.2f}l de tinta.')
print('-=-'*15)
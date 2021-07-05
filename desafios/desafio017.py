"""Faça um programa que leia o comprimento dos catetos, e calcule e mostre o comprimento da hipotenusa."""

print('-=-'*15)
ca = float(input('Qual o comprimento do Cateto Adjacente em cm?  '))
co = float(input('Qual o comprimento do Cateto Oposto me cm? '))
hip = ((ca**2) + (co**2))**0.5
print('-=-'*15)
print(f'Com os catetos medindo {ca}cm e {co}cm, a hipotenusa vai valer {hip:.1f}cm')


""" #segundo modelo usando a biblioteca MATH

from math import hypot

print('-=-'*15)
ca = float(input('Qual o comprimento do Cateto Adjacente em cm?  '))
co = float(input('Qual o comprimento do Cateto Oposto me cm? '))
hip = hypot(ca, co)
print('-=-'*15)
print(f'Com os catetos medindo {ca}cm e {co}cm, a hipotenusa vai valer {hip:.2f}cm')
"""


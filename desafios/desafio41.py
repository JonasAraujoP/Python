"""DESAFIO 41"""
from datetime import date
print('-=-'*9)
nome = str(input('Qual seu nome: ')) .upper() .strip()
nasc = int(input('Em qual ano você nasceu? '))
data = date.today().year
idade = data - nasc
print('-=-'*9)
if idade <= 9:
    print('Nome: ', nome)
    print('Idade: ', idade)
    print('Categoria: MIRIM')
elif idade >9 and idade <=14:
    print('Nome: ', nome)
    print('Idade: ', idade)
    print('Categoria: INFANTÍL')
elif idade >14 and idade <= 19:
    print('Nome: ', nome)
    print('Idade: ', idade)
    print('Categoria: JUVENÍL')
elif idade > 19 and idade <= 20:
    print('Nome: ', nome)
    print('Idade: ', idade)
    print('Categoria: SÊNIOR')
else:
    print('Nome: ', nome)
    print('Idade: ', idade)
    print('Categoria: MASTER')
print('-=-'*9)

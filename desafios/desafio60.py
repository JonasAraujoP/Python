fa = int(input('\nQual o número a calcular seu FATORIAL: '))
produto = 1
cont = 0
while fa != 0:
    produto = fa*produto
    fa +=-1
    cont += +1
print('O fatorial de {} é {}'.format( cont, produto))

#CÓDIGO DO PROFESSOR
"""from math import factorial
n = int(input('Digite o número a calcular eu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))"""

#CÓDIGO DO PROFESSOR
"""n = int(input('Digite o número a a calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! '.format(n),end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))"""


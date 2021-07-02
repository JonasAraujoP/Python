from random import randint
from time import sleep

numeros = list()


def sorteia():
    for c in range(1, 6):
        numeros.append(randint(1, 10))

    print('-=-'*14)
    print('         SORTEANDO 5 NÚMEROS')
    print('-=-'*14)
    print('Os números sorteados foram: \033[31m', end=" ")

    for c in numeros:
        sleep(0.25)
        print(c, end=' ')
    print()
    print('\033[m-=-'*14)


def somapar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores pares da lista \033[33m{numeros}\033[m é \033[32m{soma}\033[m')


sorteia()
somapar()

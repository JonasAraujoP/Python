from random import randint
from time import sleep
sorteio = []
print('==='*15)
print('{:^44}'.format('JOGO DA MEGA SENA'))
print('==='*15)
n = int(input('Quantos sorteio você deseja calcular? '))
for s in range(0, n):
    while len(sorteio) != 6:
        m = randint(1, 60)
        if m not in sorteio:
            sorteio.append(m)
    print('-=-'*15)
    sorteio.sort()
    print(f'\033[33mJogo {s+1}:\033[m \033[32m{sorteio}\033[m')
    sorteio.clear()
    sleep(0.5)
print('-=-'*15)
print('\033[34m{:^45}\033[m'.format('Boa sorte!!'))

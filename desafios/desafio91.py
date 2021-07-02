from random import randint
from time import sleep
from operator import itemgetter

print('-=-'*10)
print(f'{"SORTEIO DE DADOS":^30}')
print('-=-'*10)

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = dict()

for k, v in jogo.items():
    print(f'{k}: tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=-'*10)
print(f'{">> RANKING <<":^30}')
print('-=-'*10)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]}: com {v[1]} ')
    sleep(1)
print('-=-'*10)

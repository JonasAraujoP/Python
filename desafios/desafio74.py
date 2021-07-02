from random import randint
t = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('-='*17)
print(f'Sorteados: {t[0]}, {t[1]}, {t[2]}, {t[3]}, {t[4]}')
print(f'Ordem crescente é: {sorted(t)}')
maior = menor = t[0]
for c in t:
    if c == 0:
        menor = maior = c
    if c <= menor:
        menor = c
    if c > maior:
        maior = c
#CÓDIGO DO PROFESSOR
#print(f'Menor: {min(t)} =-=-= Maior: {max(t)}')
print(f'Menor: {menor}\nMaior: {maior}')
print('-='*17)

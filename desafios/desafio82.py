l = []
pares = list()
impares = list()
while True:
    l.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()
    if resp == 'N':
        break
for c in l:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'Os valores digitados foram -> {l}')
print(f'Os valores \033[32mpares\033[m digitados foram -> \033[33m{pares}\033[m')
print(f'Os valores \033[32mímpares\033[m digitados foram -> \033[33m{impares}\033[m')
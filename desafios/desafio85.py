n = 0
pares = []
impares = []
geral = []
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}° valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
geral = pares + impares
print(f'Lstas dos pares: {pares}')
print(f'Lista dos Ímpares: {impares}')

""" #CÓDIGO DO PROFESSOR
n = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
print('-=-'*12)
n[0].sort()
n[1].sort()
print(f'Todos os valores pares são {n[0]}')
print(f'Todos os valores ímpares são {n[1]}')
"""
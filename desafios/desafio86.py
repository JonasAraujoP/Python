n = []
cont = 0
for c in range(1, 10):
    n.append(int(input(f'Digite o {c}° Valor: ')))
print('-=-'*12)
for c in n:
    print(f'[{c:^5}]', end=' ')
    cont += 1
    if cont == 3:
        print()
        cont = 0
print('-=-'*12)
print('fim')

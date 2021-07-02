n = []
cont = ter = soma = seg = par = maior = 0
for c in range(1, 10):
    n.append(int(input(f'Digite o {c}° Valor: ')))
print('-=-'*12)
for c in n:
    print(f'[{c:^5}]', end=' ')
    cont += 1
    ter += 1
    if cont == 3:
        print()
        cont = 0
    if c % 2 == 0:
        par += c
    if ter == 4:
        maior = c
    if ter > 4 and ter == 6:
        if c > maior:
            maior = c
    if ter >= 7:
        soma += c
    if ter == 3 or ter == 6 or ter == 9:
        seg += c
print()
print('-=-'*12)
print(f'A soma de todos os valores pares é {par}')
print(f'A soma dos valores da 3° coluna é {seg}')
print(f'O maior valor da 2° linha é {maior}')


print('fim')

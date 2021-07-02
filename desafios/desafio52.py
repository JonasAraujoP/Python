div = 0
n = int(input('\nDigite um número inteiro: '))
for c in range(1, n+1):
    if n % c == 0:
        #print('\033[32m', end='')      CÓDIGO DO PROFESSOR
        div = div + 1
        #print('\033[31m', end='')      CÓDIGO DO PROFESSOR
if div == 2:
    print('\nO número {} foi dividido por {} números.'.format(n, div))
    print('O número {} é primo'.format(n))
else:
    print('\nO número {} foi dividido por {} números.'.format(n, div))
    print('O número {} não é primo.'.format(n))

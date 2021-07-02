s = 0
n = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        n = n + 1
print('\nForam somados {} números!'.format(n))
print('A soma dos números ímpares no intervalo de 1 a 500 é: ', s)

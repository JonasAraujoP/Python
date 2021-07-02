c = n = total = 0
while n != 999:
    n = int(input('Digite um número: '))
    c += 1
    total += n
    if n == 999:
        c -= 1
        total -= 999
print('Foram digitados {} números.'.format(c))
print('A soma dos valores digitados é {}'.format(total))
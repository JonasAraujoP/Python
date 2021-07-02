c = n = total = 0
n = int(input('Digite um número: '))
while n != 999:
    c += 1
    total += n
    n = int(input('Digite um número: '))
print('Foram digitados {} números.'.format(c))
print('A soma dos valores digitados é {}'.format(total))
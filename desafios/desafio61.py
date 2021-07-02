print('-=-'*10)
p = int(input('Informe o 1° termo da PA: '))
r = int(input('Razão da PA: '))
decimo = p + (11-1) * r
while p != (decimo+r):
    print(p, end=' -> ')
    p += r
print('FIM')
print('-=-'*10)
print('Saindo do programa')

#CÓDIGO DO PROFESSOR
"""n = int(input('Informe o 1° TERMO: '))
r = int(input('Informe a RAZÃO: '))
termo = n
cont = 1
while cont <= 10:
    print('{}'.format(termo), end='')
    cont += 1
    termo += r
print('fim')"""
"""SEQUÊNCIA FIBONACCI"""
n = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
t3 = 0
print('{} -> {}'.format(t1, t2), end=' -> ')
c = 2
while c < n:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    c += 1
print('fim')

"""n = int(input('Quantos termo você quer mostrar? '))
cont = 0
extra = 0
while cont <= n:
    print(cont, end=', ')
    cont += 1
    if cont == 1:
        print(cont, end=', ')
    elif cont == 3:
        print(cont, end=', ')
        cont += 2
print('FIM')"""

"""print('-=-'*10)
res = False
p = int(input('Informe o 1° termo da PA: '))
r = int(input('Razão da PA: '))
decimo = p + (10-1) * r
per = 'N'
mais = 0
cont = 0
while p != (decimo+r):
    print(p, end=' -> ')
    p += r
    cont += +1
while not res:
    per = str(input('Quer continuar [S/N]? ')).upper().strip()
    if per == 'S':
        mais = int(input('Quantos termos a mais desejar calcular? '))
        print('-=-'*10)
        print('Os novos termos são:')
        decimo = p + ((mais +1)-1)*r
        while p <= (decimo-1):
            print(p, end=' -> ')
            p += r
            cont += +1
    elif per == 'N':
        res = True
        print('-=-'*10)
        print('Sua progressaõ foi finalizada com {} termos.'.format(cont))
print('Finalizando')
print('\nSaindo do programa')"""

#CÓDIGO DO PROFESSOR
"""n = int(input('Informe o 1° TERMO: '))
r = int(input('Informe a RAZÃO: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' - > ')
        cont += 1
        termo += r
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Sua progressão foi finalizada mostrando {} termos.'.format(total))
print('\nfim')"""
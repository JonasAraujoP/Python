def cal(a, b):
    print(f'\nMostrando o fatorail de {a}:')
    print('-=-'*12)
    cont = 1
    for c in range(0, a):

        if b == 1:
            print(a, end=' ')
            if a != 1:
                print('x ', end='')
            else:
                print(f'= {cont}', end='')
        cont *= a
        a -= 1
    if show == 2:
        print(f'O fatorial de {fat} = {cont}')


fat = int(input('Deseja calcular o fatorial de qual número? '))
show = int(input('\nDigite:\n[1] - Para mostrar o calculo.\n[2] - Para mostrar apenas o resultado. '))

cal(fat, show)


"""
#CÓDIGO DO PROFESSOR
def fatorial(x, show=False):
    cont = 1
    for c in range(x, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        cont *= c
    return cont


print(fatorial(5, True))"""
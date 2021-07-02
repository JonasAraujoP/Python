from random import randint
print('\033[33m=-=\033[m'*12)
print('JOGO DO PAR OU ÍMPAR')
n = 0
total = 0
derrota = False
resultado = ''
vitoria = 0
while derrota == False:
    print('\033[33m=-=\033[m'*12)
    n = int(input('Digite um número: '))
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('Escolha: Par ou Ímpar [P/I] ')).upper().strip()[0]
    lista = randint(1, 10)
    total = lista + n
    print('\033[33m=-=\033[m'*12)
    if total % 2 == 0 and jogador == 'P':
        resultado = 'Par'
        print('\033[32mJOGADOR VENCEU\033[m')
        print(f'Você jogou {n:.>8}\nSkynet jogou {lista:.>6}\nTotal de {total:.>10}\nDeu: {resultado:.>16}')
        vitoria += 1
    elif total % 2 == 1 and jogador == 'I':
        resultado = 'Ímpar'
        print('\033[32mJOGADOR VENCEU\033[m')
        print(f'Você jogou {n:.>8}\nSkynet jogou {lista:.>6}\nTotal de {total:.>10}\nDeu: {resultado:.>16}')
        vitoria += 1
    elif total % 2 == 1 and jogador == 'P':
        resultado = 'Ímpar'
        print('\033[31mSKYNET VENCEU\033[m')
        print(f'Você jogou {n:.>8}\nSkynet jogou {lista:.>6}\nTotal de {total:.>10}\nDeu: {resultado:.>16}')
        derrota = True
    elif total % 2 == 0 and jogador == 'I':
        resultado = 'Par'
        print('\033[31mSKYNET VENCEU\033[m')
        print(f'Você jogou {n:.>8}\nSkynet jogou {lista:.>6}\nTotal de {total:.>10}\nDeu: {resultado:.>16}')
        derrota = True
print('\033[33m=-=\033[m'*12)
print('\033[31mGAME OVER\033[m',end=' - ')
print(f'Você ganhou {vitoria} seguida.')
print('\033[33m=-=\033[m'*12)
print('Fim de Jogo')
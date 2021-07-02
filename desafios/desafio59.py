from time import sleep
print('-=-' * 11)
n1 = int(input('Insira 1° valor: '))
n2 = int(input('Insira 2° valor: '))
escolha = 0
while escolha != 5:
    print('-=-' * 11)
    print("""\033[33mMENU OPÇÔES\033[m
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa """)
    print('-=-' * 11)
    escolha = int(input('Qual sua escolha? '))
    print('-=-'*11)
    if escolha == 1:
        print('\033[34mOPÇÃO: [1] SOMA\033[m')
        print('Valor 1 = ', n1)
        print('Valor 2 = ', n2)
        print('Soma =', n1+n2)
        sleep(0.5)
    elif escolha == 2:
        print('\033[34mOPÇÃO:  [2] MULTIPLICAÇÃO\033[m')
        print('Valor 1: ', n1)
        print('Valor 2: ', n2)
        print('Multiplicação =', n1*n2)
        sleep(0.5)
    elif escolha == 3:
        print('\033[34mOPÇÃO [3] MAIOR\033[m')
        print('Valor 1: ', n1)
        print('Valor 2: ', n2)
        if n1 > n2:
            print('O maior valor é', n1)
            sleep(0.5)
        elif n2 > n1:
            print('O maior valor é', n2)
            sleep(0.5)
        else:
            print('Os valores são iguais.')
            sleep(0.5)
    elif escolha == 4:
        escolha = 4
        print('\033[34mOPÇÃO [4] NOVOS NÚMEROS\033[m')
        print('Carregando...')
        sleep(1)
        print('Informe novos valores.')
        n1 = int(input('Insira 1° valor: '))
        n2 = int(input('Insira 2° valor: '))
    elif escolha == 5:
        print('\nSaindo do programa...')
        sleep(1)
        print('\nem 3', end=' ')
        sleep(1)
        print('2', end=' ')
        sleep(1)
        print('1')
        sleep(1)
    else:
        print('\033[31mOpção inválida\033[m, tente novamente.')
print('\nFIM')

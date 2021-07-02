def perg(x):
    print(f'\033[41m')
    help(x)


while True:
    s = ''
    print('\033[42m-=-'*12)
    print(f'{"Sistema do PyHelp":^35}')
    print('-=-'*12)
    print('\033[mDigite "FIM" para sair do programa')
    resp = input('\033[mFunção ou Biblioteca >> ').lower()

    if resp == 'fim':

        print('\033[44m-=-'*14)
        print('Finalizando o programa, volte sempre!!')
        print('-=-'*14)

        break
    perg(resp)


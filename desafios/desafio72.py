valor = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
         'dezoito', 'dezenove', 'vinte')
resp = False
continuar = ''
print('-=-'*12)
while resp == False:
    escolha = int(input('Escolha um número entre 0 e 20: '))
    if escolha >= 0 and escolha <= 20:
        print(f'Você digitou o número \033[34m{valor[escolha].upper()}\033[m')
        print('-=-' * 12)
        continuar = str(input('Quer continuar [S/N]? ')).upper().strip()
        if continuar == 'N':
            resp = True
    else:
        print('Opção inválida')
        print('-=-' * 12)
print('-=-'*12)
print('FIM')
from random import randint
print('\033[33m-=-\033[m'*21)
print(' Skynet vai pensar em um número entre 0 e 10. Tente adivinhar.')
print('\033[33m-=-\033[m'*21)
num = 11
cont = 0
lista = randint(0, 10)
while num != lista:
    num = int(input('\033[34mEm que número eu pensei?\033[m '))
    cont += + 1
    if lista > num:
        print('\033[33mMais, tente novamente!\033[m')
    elif num != lista and lista < num:
        print('\033[33mMenos, tente novamente!\033[m')
print('\033[33m-=-\033[m'*9)
print('Skynet pensou no número:', lista)
print('Palpites feito:', cont)
print('\nFIM')
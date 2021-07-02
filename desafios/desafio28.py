from random import randint
print('\033[33m-=-\033[m'*18)
print(' Vou pensar em um número entre 0 e 5. Tente adivinhar.')
print('\033[33m-=-\033[m'*18)
num = (int(input('Em que número eu pensei? ')))
lista = randint(0, 5)
if num == lista:
    print('PARABÉNS, você acertou.')
    print('Skynet pensou no {} e você escolheu {}'.format(lista, num))
else:
    print('VOCÊ ERROU, tente novamente.')
    print("""Skynet pensou no {} e você escolheu {}""".format(lista, num))

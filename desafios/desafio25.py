import random
print('\033[33m-=-\033[m'*11)
print(' >>>>> JOGO DA ADIVINHAÇÃO <<<<<')
print('\033[33m-=-\033[m'*11)
print('Entre 0 a 3, que número estou pensando ??')
num = int(input('Qual o seu palpite? '))
lista = [0, 1,2, 3]
lista = random.choice(lista)
print('\033[33m-=-\033[m'*11)
print('Você escolheu: ', num)
print('Skynet escolheu: ',lista)
print('\033[33m-=-\033[m'*11)
if num == lista:
    print('Parabéns, você acertou!')
else:
    print('Errou, tente novamente!')

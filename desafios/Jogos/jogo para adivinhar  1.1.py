from random import randint

cont = perdas = y = z = 0
pontos = 1000

print('\033[33m**' * 30)

while True:
    x = int(input('\033[35mQual nível de dificuldade você deseja jogar?'
                  '\nNível [1] - 20 tentativas'
                  '\nNível [2] - 10 tentativas'
                  '\nNível [3] -  5 tentativas\033[m'
                  f'\033[33m\n{"**"*30}\033[m'
                  '\nInforme a opção desejada: '))

    if x == 1 or x == 2 or x == 3:
        break
    else:
        print(f'\033[31mOpção inválida, tente novamente\033[m')
        print('\033[33m**' * 30)


if x == 3:
    y = 5
    z = 10
    numero_secreto = randint(1, 10)

if x == 2:
    y = 10
    z = 20
    numero_secreto = randint(1, 20)

if x == 1:
    y = 20
    z = 100
    numero_secreto = randint(1, 100)

print('\033[33m**\033[m' * 30)
print(f'Escolhi um número entre 1 e {z}, tente adivinhar!!'.center(30))

for c in range(1, y+1):
    print('\033[33m**\033[m' * 30)
    chute = int(input('\033[mFaça seu chute: '))
    print('\033[33m**\033[m'*30)

    cont += 1

    if chute == numero_secreto:
        print('\033[32mPARABÉNS, Você acertou !!\033[m')
        break
    elif chute > numero_secreto:
        print('\033[31mERROU, seu chute foi maior que o número secreto!\033[m')
        pontos -= (chute - numero_secreto)
    elif chute < numero_secreto:
        print('\033[31mERROU, seu chute foi menor que o número secreto!\033[m')
        pontos -= (numero_secreto - chute)
    if chute != numero_secreto:
        print(f'Você ainda possui {y-c} tentativas!!')


print(f'\nVocê precisou de {cont} tentativas para acertar o número: {numero_secreto}'
      f'\nSua pontuação foi de {pontos} pontos!!')

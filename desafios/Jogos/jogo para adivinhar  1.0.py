from random import randint

numero_secreto = randint(1, 10)
cont = 0

while True:
    print('*' * 30)
    chute = int(input('Faça seu chute: '))
    print('*' * 30)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    cont += 1

    if acertou:
        print('Você acertou !!')
        break
    else:
        if maior:
            print('ERROU, seu chute foi maior que o número secreto!')
        elif menor:
            print('ERROU, seu chute foi menor que o número secreto!')

print(f'Você precisou de {cont} tentativas para acertar o número: {numero_secreto}')

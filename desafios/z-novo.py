secreta = 'BANANA'

palavra = ['X','X','X','X','X','X']

print(f'A palavra secreta possui {len(palavra)} letras, tente adivinhar!!')

while True:
    chute = str(input('Qual o seu chute? ')).upper()

    if chute in secreta:
        for k, c in enumerate(secreta):
            if chute == c:
                palavra[k] = chute
        print('Palavra secreta = ', end='')

        for c in palavra:
            print(c, end=' ')
        print()

    elif chute not in secreta and 'X' in palavra:
        print('Você errou!')

    if 'X' not in palavra:
        break

print(f'Fim do jogo.')










resp = 'S'
maior = menor = media = c = 0
while resp == 'S':
    n = int(input('Digite um número: '))
    c += 1
    media += n
    if c == 1:
        menor = n
        maior = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    resp = str(input('Quer continuar [S/N]..? ')).upper().strip()[0]
print('~'*30)
print('Maior -> {}\nMenor -> {}\nMédia -> {}\nNúmeros Digitados -> {}'.format(maior, menor, media/c, c))
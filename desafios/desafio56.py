media = 0
maior = 0
menor = 0
nom = ''
for c in range(1,5):
    print('----- {}° PESSOA -----'.format(c))
    nome = input('Nome: ')
    sexo = str(input('Sexo: [M/F] = ')).upper().strip()
    idade = int(input('Idade: '))
    media = idade + media
    if sexo == 'M':
        maior = idade
        nom = nome
        if maior > idade:
            nom = nome
    elif sexo =='F' and idade < 20:
        menor = menor + 1
print('-=-'*10)
print('A média de idade é de {} anos'.format(media/4))
print('O nome do homem mais velho é {} com {} anos'.format(nom, maior))
print('Existem {} mulheres com menos de 20 anos.'.format(menor))
print('-=-'*10)

idade = maiorp = menorm = homem = 0
resp = ' '
while resp != 'N':
    print('-=-'*12)
    idade = int(input('Idade? '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo - [F/M] ? ')).upper().strip()[0]
    if idade >= 18:
        maiorp += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        menorm += 1
    print('-=-'*12)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar - [S/N] ? ')).upper().strip()
print('-=-'*12)
print(f'Total de pessoas com mais de 18 anos: {maiorp}')
print(f'Total de homens cadastrados: {homem}')
print(f'Total de mulheres com menos de 20 anos: {menorm}')

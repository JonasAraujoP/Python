dados = dict()
nome = []
idade = []
sexo = []
somulher = []
acima = []
media = 0
sex = perg = ''

while True:
    print('-=-'*12)
    nome.append(str(input('Nome.: ')).capitalize())
    idade.append(int(input('Idade.: ')))
    while True:
        sex = (str(input('Sexo [F/M]? ')).upper())
        if sex in 'FM':
            break
        else:
            print('\033[31mERRO!\033[m Por favor, digite apenas F ou M.')
    sexo.append(sex)
    while True:
        perg = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
        if perg in 'SN':
            break
        else:
            print('\033[31mERRO!\033[m Por favor, digite apenas S ou N.')
    if perg == 'N':
        break
media = sum(idade)/len(idade)
dados["nome"] = nome
dados["idade"] = idade
dados["sexo"] = sexo
print('-=-'*12)

for c in range(0, len(nome)):
    print(f'Nome: {dados["nome"][c].capitalize():>10}, Idade: {dados["idade"][c]:>2},'
          f'Sexo: {dados["sexo"][c].upper():>1}')

for c in range(0, len(idade)):
    if idade[c] > media:
        acima.append(c)

print('-=-'*12)
print(f'Foram cadastradas {len(nome)} pessoas.')
print('-=-'*12)
print(f'A média de idade das pessoas cadastrasdas é {media:.2f} anos.')
print('-=-'*12)

for k, c in enumerate(sexo):
    if c == 'F':
        somulher.append(nome[k])

print(f'Foram cadastradas {len(somulher)} mulheres.')
print(somulher)
print('-=-'*12)

for c in acima:
    print(f'{len(acima)} pessoas estão acima da média de idade:'
          f'{nome[c]} com {idade[c]}')
print('Fim')

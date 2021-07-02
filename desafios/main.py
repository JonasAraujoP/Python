dados = []
resp = ' '
perg = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    print('-=-'*12)
    resp = str(input('Que continuar [S/N]? ')).upper().strip()
    if resp == 'N':
        break

print('Cod.    Nome:            Média    ')
for c in range(0, len(dados), 3):
    print(f'{c:<2} {dados[c]:^16}       {(dados[c+1]+dados[c+2])/2:>4}')
print('-=-'*12)
while perg != 999:
    print('\033[31mOBS\033[m -> Digite 999 para interromper!!')
    print('-=-'*12)
    perg = int(input('Mostrar notas de qual aluno? '))
    print('-=-'*12)
    if perg == 999:
        break
    else:
        for c in range(0, len(dados), 3):
            if perg == c:
                print(f'Aluno(a): \033[34m{dados[c]}\033[m, notas: \033[34m[{dados[c+1]}]  [{dados[c+2]}]\033[m')
                print('-=-'*12)
print('Fim do Programa.')

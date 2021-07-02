n = []
resp = 'S'
c = cont = 0
while resp not in 'N':
    c = (int(input('Digite um número: ')))
    if c not in n:
        n.append(c)
        print('Número adicionado com sucesso!')
    else:
        print('Numero duplicado, não será inserido!')
    resp = str(input('Quer continuar [S/N] ?')).upper().strip()
    cont += 1
    while resp not in 'S' and resp != 'N':
        print('Opção inválida, tente novamente.')
        resp = (str(input('Quer continuar [S/N] ?'))).upper().strip()
n.sort()
print(n)

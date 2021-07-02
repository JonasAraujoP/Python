dados = dict()
partida = 0
nome = list()
gol = []
print('-=-'*12)

while True:
    dados["nome"] = str(input('Nome: ')).upper().strip()
    partida = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for c in range(1, partida+1):
        gol.append(int(input(f'Na {c}° partida macou qauntos gols? ')))

    dados["gol"] = gol[:]
    dados["totalgol"] = sum(gol)

    nome.append(dados.copy())
    dados.clear()
    gol.clear()
    print('-=-' * 12)
    while True:
        perg = str(input('Quer continuar [S/N]? ')).upper().strip()
        if perg in 'SN':
            break
        print('Opção inválida, tente novamente!')
    if perg == "N":
        break

print('-=-'*12)

for k, v in enumerate(nome):
    print(f'{k:<3} ', end="")
    for d in v.values():
        print(f'{str(d):<15}', end="")
    print()

print('-=-'*12)
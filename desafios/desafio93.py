dados = dict()
gol = list()
dados["nome"] = str(input('Nome: ')).capitalize().strip()
dados["partidas"] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
print('\033[33m-=-\033[m'*24)

for c in range(1, dados["partidas"]+1):
    gol.append(int(input(f'Na {c}° partida marcou quantos gols? ')))
print('\033[33m-=-\033[m'*24)

dados["gol"] = gol[:]
dados["total de gols"] = sum(gol)

"""OS DADOS CONTIDOS NO DICIONÁRIO SERÃO MOSTRADOS NA TELA"""
print(dados)
print('\033[33m-=-\033[m'*24)

"""OS DADOS DO DICIONÁRIO SERÃO MOSTRADOS NA TELA DE FORMA MAIS ORGANIZADA"""
for k, c in dados.items():
    print(f'{k} = {c}')

print('\033[33m-=-\033[m'*24)

"""SERÁ MOSTRADO NA TELA A QUANTIDADE DE GOLS POR PARTIDA"""
print(f'Durante o campeonato, o jogador {dados["nome"]}, jogou {dados["partidas"]} partidas e', end=' ')

if dados["total de gols"] == 1:
    print(f'marcou {dados["total de gols"]} gol')
if dados["total de gols"] > 1:
    print(f'marcou {dados["total de gols"]} gols')
if dados["total de gols"] < 1:
    print('não marcou gol')

print('\033[33m-=-\033[m'*24)

for i, c in enumerate(dados["gol"]):
    if c == 0:
        print(f'No {i+1}° jogo, não fez gol.')
    if c == 1:
        print(f'No {i+1}° jogo, marcou {c} gol.')
    if c > 1:
        print(f'No {i+1}° jogo, marcou {c} gols.')

print('\033[33m-=-\033[m'*24)

"""FIM do CÓDIGO"""
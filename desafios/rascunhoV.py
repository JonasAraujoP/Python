import time
jogador = {}
total = 0
gols = []
while True:
    jogador["Nome"] = input('\nDigite o nome do jogador: ').capitalize()
    jogador["Partidas"] = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    for g in range(jogador["Partidas"]):
        golPart = int(input(f'Gols da {g+1}º partida: '))
        gols.append(golPart)
        #total += golPart
    total = sum(gols)
    jogador["Gols"] = gols.copy()
    jogador["Total"] = total
    print('-='*30)
    print(jogador)
    print('-='*30)
    for k,v in jogador.items():
        print(f'O campo {k} tem o(s) valor(es) {v}')
        time.sleep(1)
    print('-='*30)
    print(f'O jogador {jogador["Nome"]} fez {jogador["Partidas"]} partida(s) durante o campeonato')
    for p, c in enumerate(jogador["Gols"]):
        print(f'     => Na {p+1}º partida {jogador["Nome"]} fez {c} gol(s)')
        time.sleep(1.5)
    print(f'No total, {jogador["Nome"]} fez {jogador["Total"]} gol(s) durante o campeonato')
    print('-='*30)
    gols.clear()
    total = 0
    resp = ' '
    while resp not in 'ns':
        resp = input('Deseja continuar: ').lower().strip()[0]
    if resp in 'n':
        break
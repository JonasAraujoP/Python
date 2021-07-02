def ficha(x='', y=''):
    print(f"Nome: {nome}\nGols Marcado: {gol}")
    print('\033[33m-=-\033[m' * 15)


print('\033[33m-=-\033[m'*15)
nome = str(input('Nome: ')).title()

if nome == '':
    nome = '\033[31mDesconhecido\033[m'
gol = str(input(f'Quantos gols o jogador \033[34m{nome}\033[m marcou? '))

if gol.isnumeric():
    gol = int(gol)

else:
    gol = '\033[31m"0 gol(s)"\033[m'

print('\033[33m-=-\033[m'*15)
ficha(nome, gol)
dados = list()
nome = list()
peso = list()
pesado = leve = 0
while True:
    nome.append(str(input('Qual o seu nome? ')))
    peso.append(float(input('Qual o seu peso? ')))
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()
    if resp == 'N':
        break
for c in range(0, len(nome)):
    dados.append(nome[c])
    dados.append(peso[c])
print('-=-'*12)
print(f'Foram cadastradas {len(nome)}. Nomes => {nome}')
print(f'O maior peso foi de {max(peso):.2f}KgMario. Peso de ', end='[ ')
for c in peso:
    if c == max(peso):
        print(nome[pesado], end=' ]')
    pesado += 1
print()
print(f'O peso mais leve foi de {min(peso):.2f}Kg. Peso de ', end=' ')
for c in peso:
    if c == min(peso):
        print(nome[leve], end=' ')
    leve += 1
print()
print('Fim')

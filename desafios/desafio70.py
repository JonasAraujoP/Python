frase = 'LOLA SUPER BARATÃO'
print('-'*30)
print(f'{frase: ^30}')
print('-'*30)
resp = baratonome = ''
total = mais1000 = barato = c = 0
while resp != 'N':
    nome = str(input('Nome do produto: ')).upper().strip()
    valor = float(input('Preço R$: '))
    print('-=-' * 12)
    total += valor
    c += 1
    if valor > 1000:
        mais1000 += 1
    if c == 1 or valor < barato:
        barato = valor
        baratonome = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ? ')).strip().upper()
    if resp not in 'SN':
            print('Opção inválida')
            resp = str(input('Quer continuar [S/N] ? ')).strip().upper()
print('-=-'*12)
print(f'O total de gastos foi de R${total:.2f} reais.')
print(f'{mais1000} produtos custaram mais de R$ 1000,00 reais.')
print(f'O produto mais barato foi {baratonome}')
print('{:-^37}'.format('FIM DO PROGRAMA'))

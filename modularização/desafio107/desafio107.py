import moeda
print('-=-'*12)
valor = float(input('Digite o preço: R$ '))
taxa = float(input('Informe a taxa: '))
print('-=-'*12)
print(f'Aumento de {taxa}% sobre R${valor} = R${moeda.aumentar(valor, taxa)}')
print(f'Diminuição de {taxa}% sobre R${valor} = R${moeda.diminuir(valor, taxa)}')
print(f'Dobro de R${valor} = R${moeda.dobro(valor)}')
print(f'Metade R${valor} = R${moeda.metade(valor)}')
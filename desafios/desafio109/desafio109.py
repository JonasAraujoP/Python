import moeda
print('-=-'*12)
valor = float(input('Digite o preço: R$ '))
taxa = float(input('Informe a taxa: '))
#per = str(input('Deseja formato monetário [S/N]: ')).upper().strip()
print('-=-'*12)
print(f'Aumento de {taxa:.2f}% sobre {moeda.moeda(valor)} = {moeda.aumentar(valor, taxa, True)}')
print(f'Diminuição de {taxa:.2f}% sobre {moeda.moeda(valor)} = {moeda.diminuir(valor, taxa, True)}')
print(f'Dobro de {moeda.moeda(valor)} = {moeda.dobro(valor, True)}')
print(f'Metade {moeda.moeda(valor)} = {moeda.metade(valor, True)}')
print('-=-'*12)

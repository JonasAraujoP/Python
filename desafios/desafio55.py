maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('{}° valor '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O menor peso é', menor)
print('O maior peso é', maior)

t = 0
n = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')),
     int(input('Digite um valor: ')))
print(f'Os números inseridos foram: {n}')
print(f'O número 9 aparece {n.count(9)} vezes.')
if 3 in n:
    print(f'O número 3 aparece primeiro na posição {n.index(3)+1}')
else:
    print('O número 3 não foi digitado em nenhuma posição!')
for c in n:
    if c % 2 == 0:
        t += 1
print(f'Foram digitados {t} números pares.')
print('fim')
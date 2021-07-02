n = []
menor = maior = 0
for c in range(0, 5):
    n.append(int(input(f'informe o {c+1}º valor:')))
    if c == 0:
        menor = maior = n[c]
    else:
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
print(n)
print(f'O maior valor digitado foi {maior} e está na posição {n.index(maior)+ 1}')
print(f'O menor valor digitado foi {menor} e está na posição {n.index(menor)+ 1}')
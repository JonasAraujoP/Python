valores = []
menor = maior = cont = pose = posa = 0
for c in range(0, 5):
    valores.append(int(input(f'Informe um valor na posição {c+1}: ')))
for pos, c in enumerate(valores):
    cont += 1
    if cont == 1:
        menor = maior = c
    if maior < c:
        maior = c
        posa = cont
    if c < menor:
        menor = c
        pose = cont
print(valores)
print(f'maior valor é {maior}, está na posição {posa} da lista!')
print(f'menor valor é {menor}, está na posição {pose} da lista!')
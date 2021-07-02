n = []
m = ''
for c in range(0, 5):
    m = (int(input('Digite um valor: ')))
    if c == 0 or m > n[-1]:
        n.append(m)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(n):
            if m <= n[pos]:
                n.insert(pos, m)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados na ordem foi {n}')
print('FIM')
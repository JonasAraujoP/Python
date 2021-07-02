pa = pf = 0
exp = input('Digite sua expressão: ')
exp.split()
for c in exp:
    if c == '(':
        pa += 1
    if c == ')':
        pf += 1
if pa == pf:
    print(f'Sua expressão é válida.')
    print(f'Possui {pa} parenteses abertos e {pf} parenteses fechando.')
elif pa != pf:
    print('Sua expressão não é válida.')
    print(f'Possui {pa} parenteses abertos e {pf} parenteses fechando.')

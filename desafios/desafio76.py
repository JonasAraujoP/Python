t = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
    'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.00, 'Canetas', 22.00,
    'Livro', 34.90)
print('-'*30)
print('{: ^30}'.format('LISTA DE PREÇOS'))
print('-'*30)
for c in range(0, 17, 2):
    print(f'{t[c]:.<20} R${ t[c+1]:>7.2f}')

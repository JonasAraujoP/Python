from time import sleep
print('\nEsses são todos os números pares de 1 a 50:')
for c in range(1, 51):       #for c in range(2, 51, 2): (CÓDIGO DO PROFESSOR)
    if c % 2 == 0:
        print(c, end=" ")
print('FIM')
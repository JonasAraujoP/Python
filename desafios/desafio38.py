"""DESAFIO 38"""
n1 = int(input('Insira o 1° valor: '))
n2 = int(input('Insira o ° valor: '))
if n1 > n2:
    print('\nNúmero maior: {}\nNúmero menor: {}' .format(n1, n2))
elif n2 > n1:
    print('\nNúmero maior: {}\nNúmero menor: {}' .format(n2, n1))
else:
    print('\nOs números {} e {} são iguais!' .format(n1, n2))

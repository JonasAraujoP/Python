""" DESAFIO 37 - ESTUDAR E REFAZER"""
num = int(input('Digite um número inteiro: '))
escolha = int(input('1 para Binário.\n2 para Octagonal.\n3 para Hexadecimal.\nFaça sua escolha:  '))

if escolha == 1:
    print('O valor {} em BINÁRIO é {} ' .format(num, bin(num)[2:]))
elif escolha == 2:
    print('O valor {} em DECIMAL é {}' .format(num, oct(num)[2:]))
elif escolha == 3:
    print('O valor {} em OCTAL é {}' .format(num, hex(num)[2:]))
else:
    print('Opção inválida')
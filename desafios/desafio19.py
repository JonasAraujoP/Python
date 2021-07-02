from random import choice
n1 = str(input('1° nome: ')).upper().strip()
n2 = str(input('2° nome: ')).upper().strip()
n3 = str(input('3° nome: ')).upper().strip()
n4 = str(input('4° nome: ')).upper().strip()
lista = [n1, n2, n3, n4]
lista = choice(lista)
print('O aluno escolhido foi ',lista)
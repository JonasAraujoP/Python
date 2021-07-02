#CÓDIGO SORTEIA UM ALUNO APENAS
from random import shuffle
a = str(input('1° aluno: ')).upper().strip()
b = str(input('2° alino: ')).upper().strip()
c = str(input('3° aluno: ')).upper().strip()
d = str(input('4° aluno: ')).upper().strip()
lista = [a,b,c,d]
shuffle(lista)
print(lista)
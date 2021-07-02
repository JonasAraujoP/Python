"""DESAFIO 42 / 35 """
n1 = float(input('1° valor: '))
n2 = float(input('2° valor: '))
n3 = float(input('3° valor: '))

"""if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n3 and n1 == n2 and n2 != n3 or n1 == n3 and n2!= n3 or n2 == n3 and n2 != n1:
    print('Os segmentos foram um TRIÂNGULO ISÓSCELES.')

elif n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2 and n1 != n2 and n1 != n3 and n2 != n3:
    print('Os segmentos formam um TRIÂNGULO ESCALENO.')
elif n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2 and n1 == n2 and n1 == n3 and n2 == n3:
    print('Os segmentos formam um TRIÂNGULO EQUILÁTERO.')
else:
    print('Os segmentos não formam um TRIÂNGULO.')"""

#CÓDIGO DO PROFESSOR
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos formam um triângulo', end=' ')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 != n2 and n2 != n3 and n1 != n3: #outro modo de representar: n1 != n2 != 3!= n1
        print('ESCALENO')
    elif n1 == n2 or n1 == n3 or n2 == n3:    #outro modo de representar, trocar a espressão por "ELSE"
        print('ESÓSCELES')
else:
    print('Os segmentos NÃO FORMAM UM TRIÂNGULO.')
    
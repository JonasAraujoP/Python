from time import sleep


def contador(a, b, c):
    cont = a
    if a > b:
        if c < 0:
            c *= -1
        if c ==0:
            c = 1
        while cont >= b:
            print(cont, end=' ')
            cont -= c
            sleep(0.25)

    else:
        if c < 0:
            c *= -1
        if c == 0:
            c = 1
        while cont <= b:
            print(cont, end=' ')
            cont += c
            sleep(0.25)


print('Desafio 98 - Item "A"')
print('Contagem de 1 até 10, pulando de 1 em 1.')
a = 1
b = 10
c = 1
contador(a, b, c)
print()
print('-=-'*12)

print('Desafio 98 - Item "B"')
print('Contagem de 10 até 0, pulando de 2 em 2.')
a = 10
b = 0
c = 2
contador(a, b, c)
print()
print('-=-'*12)

print('Desafio 98 - Item "C"')
print('Contagem personalizada, definidade pelo usuário!')
a = int(input('Infomre o início da contagem: '))
b = int(input('informe o fim da contagem: '))
c = int(input('informe o PASSO da contagem: '))
print('-=-'*12)
contador(a, b, c)

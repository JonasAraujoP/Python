from time import sleep


def valor(*num):
    maior = 0
    cont = 0

    print('-=-' * 12)
    print('Analisando os valores informados!')

    for c in num:
        if cont == 0:
            maior = c

        if c > maior:
            maior = c
        cont += 1
        print(c, end=' ')
        sleep(0.25)

    if len(num) == 1:
        print(f'-> Foi informado {cont} valor ao todo.\nTendo o maior valor o {maior}')
    else:
        print(f'-> Foram informados {cont} valores ao todo.\nTendo o maior valor o {maior}')


valor(2, 9, 4, 5, 7, 1)
valor(4, 7, 0)
valor(1, 2)
valor(6)
valor()

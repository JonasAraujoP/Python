def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mErro! Digite um número inteiro.\033[m ')
        if ok:
            break
    return valor


n = leiaint('Digite um número inteiro: ')
print(f'O valor inteiro digitado foi {n}')
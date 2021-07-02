def leiaint(x):
    n = 0

    while True:
        try:
            n = int(input(x))
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        except:
            print(f'\033[31mErro. O número \"{n}\" é inválido.\033[m')
            continue
        else:
            return n


def leiafloat(x):
    n = 0

    while True:
        try:
            n = float(input(x))
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        except:
            print(f'\033[31mErro. O número \"{n}\" é inválido.\033[m')
            continue
        else:
            return n


inteiro = leiaint('Digite um número inteiro: ')
m = leiafloat('Digite um número real: ')
print()
print(f'O valor inteiro digitado foi {inteiro} e o real foi {m}')
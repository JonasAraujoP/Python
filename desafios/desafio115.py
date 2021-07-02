def cadastro(m=''):
    nome = list()
    idade = list()

    while True:
        try:
            n = int(m)
        except:
            return print('\033[31mERRO.Opção inválida, tente novamente!\033[m')
        else:
            if n == 1 and len(nome) == 0:
                print(f'\033[34m{"OPÇÃO - 1".center(34)}\033[m')
                print(f'\033[34m{"VER PESSOAS CADASTRADAS".center(34)}\033[m')
                print('\033[33m-\033[m' * 34)
                print('\033[31mNão há nomes cadastrados no momento.\033[m')
            elif n == 1 and len(nome) > 0:
                print(f'\033[34m{"OPÇÃO - 1".center(34)}\033[m')
                print(f'\033[34m{"VER PESSOAS CADASTRADAS".center(34)}\033[m')
                print('\033[33m-\033[m' * 34)
                print(f'\033[33m{"Nome:":<20}{"Idade:":>13} \033[m')

                for c in range(0, len(idade)):
                    print(f'{nome[c]:<20}  ->  {idade[c]:>3} anos')
                    #print(f'Nome: {nome[c]}  ->  Idade: {idade[c]} anos')

            elif n == 2:
                print(f'\033[34m{"OPÇÃO - 2".center(34)}\033[m')
                print(f'\033[34m{"CADASTRAR NOVA PESSOA".center(34)}\033[m')
                print('\033[33m-\033[m' * 34)
                nome.append(input('Qual nome deseja cadastrar? ').title())
                idade.append(input(f'Qual a idade? '))
            elif n == 3:
                print('Finalizando o programa, até logo!')
                break
        finally:
            print('\033[33m-\033[m' * 34)
            print(f'{"MENU PRINCIPAL".center(30)}')
            print('\033[33m-\033[m' * 34)
            print('\033[34m1 - Ver Pessoas Cadastradas'
                  '\n2 - Cadastrar Nova Pessoa'
                  '\n3 - Sair do Sistema\033[m')
            print('\033[33m-\033[m' * 34)
            m = str(input('Digite sua opção: '))
            print('\033[33m-\033[m' * 34)
            if '3' in m:
                print('Finalizando o programa, até logo!')
                break
            else:
                continue


print('\033[33m-\033[m' * 34)
print(f'{"MENU PRINCIPAL".center(34)}')
print('\033[33m-\033[m' * 34)
print('\033[34m1 - Ver Pessoas Cadastradas'
      '\n2 - Cadastrar Nova Pessoa'
      '\n3 - Sair do Sistema\033[m')
print('\033[33m-\033[m' * 34)
n = str(input('Digite sua opção: '))
print('\033[33m-\033[m' * 34)
cadastro(n)

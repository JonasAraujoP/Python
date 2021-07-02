meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
n= 1
while n < 4:
    mes = int(input('Escolha o número do mês desejado [1-12]: '))

    if 1 <= mes < 13:
        print(f'O mês escolhido foi \033[32m{meses[mes-1]}\033[m ')
        print('-=-'*12)
    else:
        print('Opção inválida!!')
    n += 1
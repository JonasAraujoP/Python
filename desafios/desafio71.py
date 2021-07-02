print('\033[33m=\033[m'*30)
print('\033[34m{: ^32}\033[m'.format('>> BANCO DO BRASIL <<'))
print('\033[33m=\033[m'*30)
while True:
    valor = int(input('\033[32mQuanto deseja sacar? R$ \033[m'))
    resto = cin = vin = dez = um = 0
    cin = valor // 50
    resto = valor % 50
    vin = resto // 20
    resto = resto % 20
    dez = resto // 10
    resto = resto % 10
    um = resto // 1
    resto = resto % 1
    if resto == 0:
        break
print('\033[33m='*30)
print('Você receberá:')
print(f'{cin:2} notas de R$ 50,00 reais\n{vin:2} notas de R$ 20,00 reais\n{dez:2} notas de R$ 10,00 reais\n{um:2} notas de R$  1,00 real\033[m')
print('\033[33m='*30)
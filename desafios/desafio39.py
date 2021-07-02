"""DESAFIO 39"""
from datetime import date
print('-=-'*10)
nasc = int(input('Em qual ano você nasceu? '))
sexo = int(input('Qual o seu sexo:\n1 - para MASCULINO\n2 - para FEMININO\nOpção: '))
print('-=-'*10)
atual = date.today().year
idade = atual-nasc

if idade < 18 and sexo == 1:
    print('Espere mais um pouco,\nsua idade é ', idade, 'anos')
    alistar = 18 - idade
    print('Seu alistamento será daqui a {} anos'.format(alistar))
elif idade == 18 and sexo == 1:
    print('Esta na hora de se alistar, pois sua idade é ', idade, 'anos')
elif idade > 18 and sexo == 1:
    print('Já passou do tempo,\nsua idade é ', idade, 'anos')
    idade = idade - 18
    print('Seu alistamento foi há {} anos'.format(idade))
else:
    print('Você não precisa se alistar!')
print('-=-'*10)

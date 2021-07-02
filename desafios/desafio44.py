"""DESAFIO 44"""
print('-=-'*13)
valor = float(input('Qual o valor do pagamento? R$ '))
print('-=-'*13)
print("""Qual a forma de pagamento?
[1]– à vista dinheiro/cheque: 10% de desconto
[2]– à vista no cartão: 5% de desconto
[3]– em até 2x no cartão: preço formal 
[4]– 3x ou mais no cartão: 20% de juros""")
forma = int(input('\nDigite sua escolha: '))
print('-=-'*13)

if forma == 1:
    des = valor - (valor*0.1)
    print("""Valor bruto: R${} reais
Valor do desconto: R${:.2f} reais
Valor a Pagar: R${:.2f} reais""".format(valor,valor*0.1, des))

elif forma == 2:
    desc = valor - (valor*0.05)
    print("""Valor bruto: R$ {:.2f} reais
Valor do desconto: R${:.2f} reais
Valor a pagar: R$ {:.2f} reais""".format(valor, valor*0.05, desc))

elif forma == 3:
    desc = 0
    print("""Valor bruto: R$ {:.2f} reais
Valor do desconto: R$ {:.2f} reais
Valor a pagar: R$ {:.2f}""".format(valor, valor*0, valor))

elif forma == 4:
    acres = valor + (valor*0.2)
    par = int(input('Em quantas parcelas deseja passar? '))
    print('-=-'*13)
    print("""Valor bruto: R$ {:.2f} reais
Quantidade de parcelas: {}
Valor do Acréscimo de 20%: R$ {:.2f} reais
Valor a pagar: R$ {:.2f} reais""".format(valor,par, valor*0.2, acres))
else:
    print('Opção inválida de pagamento, tente novamente.')
print('-=-'*13)

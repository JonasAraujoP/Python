print('='*21)
print(' 10 TERMOS DE UMA PA')
print('='*21)
n1 = int(input('Insira 1° termo: '))
r = int(input('Qual a RAZÃO dessa PA? '))
#quant_termo = int(input('Quantos termos deseja descobrir? '))
termo = n1 + (12 - 1) * r
print('='*21)

while termo-1 >= n1:
    n1 += r
    print(n1, end=' -> ')
print('FIM')
from datetime import date
maior = 0
menor = 0
hoje = date.today().year
for c in range(1, 8):
    idade = int(input('Em que ano a {}° pessoa nasceu: '.format(c)))
    if hoje - idade >= 21:
        maior += +1
    else:
        menor+=+1
print('Das {} datas informadas,\n{} são maiores de idade\n{} são menores de idade.'.format(c, maior, menor))

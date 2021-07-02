sexo = ''
while sexo != 'F' != 'M' != sexo:
    sexo = str(input('Informe seu sexo: ')).upper().strip()
    if sexo == 'F' or sexo == 'M':
        print('Obrigado por informa !')
    else:
        print('Opção inválida!')
print('ACABOU')

#CÓDIGO DO PROFESSOR
"""sexo = str(input('informe seu sexo: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Informação inválida, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))"""
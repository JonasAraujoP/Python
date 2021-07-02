dados = {'NOME': ' ', 'MÉDIA': ' '}
situacao = ' '
dados['NOME'] = str(input('Nome: ')).capitalize().strip()
media = float(input('Média: '))
dados['MÉDIA'] = media
if media >= 7:
    dados['SITUAÇÃO'] = 'APROVADO'
elif 5 <= media < 7:
    dados['SITUAÇÃO'] = 'RECUPERAÇÃO'
elif media < 5:
    dados['SITUAÇÃO'] = 'REPROVADO'
print('-=-'*12)
for k, v in dados.items():
    print(f'-{k} é igual a {v}')
print('-=-'*12)
print('Fim')

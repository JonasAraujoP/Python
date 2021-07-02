from datetime import date
dado = dict()

print('-=-'*12)

nome = str(input('Nome: ')).capitalize().strip()
nasc = int(input('Ano de nascimento: '))
idade = date.today().year-nasc
ctps = int(input('N° da CTPS: (0 não tem) '))

dado["nome"] = nome
dado["idade"] = idade

print('-=-'*12)

if ctps > 0:
    admissao = int(input('Ano que foi contratado: '))
    salario = float(input('Informe o salário: R$ '))
    aposentar = 35 - (date.today().year - admissao)
    dado["ctps"] = ctps
    dado["admissão"] = admissao
    dado["salário"] = salario
    dado["aposentadoria"] = aposentar
    print('-=-'*12)
    print(f'{dado["nome"]} tem {dado["idade"]} anos\n'
          f'N° CTPS: {dado["ctps"]}\n'
          f'Trabalha há {date.today().year-admissao} anos\n'
          f'Salário R$ {(dado["salário"]):.2f}\n'
          f'Idade a se aposentar: {idade+dado["aposentadoria"]} anos\n'
          f'Restando {dado["aposentadoria"]} anos de contribuição.')
else:
    print(f'{dado["nome"]} tem {dado["idade"]} anos,\n'
          f'Deve contribuir com 35 anos, para se aposentar')
print('-=-'*12)

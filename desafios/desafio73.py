clas = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
                 'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'EC Vitória',
                 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
t = 0
print('-=-'*20)
print(f'\033[31mListas dos times do Brasileirão 2017:\033[m')
for c in clas:
    print(c, end=' -> ')
    t += 1
    if t == 5 or t == 10 or t == 15 or t == 20:
        print('\n',end='')

print('-=-'*20)
print('\033[34mAtividade A\033[m')
print('Os primeiros 5 colocados são: ')
print(clas[0:5])
print('-=-'*20)
print('\033[34mAtividade B\033[m')
print('Os 4 últimos colocados são:')
print(clas[-4:])
print('-=-'*20)
print('\033[34mAtividade C\033[m')
print('A classificação na ordem alfabetica é:')
print(sorted(clas))
print('-=-'*20)
print('\033[34mAtividade D\033[m')
print('Em qual posição da tabela o time da \033[32mChapecoense\033[m está ?')
#CÓDIGO DO PROFESSOR print(f'A Chapecoense está na {clas.index("Chapecoense")+ 1}ª posição.')
for p, c in enumerate(clas):
    if c == 'Chapecoense':
        print(f'A Chapecoense está na {p + 1}ª posição.')
print('-=-'*20)

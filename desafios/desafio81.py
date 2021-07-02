l = list()
while True:
    l.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()
    if resp == 'N':
        break
print(f'Na lista L={l} há {len(l)} valores.')
l.sort(reverse=True)
print(f'Os valores na ordem decrescente é {l}')
if 5 in l:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 não faz parte da lista.')

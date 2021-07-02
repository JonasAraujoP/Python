print('-=-'*14)
print(f'{"Calculadora":^35}')
print('-=-'*14)
n = int(input('Deseja ver a tabuaba de qual número? '))
print('-=-'*14)

for c in range(1, 11):
    print(f'{n} x {c:2} = {n*c:2}')
print('-=-'*14)
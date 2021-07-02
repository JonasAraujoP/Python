n = 0
while True:
    print('~'*36)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('~'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c:2}')
print('Programa Tabuada encerrado, volte sempre !!')
print('FIM')
print('-=-'*15)
num = int(input('Digite um número para ver sua tabuada? '))
print('-=-'*15)
print(f'Exibindo a tabuada de multiplicação do {num}')
print('-=-'*15)

for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c:2}')

print('-=-'*15)


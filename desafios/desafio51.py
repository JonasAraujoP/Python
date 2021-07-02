num = int(input('1° termo da PA: '))
r = int(input('RAZÃO da PA: '))
decimo = num + (11-1) * r
print('-=-'*9)
for num in range(num, (decimo+r), r):
    print(num, end=' -> ')
print('FIM')

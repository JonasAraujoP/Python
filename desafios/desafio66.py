s = c = 0
while True:
    n = int(input('[Digite 999 para parar] - Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'\nA soma dos {c} valores é {s}')
t = ('APRENDER', 'PROGRAMAR', 'LINGUAGUEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
#pa =

for c in t:
    print(f'\nNa palavra {c}, temos ',end=' ')
    for letra in c:
        if letra in 'AEIOU':
            print(letra, end=' ')

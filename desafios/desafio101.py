def voto(x):
    from datetime import date
    atual = date.today().year
    idade = atual - x

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'

    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'

    else:
        return f'com {idade} anos: VOTO OBRIGATÓRIO.'


print('-=-'*12)
nasc = int(input('Informe seu ano de nascimento: '))
print(voto(nasc))
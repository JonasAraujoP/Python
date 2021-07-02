def aumentar(v=0, t=0, per=False):
    res = v + (v*t/100)
    return res if per is False else f'{moeda(res)}'


def diminuir(v=0, t=0, per=False):
    res = v - (v*t/100)
    return res if per == False else f'{moeda(res)}'


def dobro(v=0, per=False):
    res = v*2
    return res if not per else f'{moeda(res)}'


def metade(v=0, per=False):
    res = v /2
    return res if per==False else f'{moeda(res)}'


def moeda(v=0, cifrao='R$'):
    return f'{cifrao}{v:.2f}'.replace(".", ",")


def resumo(v=0, au=10, dim=5):
    print('-=-'*12)
    print(f'{"RESUMO DO PREÇO":^35}')
    print('-=-'*12)
    print(f'Preço analisado: \t{moeda(v)}'
          f'\nDobro do preço: \t{dobro(v, True)}'
          f'\nMetade do preço: \t{metade(v, True)}'
          f'\n{au}% de aumento: \t{aumentar(v, au, True)}'
          f'\n{dim}% de redução: \t{diminuir(v, dim, True)}')
    print('-=-'*12)
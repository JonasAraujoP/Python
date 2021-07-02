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
def aumentar(v=0, t=0):
    res = v + (v*t/100)
    return res


def diminuir(v=0, t=0):
    res = v - (v*t/100)
    return res


def dobro(v=0):
    res = v*2
    return res


def metade(v=0):
    res = v /2
    return res


def moeda(v=0, cifrao='R$'):
    return f'{cifrao}{v:.2f}'.replace(".", ",")
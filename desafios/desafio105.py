def notas(*num, sit=False):
    resp = dict()
    menor = maior = media = 0
    for k, v in enumerate(num):
        if k == 0:
            maior = v
            menor = v
        if v > maior:
            maior = v
        if v < menor:
            menor = v
    resp["Total"] = len(num)
    resp["maior"] = maior
    resp["menor"] = menor
    resp["média"] = sum(num) / len(num)
    if sit:
        if resp["média"] >= 7:
            resp["situação"] = "BOA"
        elif resp["média"] >= 5:
            resp["situação"] = "RAZOÁVEL"
        else:
            resp["situação"] = "RUIM"

    return resp


resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
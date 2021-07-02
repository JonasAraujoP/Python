def area(a, b):
    area1 = a * b
    print('-=-'*12)
    print(f'O terreno de LARGURA: {a} x COMPRIMENTO: {b} tem uma ÁREA DE {area1:.2f}m²')


print('-=-'*12)
largura = float(input('Qual a LARGURA do terreno? '))
comprimento = float(input('Qual o COMPRIMENTO do tereno? '))
area(largura, comprimento)

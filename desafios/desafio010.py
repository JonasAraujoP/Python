"""Crie um programa que leia quanto diheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar."""
print('-=-'*20)
num = float(input('Quanto você tem na sua carteira? R$').strip())
print(f'Com R$ {num:.2f} reais, você pode comprar U$$ {num / 4.91:.2f} dólares')
print('-=-'*20)
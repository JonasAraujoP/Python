"""Escreva um programa que converta uma temperatura digitada em °C para °F."""
print('-=-'*10)
temp = float(input('Informe a temperatura em °C: '))
fah = (temp * 1.8) + 32
kel = temp + 273.15
print('-=-'*10)
print(f'Convertendo {temp}°C, para:\n'
      f'1 - Fahrenheit: {fah}°F\n'
      f'2 - Kelvi: {kel}K')
print('-=-'*10)
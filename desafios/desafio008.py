
print('-=-'*15)
dis = float(input('Digite a distância em metros: ').replace(',','.'))
print('-=-'*15)
print(f'A distância em KM é {dis/1000}km')
print(f'A distância em HM é {dis/100}hm')
print(f'A distância em DAM é {dis/10}dam')
print(f'\033[32mA distância em M é {dis}m\033[m')
print(f'A distância em DM é {dis*10}dm')
print(f'A distância em CM é {dis*100}cm')
print(f'A distância em MM é {dis*1000}mm')
print('-=-'*15)
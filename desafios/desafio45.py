from random import randint
from time import sleep
print('\033[0;33m-=-\033[m'*12)
print('{:=^44}'.format('\033[34m JOGO DO JOKENPÔ\033[m '))
print('\033[33m-=-\033[m'*12)
print("""Faça sua escolha: 
[1] - Pedra
[2] - Papel
[3] - Tesoura""")
escolha = int(input('Qual a sua escolha? '))
print('\033[33m-=-\033[m'*12)
print('           \033[34mJO\033[m ',end='')
sleep(1)
print(' \033[34mKEN ',end='')
sleep(1)
print(' \033[34mPÔ')
print('\033[33m-=-\033[m'*12)
#sleep(2)
lista = randint(1,3)
if escolha == 1 and lista == 2:
    print("""Você jogou PEDRA
Skynet jogou PAPEL""")
    print('\033[31mVOCÊ PERDEU\033[m, tente novamente.')
elif escolha == 1 and lista == 1:
    print('Você jogou PEDRA\nComputador jogou PEDRA\n\033[33mDEU EMPATE\033[m.')
elif escolha == 1 and lista == 3:
    print("""Você jogou PEDRA
Skynet jogou TESOURA""")
    print('\033[32mVOCÊ VENCEU\033[m, PARABÉNS!')
elif escolha == 2 and lista ==1:
    print("""Você jogou PAPEL
Skynet jogou PEDRA""")
    print('\033[32mVOCÊ VENCEU\033[m, PARABÉNS!')
elif escolha == 2 and lista == 2:
    print('Você jogou PAPEL\nComputador jogou PAPEL\n\033[33mDEU EMPATE\033[m.')
elif escolha == 2 and lista == 3:
    print("""Você jogou PAPEL
Skynet jogou TESOURA""")
    print('\033[31mVOCÊ PERDEU\033[m, tente novamente.')
elif escolha == 3 and lista ==1:
    print("""Você jogou TESOUTA
Skynet jogou PEDRA""")
    print('\033[31mVOCÊ PERDEU\033[m, tente novamnete')
elif escolha == 3 and lista ==2:
    print("""Você jogou TESOURA
Skynet jogou PAPEL""")
    print('\033[32mVOCÊ VENCEU\033[m, PARABÉNS!')
elif escolha ==3 and lista ==3:
    print('Você jogou TESOURA\nComputador jogou TESOURA\n\033[33mDEU EMPATE\033[m.')
else:
    print('Opção inválida, tente novamente!')
print('\033[33m-=-\033[m'*12)
import urllib.request
import webbrowser
from time import sleep

print('-=-'*15)
try:
    site = urllib.request.urlopen('https://youtube.com.br')

except:
    print('Site indisponível no momento!!')

else:
    print('Site disponível no momento!!')
    print('Abrindo o site em ', end=' ')
    sleep(1)
    print('3', end=' ')
    sleep(1)
    print('2', end=' ')
    sleep(1)
    print('1', end=' ')
    sleep(0.25)
    print('Go !!')
    sleep(0.25)
    webbrowser.open('https://youtube.com.br')

print('-=-'*15)












''' CÓDIGO DE TERCEIROS - MUITO BOM


from time import sleep
import urllib.request
import webbrowser
try:
    urllib.request.urlopen("http://www.pudim.com.br")
except Exception as erro:  # Desligando o wifi, ou o site não estiver no ar
    print('\033[1;31m O site Pudim não está acessível no momento.\033[m')
    er = erro  # Variável usada para não ter marcações de erro no código pelo PyCharm.
else:  # Com wifi ligado:
    print('\033[1;32mConsegui acessar o site Pudim com sucesso!\033[m')
    print('Abrindo o site em 3, 2, 1...')
    sleep(3)
    webbrowser.open('http://www.pudim.com.br', new=2)

'''
""" DESAFIO 43 """
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))
imc = peso / altura**2

if imc < 18.5:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('Você está ABAIXO DO PESO, cuide-se mais.')

elif imc < 25 and imc >= 18.5:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('Você está no PESO IDEAL.')

elif imc >= 25 and imc < 30:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('Você está com SOBREPESO.')

elif imc >= 30 and imc < 40:
    print('Seu IMC é de {:.1f}'. format(imc))
    print('Você está com OBESIDADE.')

else:
    print('Você está com OBESIDADE MORBIDA.')

print('FIM')

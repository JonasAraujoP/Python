"""DESAFIO 40"""
print('-=-'*9)
nome = str(input('Qual o nome do aluno? ')) .upper() .strip()
n1 = float(input('Qual foi a 1° nota: '))
n2 = float(input('Qual foi a 2° nota: '))
m = (n1+n2)/2
print('-=-'*9)

if m >= 7:
    print('Nome: ', nome)
    print('Média: ', m)
    print('Situação: \033[34mAPROVADO\033[m')

elif m < 7 and m >= 5:
    print('Nome: ', nome)
    print('Média: ', m)
    print('Situação: \033[33mRECUPERAÇÂO\033[m')

else:
    print('Nome: ', nome)
    print('Média: ', m)
    print('Situação: \033[31mREPROVADO\033[m')

print('-=-'*9)

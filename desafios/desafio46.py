from time import sleep
print('\n\033[34mContagem Regressiva Para o Estouro dos \033[33m"Fogos de Artifício"\033[m.')
for c in range(10, -1, -1):
    sleep(0.5)
    print(c, end=' ')
print("\nFOGOS")
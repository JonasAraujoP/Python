c = int(input('\n\033[34mQual a tabuada desejada?\033[m '))
for n in range(1, 11):
    print('{} x {:2} = {:2}'.format(c, n, (c*n)))
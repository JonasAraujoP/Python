"""PROGRAMA ADAPTA AS LINHAS AO TEXTO INSERIDO PELO USUÁRIO"""


def escreva(msg):
    soma = len(texto) + 2
    print(f'='*soma)
    print(f'{texto:^{soma}}')
    print('='*soma)


print('-=-'*12)
texto = str(input('Digite um texto: ')).upper()
escreva(texto)


"""PROGRAMA COM TEXTO FIXO"""
"""
def escreva(msg):
    soma = len(msg) + 2
    print(f'='*soma)
    print(f'{msg:^{soma}}')
    print('='*soma)


escreva('GUSTAVO GUANABARA')
escreva('Curso em Vídeo de Python no Youtube')
escreva('CEV')
"""
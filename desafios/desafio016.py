"""Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
   ex: digite um número: 6.127  =>  O número 6.127, tem a parte inteiro 6 """

n = float(input('digite um número real:'))
print(f'O número {n}, tem a parte inteiro {n:.0f}')
print('\033[32m=-' * 10)
print('COMPARANDO NÚMEROS')
print('\033[32m=-\033[m' * 10)
n = int(input('''Escolha dois números inteiros para avaliar.
Primeiro número:'''))
m = int(input('Segundo número:'))
if n > m:
    print('O primeiro valor foi o maior número digitado!')
elif m > n:
    print('O segundo valor foi o maior número digitado!')
elif m == n:
    print('Não existe valor maior, os dois são iguais!')

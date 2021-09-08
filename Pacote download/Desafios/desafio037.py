print('\033[35m=-'*10)
print('BASES DE CONVERSÃO')
print('\033[35m=-\033[m'*10)
n = int(input('Digite um número qualquer:'))
print('''Escolha uma das bases para conversão:
\033[31m[ 1 ]\033[m CONVERTER para Binário
\033[31m[ 2 ]\033[m CONVERTER para Octal
\033[31m[ 3 ]\033[m CONVERTER para Hexadecimal''')
m = int(input('Agora digite o número correspondente a base você deseja:'))
if m == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif m == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif m == 3:
    print('{} convertido em HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Operação Inválida! Tente novamente!')
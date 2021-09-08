#SOMANDO APENAS OS NUMEROS PARES DIGITADOS feito
s = 0
h = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro qualquer:'))
    if n % 2 == 0:
        s = s + n
        h = h + 1
print('O somatório de todos os {} números pares digitados equivale a {}'.format(h, s))

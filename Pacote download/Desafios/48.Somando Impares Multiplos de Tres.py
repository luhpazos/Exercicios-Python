#SOMA DOS NUMEROS IMPARES MULTIPLOS DE 3 ENTRE 1 E 500 FEITO
s = 0
for c in range(1, 500):
    if c % 2 != 0 and c % 3 == 0:
        s = s + c
print('A soma de todos os números solicitados é {}'.format(s))




print('\033[36m=-'*15)
print('CALCULANDO SUA MÉDIA ESCOLAR')
print('\033[36m=-\033[m'*15)
n1 = float(input('Digite sua nota de AV1:'))
n2 = float(input('Digite sua nota de AV2:'))
m = (n1 +n2)/2
if m < 5:
    print('Reprovado! Sua média foi de {:.2f}!'.format(m))
elif 5 <= m <= 6.9:
    print('Recuperãção! Sua média foi de {:.2f}. Estude bastante para passar de ano!'.format(m))
elif m >= 7:
    print('Aprovado! Sua média foi de {:.2f}. Parabéns!'.format(m))
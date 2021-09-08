v = int(input('Quantos Km você percorrerá na sua viagem?'))
n = v * 0.50
m = v * 0.45
if v <= 200:
    print('A sua passagem custará R${:.2f}.'.format(n))
else:
    print('A sua passagem custará R${:.2f}.'.format(m))

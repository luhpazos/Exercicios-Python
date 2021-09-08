n1 = float(input('Quantos reais você tem?'))
m = n1 // 3.27
r = n1 % 3.27
print('Com ${} Reais você consegue comprar ${} Dólares! Visto que a cotação atual está em R$3,27!'.format(n1, m))
print('Resta ${:.2f} Reais!'.format(r))

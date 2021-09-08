n = int(input('Digite um número entre 0 e 9999:'))
print('O número escolhido foi:{}'.format(n))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('unidade:{}'.format(u))
print('ddezena:{}'.format(d))
print('centena:{}'.format(c))
print('milhar:{}'.format(m))

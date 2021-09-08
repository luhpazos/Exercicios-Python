#USANDO A VARIAVEL DE REPETIÇÃO FOR (COLOCAR ASPAS ANTES DE USAR)
m = 1
n = int(input('Digite um número qualquer e descubra seu fatorial:'))
for c in range(n, 0, -1):
    m = m * c
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
print(m, end='')
print('\nO fatorial de {} vale {}'.format(n, m))

#USANDO A VARIAVEL DE REPETIÇÃO WHILE (COLOCAR ASPAS ANTES DE USAR)
c = 1
n = int(input('Digite um número qualquer e descubra seu fatorial:'))
b = n
while b > 0:
    c = c * b
    print('{} '.format(b), end='')
    b = b - 1
    print('x ' if b > 0 else '= ', end='')
print(c, end='')
print('\nO fatorial de {} vale {}'.format(n, c))


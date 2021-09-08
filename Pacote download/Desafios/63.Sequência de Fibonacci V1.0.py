#SEQUENCIA DE FIBONACCI
"""n = int(input('Digite um número inteiro qualquer para vê-lo na sequência de Fibonacci:'))
c = 1
f = 0
while n != 0:
    print('{}'.format(f))
    f = f + c
    c = f - c
    n = n - 1"""
n = int(input('Quantos termos da sequência de fibonacci você deseja ver?'))
t1 = 0
t2 = 1
print('{} ~ {} ~ '.format(t1, t2), end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print('{} ~ '.format(t3),end='')
    t1 = t2
    t2 = t3
    count += 1
print('FIM')
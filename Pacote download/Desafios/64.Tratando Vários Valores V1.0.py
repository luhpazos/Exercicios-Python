n = int(input('Digite um número qualquer:'))
s = n
c = 0
while n != 999:
    n = int(input('Digite mais um número: (quando quiser parar digite "999")'))
    s = s + n
    c = c + 1
print('FIM')
print('A soma de todos os {} números digitados vale {}'.format(c, (s - 999)))

n = int(input('Digite um número qualquer:'))
q = str(input('Você quer continuar? [S/N]:')).strip().upper()[0]
s = n
c = 1
maior = n
menor = n
while q not in 'N':
    n = int(input('Digite mais um número:'))
    q = str(input('Você quer continuar? [S/N]:')).strip().upper()[0]
    s = s + n
    c = c + 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n

m = s / c
print('A média de todos {} os valores digitados vale {:.2f}'.format(c, m))
print('O menor valor digitado foi {} e o maior valor digitado foi {}'.format(menor, maior))

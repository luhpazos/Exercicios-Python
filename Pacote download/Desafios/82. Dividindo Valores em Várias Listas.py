lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    p = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    while p not in 'NS':
        p = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    if p == 'N':
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    if n % 2 != 0:
        impar.append(n)
print(f'Os valores digitados foram {lista}')
print(f'Os valores pares digitados foram {par}')
print(f'Os valores impares digitados foram {impar}')

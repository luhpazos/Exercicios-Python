par = []
impar = []
t = []
for c in range(0,7):
    n = int(input(f'Digite o {c + 1}º valor:'))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
impar.sort()
t.append(par)
t.append(impar)
print(f'Os valores pares digitados foram: {t[0]}')
print(f'Os valores impares digitados foram: {t[1]}')
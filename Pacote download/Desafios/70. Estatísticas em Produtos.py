print('--'*10)
print('LOJA SUPER BARATÃO')
print('--'*10)
n = str(input('Nome do produto:')).strip().lower()
p = float(input('Preço: R$'))
q = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
s = p
c = 0
menor = p
barato = n
while True:
    n = str(input('Nome do produto:')).strip().lower()
    p = float(input('Preço: R$'))
    q = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    s += p
    if p < menor:
        menor = p
        barato = n
    if p > 1000:
        c += 1
    while q not in 'SN':
        q = str(input('Quer continuar? [S/N]:')).strip().upper()[0]

    if q == 'N':
        print('======= FIM DO PROGRAMA =======')
        break
print(f'O total da compra foi de R${s:.2f}')
print(f'Temos {c} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

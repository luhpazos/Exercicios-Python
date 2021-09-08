print('=' * 20)
print(f'{"Banco CEV":^20}')
print('=' * 20)
n = int(input('Qual valor você deseja sacar? R$'))
m = n
c50 = c20 = c10 = c1 = 0
while True:
    while m >= 50:
        m -= 50
        c50 += 1
    while m >= 20:
        m -= 20
        c20 += 1
    while m >= 10:
        m -= 10
        c10 += 1
    while m >= 1:
        m -= 1
        c1 += 1
    break
if c50 > 0:
    print(f'total de {c50} cédulas de R$50')
if c20 > 0:
    print(f'total de {c20} cédulas de R$20')
if c10 > 0:
    print(f'Total de {c10} cédulas de R$10')
if c1 > 0:
    print(f'Total de {c1} cédulas de R$1')
print('=='*20)
print('Volte sempre ao Banco CEV!')
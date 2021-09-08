t = []
princ = []
peso = []
while True:
    t.append(str(input('Nome:')))
    t.append(float(input('Peso:')))
    princ.append(t[:])
    peso.append(t[1])
    t.clear()
    q = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    while q not in 'SN':
        q = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    if q == 'N':
        break
print(f'Ao todo foram cadastradas {len(princ)} pessoas')
print(f'O maior peso foi de {max(peso):.1f}Kg de ', end='')
for p in princ:
    if p[1] == max(peso):
        print(f'[{p[0] }]', end=' ')
print(f'\nO menor peso foi de {min(peso):.1f}Kg de ', end='')
for p in princ:
    if p[1] == min(peso):
        print(f'[{p[0]}]', end=' ')

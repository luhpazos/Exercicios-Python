t = list()
princ = list()
nomema = []
nomeme = []
while True:
    t.append(str(input('Nome:')))
    t.append(float(input('Peso:')))
    princ.append(t[:])
    t.clear()
    q = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    while q not in 'SN':
        q = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    if q == 'N':
        break
pme = princ[0][1]
pma = 0
print(pme)
for p in princ:
    if p[1] > pma:
        pma = p[1]
    if p[1] < pme:
        pme = p[1]
for p in princ:
    if p[1] == pma:
        nomema.append(p[0])
    if p[1] == pme:
        nomeme.append(p[0])
print(princ)
print(f'Ao todo foram cadastradas {len(princ)} pessoas')
print(f'O maior peso foi de {pma:.1f}Kg de {nomema}')
print(f'O menor peso foi de {pme:.1f}Kg de {nomeme}')

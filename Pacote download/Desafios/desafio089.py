tot = list()
while True:
    n = input('Nome:').strip().capitalize()
    t1 = float(input('Nota 1:'))
    t2 = float(input('Nota 2:'))
    med = (t2 + t1) / 2
    tot.append([n, [t1, t2], med])
    q = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    while q not in 'SN':
        q = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    if q == 'N':
        break
print(tot)
print('=-'*22)
print(f'{"NO.":<6} {"NOME":<10} {"MÉDIA":>5}')
print('--'*13)
for i, c in enumerate(tot):
    print(f'{i:<6} {c[0]:<10} {c[2]:>5.1f}')
print('--'*13)
while True:
    e = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    for i, c in enumerate(tot):
        if e == i:
            print(f'As notas de {c[0]} são {c[1]}')
            print('--'*20)
    if e == 999:
        break

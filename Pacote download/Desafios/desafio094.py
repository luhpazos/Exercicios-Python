d = dict()
dados = list()
c = 0
si = 0
while True:
    d['nome'] = str(input('Nome:')).strip().capitalize()
    d['sexo'] = str(input('Sexo [M/F]:')).strip().upper()[0]
    while d['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        d['sexo'] = str(input('Sexo [M/F]:')).strip().upper()[0]
    d['idade'] = int(input('Idade:'))
    c += 1
    si += d['idade']
    dados.append(d.copy())
    d.clear()
    q = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    while q not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N.')
        q = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if q == 'N':
        break
m = si / c
print('=-'*20)
print(f'- O grupo tem {c} pessoas cadastradas.')
print(f'- A média de idade é de {m:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for e in range(0, len(dados)):
    if dados[e]['sexo'] in 'F':
        print(f'{dados[e]["nome"]}', end=' ')
print('\n- Lista das pessoas que estão acima da média:')
for e in range(0, len(dados)):
    if dados[e]['idade'] >= m:
        print(f'{dados[e]}')
        print()

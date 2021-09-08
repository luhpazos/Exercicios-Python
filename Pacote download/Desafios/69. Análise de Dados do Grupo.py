ci = cs = m = 0
while True:
    print('--'*10)
    print('CADASTRE UMA PESSOA')
    print('--'*10)
    i = int(input('Idade:'))
    s = str(input('Sexo [F/M]:')).strip().upper()[0]
    if i >= 18:
        ci += 1
    if s == 'M':
        cs += 1
    if s == 'F' and i < 20:
        m += 1
    while s not in 'FM':
        s = str(input('Sexo [F/M]:')).strip().upper()[0]
    print('--'*10)
    p = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    while p not in 'SN':
        p = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if p == 'N':
        print('=======FIM DO PROGRAMA=======')
        break
print(f'No total foram cadastradas {ci} pessoas com mais de 18 anos!')
print(f'Ao todo temos {cs} homens cadastrados!')
print(f'E temos {m} mulheres com menos de 20 anos!')

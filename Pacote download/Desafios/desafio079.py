l = []
while True:
    n = int(input('Digite um valor:'))
    if n in l:
        print('Valor duplicado! Não vou adicionar...')
    else:
        l.append(n)
        print('Valor adicionado com sucesso!')
    p = str(input('Você que continuar? [S/N]')).strip().upper()[0]
    while p not in 'SN':
        p = str(input('Você que continuar? [S/N]')).strip().upper()[0]
    if p == 'N':
        break
print(f'Você digitou os valores ', end='')
l.sort()
print(l)

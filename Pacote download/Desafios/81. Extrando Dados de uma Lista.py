lista = []
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    p = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    while p not in 'SN':
        p = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    if p == 'N':
        break
print(f'Você digitou {len(lista)} elementos!')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if lista.count(5) >= 1:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
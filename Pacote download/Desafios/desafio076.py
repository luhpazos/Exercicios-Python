lista = ('Lápis', 1.75, 'borracha', 2, 'caderno', 15.90, 'Estojo',25, 'transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'canetas', 22.30, 'livro', 34.90)
print('--'*20)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('--'*20)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<28}', end='')
    if c % 2 != 0:
        print(f'R${lista[c]:>7.2f}')
print('--'*20)
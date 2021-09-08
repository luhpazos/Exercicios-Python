matriz = [[], [], []]
soma = 0
somal = 0
ma = 0
for c in range(0, 3):
    for li in range(0, 3):
        n = (int(input(f'Digite um valor para [{li}, {c}]:')))
        matriz[c].append(n)
        if n % 2 == 0:
            soma += matriz[c][li]
        if li == 2:
            somal += matriz[c][li]
        if c == 1:
            if n > ma:
                ma = n
print('-='*20)
for p in range(0, 3):
    print(f'[{matriz[0][p]:^5}]', end=' ')
print()
for p in range(0, 3):
    print(f'[{matriz[1][p]:^5}]', end=' ')
print()
for p in range(0, 3):
    print(f'[{matriz[2][p]:^5}]', end=' ')
print()
print('-='*20)
print(f'A soma de todos os valores pares é {soma}')
print(f'A soma dos valores da terceira coluna vale {somal}')
print(f'O maior valor da segunda linha vale {ma}')

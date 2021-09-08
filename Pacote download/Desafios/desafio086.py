matriz = [[], [], []]
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {l}]:')))

for p in range(0,3):
    print(f'[{matriz[0][p]:^5}]', end=' ')
print()
for p in range(0, 3):
    print(f'[{matriz[1][p]:^5}]', end=' ')
print()
for p in range(0, 3):
    print(f'[{matriz[2][p]:^5}]', end=' ')

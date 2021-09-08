
p = []
pma = []
pme = []
for c in range(0, 5):
    n = (int(input(f'Digite um valor para a posição {c}:')))
    p.append(n)
for i, v in enumerate(p):
    if v == max(p):
        pma.append(i)
    if v == min(p):
        pme.append(i)
print(f'O maior valor digitado foi {max(p)} nas posições {pma}')
print(f'O menor valor digitado foi {min(p)} nas posições {pme}')


d = []
for c in range(0, 5):
    n = int(input('Digite um valor:'))
    if c == 0:
        d.append(n)
    if c == 1:
        if n > d[0]:
            d.append(n)
        if n < d[0]:
            d.insert(0, n)
    if c == 2:
        if n < d[0]:
            d.insert(0, n)
        if n > d[1]:
            d.append(n)
        if d[0] < n < d[1]:
            d.insert(1, n)
    if c == 3:
        if n < d[0]:
            d.insert(0, n)
        if n > d[2]:
            d.append(n)
        if d[0] < n < d[1]:
            d.insert(1, n)
        if d[1] < n < d[2]:
            d.insert(2, n)
    if c == 4:
        if n < d[0]:
            d.insert(0, n)
        if n > d[3]:
            d.append(n)
        if d[0] < n < d[1]:
            d.insert(1, n)
        if d[1] < n < d[2]:
            d.insert(2, n)
        if d[2] < n < d[3]:
            d.insert(3, n)
    print(f'Valor adicionado na posição {d.index(n)} da lista...')

print(f'Os valores digitados em ordem foram {d}')

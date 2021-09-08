print('\033[36m----------TABUADA----------\033[m')
while True:
    n = int(input('De qual valor você deseja ver a tabuada?'))
    print('\033[35m--\033[m'*20)
    if n < 0:
        break
    for c in range(1, 11):
        m = n * c
        print(f'{n} x {c} = {m}')
    print('\033[35m--\033[m'*20)
print('Programa ENCERRADO! Volte sempre!')

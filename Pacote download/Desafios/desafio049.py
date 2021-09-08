#TABUADA
print('\033[35m✨🎇 TABUADA 🎇✨\033[m')
n = int(input('Digite um número entre 1 e 10 para vê-lo na tabuada:'))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))


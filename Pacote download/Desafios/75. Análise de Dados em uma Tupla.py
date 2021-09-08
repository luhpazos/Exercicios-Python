n = tuple(int(input('Digite um número:')) for c in range(1, 5))
print(f'Você digitos os valores {n}')
print(f'O valor nove apareceu {n.count(9)} vezes!')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1}º posição!')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print('Os valores pares digitados foram', end=' ')
for n in n:
    if n % 2 == 0:
        print(f'{n}', end=' ')

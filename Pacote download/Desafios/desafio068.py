import random
print('=-'*13)
print('\033[36mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('=-'*13)
c = 0
while True:
    s = 0
    r = random.randint(1, 10)
    n = int(input('Digite um valor:'))
    v = str(input('Par ou Ímpar? [P/I]:')).strip().upper()[0]
    print('\033[36m--\033[m'*30)
    s = n + r
    print(f'Você jogou {n} e o computador {r}. A soma vale {s}. ', end='')
    if s % 2 == 0:
        print('Deu PAR!')
        print('\033[36m--\033[m'*30)
    if s % 2 != 0:
        print('Deu IMPAR!')
        print('\033[36m--\033[m'*30)
    if s % 2 == 0 and v == 'P':
        print('Você VENCEU!\nVamos jogar novamente...')
        c += 1
    elif s % 2 == 0 and v == 'I':
        print('Você PERDEU!')
        break
    elif s % 2 != 0 and v == 'I':
        print('Você VENCEU!\nVamos jogar novamente...')
        c += 1
    elif s % 2 != 0 and v == 'P':
        print('Você PERDEU!')
        break
print(f'\033[31mGAME OVER!\033[m Você venceu {c}', end='')
if c == 1:
    print(' vez!')
else:
    print(' vezes!')

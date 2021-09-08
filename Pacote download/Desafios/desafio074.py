from random import randint
print('Os números sorteados foram: ', end='')
r = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(r, end=' ')
print(f'\nO maior valor sorteado foi {max(r)}')
print(f'O menor valor sorteado foi {min(r)}')

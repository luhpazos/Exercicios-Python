from random import randint
from time import sleep
nu = []
jo = []
print('--'*20)
print(f'{"JOGO DA MEGA SENA":^40}')

print('--'*20)
p = int(input('Quantos jogos você quer que eu sorteie?'))
for c in range(0, p):
    for x in range(0, 6):
        s = randint(1, 60)
        nu.append(s)
    jo.append(nu[:])
    nu.clear()

print(f'---- SORTEANDO {p} JOGOS ----')
for b in range(0, p):
    print(f'Jogo {b + 1}: ', end='')
    print(f'{jo[b]}')
    sleep(0.5)
print('------ BOA SORTE! ------')

from random import randint
from time import sleep
from operator import itemgetter
from typing import Dict, Any

res = dict()
for c in range(0, 4):
    d = randint(1, 6)
    res[f'Jogador {c + 1}'] = d
print('Valores sorteados:')
for k, v in res.items():
    sleep(1)
    print(f'O {k} tirou {v}')
print('=-'*20)
print('Ranking dos jogadores:')
rank = sorted(res.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(rank):
    print(f'{k + 1}º Lugar: {v[0]} com {v[1]}')

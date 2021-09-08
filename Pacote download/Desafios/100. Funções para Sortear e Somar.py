from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista:')
    for c in range(0, 5):
        lista.append(randint(1, 10))
    for v in lista:
        print(f'{v}', end='    ')
        sleep(1)


def somapar(lista):
    s = 0
    for v in lista:
        if v % 2 == 0:
            s += v
    print(f'\nSomando todos os valores pares presentes em {numeros}, temos {s}')


# programa principal
numeros = list()
sorteia(numeros)
somapar(numeros)

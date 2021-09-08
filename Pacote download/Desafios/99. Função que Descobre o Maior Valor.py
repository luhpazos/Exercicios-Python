from time import sleep


def maior():
    print('Analisando os valores passados...')
    for d in range(0, len(numeros)):
        print(f'{numeros[d]}', end=' ')
        sleep(1)
    print(f'\nAo todo foram informados {len(numeros)} valores.')
    print(f'O maior valor informado foi {max(numeros)}.')


numeros = list()
q = str(input('Você quer digitar algum número? [S/N]')).strip().upper()[0]

if q == 'S':
    while True:
        n = int(input('Digite um número inteiro:'))
        numeros.append(n)
        p = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        while p not in 'SN':
            p = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if p == 'N':
            break
    print(maior())
else:
    print('Analisando os valores passados...')
    print(f'Ao todo foram informados 0 valores.')
    print(f'O maior valor informado foi 0.')

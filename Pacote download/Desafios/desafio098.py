from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
            sleep(0.5)
    if fim < inicio:
        for c in range(inicio, fim - 1, - passo):
            print(c, end=' ')
            sleep(0.5)
    print('FIM!')


# programa principal
# A
contador(1, 10, 1)
# B
contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
contador(i, f, p)

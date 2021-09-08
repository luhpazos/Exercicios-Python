x = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
     'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
     'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
     'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20:'))
while n < 0 or n > 20:
    n = int(input('Tente novamente. Digite um número entre 0 e 20:'))
print(f'Você digitou o número {x[n]}')

while True:
    d = str(input('Você quer continuar?: [S/N]')).strip().upper()[0]
    if d == 'S':
        n = int(input('Digite um número entre 0 e 20:'))
    else:
        break
print('FIM DO PROGRAMA')
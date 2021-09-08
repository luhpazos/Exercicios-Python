print('\033[36m~CALCULANDO PA~\033[m')
n = int(input('Digite o primeiro termo da PA:'))
r = int(input('Agora digite a razão dessa PA:'))
print('Esses são os dez primeiros termos dessa PA:')
termo = n
cont = 1
while cont <= 10:
    print('\033[36m{}'.format(termo), end=' ')
    cont += 1
    termo += r

b = int(input('\n\033[mVocê deseja ver mais termos dessa PA? se sim, quantos? [caso não queira, digitar 0]'))
co = 1
s = 10 + b
while b > 0:
    co = 1
    while co <= b:
        co += 1
        print('\033[36m{}'.format(termo), end=' ')
        termo += r
    b = int(input('\n\n\033[mVocê deseja ver mais termos dessa PA? se sim, quantos? [caso não queira, digitar 0]'))
    s = s + b
print('\n\033[31mFIM')
print('Foram mostrados {} termos'.format(s))

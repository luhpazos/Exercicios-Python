print('\033[36m~CALCULANDO PA~\033[m')
n = int(input('Digite o primeiro termo da PA:'))
r = int(input('Agora digite a razão dessa PA:'))
print('Esses são os dez primeiros termos dessa PA:')
t = n
c = 1
while c <= 10:
    c = c + 1
    print('{}'.format(t), end=' ')
    t = t + r
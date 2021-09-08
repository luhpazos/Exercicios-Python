#CALCULADORA DE PA feito
print('\033[36m~CALCULANDO PA~\033[m')
n = int(input('Digite o primeiro termo da PA:'))
r = int(input('Agora digite a razão dessa PA:'))
print('Esses são os dez primeiros termos dessa PA:')
for c in range(1, 11):
    m = n + (c - 1) * r
    print(m)

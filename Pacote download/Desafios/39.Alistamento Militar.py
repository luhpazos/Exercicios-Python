from datetime import date
print('\033[33m=-'*6)
print('ALISTAMENTO')
print('\033[33m=-\033[m'*6)
a = int(input('Digite seu ano de nascimento por favor:'))
n = date.today().year - a
if n < 18:
    print('faltam {} anos para seu alistamento no serviço militar!'.format(18 - n))
elif n > 18:
    print('Já se passaram {} anos do seu alistamento militar!'.format(n - 18))
elif n == 18:
    print('Chegou a hora de se alistar! Este é o seu ano de alistamento no serviço militar! prepare-se!')

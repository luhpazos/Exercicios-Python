from datetime import date
print('\033[34m~~'*12)
print('CONFEDERAÇÃO DE NATAÇÃO')
print('\033[34m~~\033[m'*12)
a = int(input('''Descubra qual a sua categoria de acordo com o ano em que nasceu!
ANO:'''))
i = date.today().year - a
print('O atleta tem {} anos!'.format(i))
if i <= 9:
    print('Sua categoria é MIRIM!')
elif i <= 14:
    print('Sua categoria é INFANTIL!')
elif 14 < i <= 19:
    print('Sua categoria é JUNIOR!')
elif 19 < i <= 25:
    print('Sua categoria é SÊNIOR!')
elif i > 25:
    print('Sua categoria é MASTER!')
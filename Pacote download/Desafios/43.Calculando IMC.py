print('\033[36m~~'*10)
print('CALCULADORA DE IMC')
print('~~'*10)
p = float(input('\033[mQuantos Kg você pesa:'))
a = float(input('Quantos metros você tem de altura:'))
c =  p / (a**2)
print('O seu IMC é de {:.2f}'.format(c))
if c < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= c < 25:
    print('Você está com seu peso ideal!')
elif 25 <= c < 30:
    print('Você está com sobrepeso!')
elif 30 <= c < 40:
    print('Você está com obesidade!')
elif  c >= 40:
    print('Você está com obesidade mórbida! Cuide-se!')
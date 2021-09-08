s = float(input('Qual é o seu salário atual? R$'))
a = (s * 10/100) + s
b = (s * 15/100) + s
if s <= 1250.00:
    print('Você receberá um aumento de 15%. Seu novo salário é de R${:.2f}'.format(b))
else:
    print('Você receberá um aumento de 10%. Seu novo salário é de R${:.2f}'.format(a))

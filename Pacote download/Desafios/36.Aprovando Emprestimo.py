print('\033[34m=-' * 10)
print('\033[36mEMPRÉSTIMO BANCÁRIO')
print('\033[34m=-\033[m' * 10)
print('\033[97mPara análise e aprovação do empréstimo solicitado informe os seguintes dados')
a = float(input('Valor do empréstimo:'))
b = float(input('Valor do seu sálario mensal:'))
c = int(input('Em quantos anos você pretende pagar:'))
n = a / (c * 12)
if n < b * 0.3:
    print('Seu empréstimo foi aprovado e sua prestação será de R${:.2f} durante {} anos!'.format(n, c))
else:
    print('Seu empréstimo foi negado! O valor da prestação seria de R${:.2} e acreditamos que você não ganha o suficiente para nos pagar!'.format(n))

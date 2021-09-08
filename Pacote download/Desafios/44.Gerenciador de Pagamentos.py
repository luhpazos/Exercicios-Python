print('\033[36m~' * 7)
print('COMPRAS')
print('~' * 7)
n = int(input('''\033[31m[1]\033[m MICROONDAS
\033[31m[2]\033[m BICICLETA
\033[1mDigite o número referente ao poduto que você deseja?\033[m'''))
if n == 1:
    print('O microondas custa R$500.00!')
elif n == 2:
    print('A bicicleta custa R$350.00!')
else:
    print('Opção Inválida!')

print('\033[36m~~'*10)
print('FORMAS DE PAGAMENTO')
print('~~'*10)
a = int(input('''\033[33m[1]\033[m À VISTA (DINHEIRO/CHEQUE)
\033[33m[2]\033[m À VISTA (CARTÃO)
\033[33m[3]\033[m EM 2X NO CARTÃO
\033[33m[4]\033[m EM 3X OU MAIS NO CARTÃO (ATÉ 10X)
\033[1mQual a forma de pagamento desejada?\033[m'''))
if a == 1:
    if n == 1:
        print('Você recebeu 10% de desconto! Pague R$450.00.')
    if n == 2:
        print('Você recebeu 10% de desconto! Pague R$315.00.')
if a == 2:
    if n == 1:
        print('Você recebeu 5% de desconto! Pague R$475.00.')
    if n == 2:
        print('Você recebeu 5% de desconto! Pague R$332.50.')
if a == 3:
    if n == 1:
        print('Você não recebeu desconto! pague 2 parcelas de R$250.00')
    if n == 2:
        print('Você não recebeu desconto! Pague 2 parcelas de R$175.00.')
if a == 4:
    v = int(input('\033[1mEm quantas vezes deseja pagar?\033[m'))
    y = 420.00 / v
    x = 600.00 / v
    if v == 3 or v == 4 or v == 5 or v == 6 or v == 7 or v == 8 or v == 9 or v == 10:
        if n == 1:
            print('A forma de pagamento escolhida tem um juros de 20%! Cada parcela será de R${:.2f}'.format(x))
        if n == 2:
            print('A forma de pagamento escolhida tem um juros de 20%! Cada parcela será de R${}'.format(y))
    elif v != 3 or v != 4 or v != 5 or v != 6 or v != 7 or v != 8 or v != 9 or v != 10:
        print('Opção Inválida!')

#MENOR E MAIOR VALOR
maior = 0
menor = 0
for p in range(1, 6):
    n = float(input('Digite o seu peso atual em Kg:'))
    if p == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))

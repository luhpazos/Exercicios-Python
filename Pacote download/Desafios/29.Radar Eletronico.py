v = int(input('A quantos Km/h estava o carro?'))
m = (v - 80)*7
if v > 80:
    print('A velocidade limite é 80Km/h. Você ultrapassou o limite e terá de pagar uma multa no valor de R${:.2f}'.format(m))
else:
    print('Continue assim! segurança em primeiro lugar!')

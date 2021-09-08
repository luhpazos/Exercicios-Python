number = float(input('Digite um número inteiro de 0 a 9999: '))
if(number > 9999):
    print('esse número é maior que 9999')
elif(number >= 1000):
    number = str(number)
    unidade = number[3]
    dezena = number[2]
    centena = number[1]
    milhar = number[0]
    decimais = number[4:]
    print('Unidade: {} \nDezena: {}\nCentena: {}\nMilhar: {}\nDecimais: {}'.format(unidade, dezena, centena, milhar, decimais))
elif(number >= 100):
    number = str(number)
    unidade = number[2]
    dezena = number[1]
    centena = number[0]
    milhar = 0
    decimais = number[3:]
    print('Unidade: {} \nDezena: {}\nCentena: {}\nMilhar: {}\nDecimais: {}'.format(unidade, dezena, centena, milhar, decimais))
elif(number >= 10):
    number = str(number)
    unidade = number[1]
    dezena = number[0]
    centena = 0
    milhar = 0
    decimais = number[2:]
    print('Unidade: {} \nDezena: {}\nCentena: {}\nMilhar: {}\nDecimais: {}'.format(unidade, dezena, centena, milhar, decimais))
elif(number >= 0):
    number = str(number)
    unidade = number[0]
    dezena = 0
    centena = 0
    milhar = 0
    decimais = number[1:]
    print('Unidade: {} \nDezena: {}\nCentena: {}\nMilhar: {}\nDecimais: {}'.format(unidade, dezena, centena, milhar, decimais))
elif(number < 0):
    print('esse número é menor que 0')
else:
    print('numero não compativel')
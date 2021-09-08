n1 = float(input('Qual é o preço atual do produto?'))
d = n1 - (0.05 * n1)
print('Na liquidação o valor desse produto será R${:.2f}, visto que ele terá 5% de desconto!'.format(d))

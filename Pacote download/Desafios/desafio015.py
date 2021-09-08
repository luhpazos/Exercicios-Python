n = int(input('Por quantos dias o carro foi alugado?'))
m = float(input('Quantos Km foram percorridos com o veículo?'))
d = n * 60
km = m * 0.15
t = d + km
print('o cliente deve pagar um total de R${:.2f}'.format(t))

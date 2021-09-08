n = input('digite algo:')
print('O tipo primitivo desse valor é', (type(n)))
print('É um número?', (n.isnumeric()))
print('É alfabético?', (n.isalpha()))
print('Só tem espaços?', (n.isspace()))
print('É alfanumérico?', (n.isalnum()))
print('Está em maiúscula?', (n.isupper()))
print('Está capitalizada?', (n.istitle()))


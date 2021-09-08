import random
a = str(input('Primeiro nome:'))
b = str(input('Segundo nome:'))
c = str(input('Terceiro nome:'))
d = str(input('Quarto nome:'))
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))

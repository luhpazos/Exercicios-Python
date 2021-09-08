import random
a = str(input('Primeiro nome:'))
b = str(input('Segundo nome:'))
c = str(input('Terceiro nome:'))
d = str(input('Quarto nome:'))
lista = [a, b, c, d]
t = random.choice(lista)
print('O aluno escolhido foi {}'.format(t))


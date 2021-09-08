import math
a = int(input('Digite um ângulo qualquer:'))
c = math.cos(math.radians(a))
s = math.sin(math.radians(a))
t = math.tan(math.radians(a))
print('O seno de {} vale {:.2f}\nO cosseno de {} vale {:.2f}\nA tangente de {} vale {:.2f}'.format(a, s, a, c, a, t))

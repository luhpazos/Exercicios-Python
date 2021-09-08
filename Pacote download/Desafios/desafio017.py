import math
co = int(input('qual o comprimento do cateto oposto?'))
ca = int(input('Qual o comprmento do cateto adjacente?'))
'''s = (co**2) + (ca**2)
t = sqrt(s)'''
h = math.hypot(co, ca)
print('A hipotenusa desse triângulo equivale a {:.2f}'.format(h))

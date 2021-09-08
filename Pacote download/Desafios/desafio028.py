import random
from time import sleep
l = [0, 1, 2, 3, 4, 5]
c = random.choice(l)
n = str(input('O computador escolheu um número entre 0 e 5. você consegue adivinhar qual número ele escolheu?')).strip().lower()
print('PROCESSANDO...')
sleep(2)
if n == 'sim':
   h = int(input('Ok.qual número ele escolheu?'))
   if h == c:
       print('UAU! você acertou!')
   else:
       print('Que pena! o número certo era {}!'.format(c))
else:
    print('Que pena! esperava mais de você!')


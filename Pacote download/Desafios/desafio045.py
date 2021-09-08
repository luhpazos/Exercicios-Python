import random
from time import sleep
a = ['pedra', 'papel', 'tesoura']
c = random.choice(a)
print('\033[33m~'*7)
print('JOKENPÔ')
print('\033[33m~\033[m'*7)
b = str(input('Vamos jogar? Escolha entre \033[1mPEDRA , PAPEL, TESOURA\033[m:')).strip().lower()
print('\033[33mJO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!\033[m')

if b == c:
    print('EMPATE!Você leu meu pensamento?')
elif b == 'papel' and c == 'pedra' or b == 'pedra' and c == 'tesoura' or b == 'tesoura' and c == 'papel':
    print('Que droga! Eu escolhi {}. Você VENCEU!'.format(c))
elif b == 'pedra' and c == 'papel' or b == 'tesoura' and c == 'pedra' or b == 'papel' and c == 'tesoura':
    print('Eu VENCI! Escolhi {}. Mais sorte da próxima vez!'.format(c))
import random
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = random.choice(l)
t = 1
n = int(input('Eu pensei em um número entre 0 e 10. você sabe o número em que pensei?'))
while n != c:
    if c > n:
        print('mais...', end='')
    if c < n:
        print('menos...', end='')
    n = int(input('Tente novamente:'.format(n)))
    t = t + 1
print('Parabéns! Você acertou e precisou de {} tentativas!'.format(t))

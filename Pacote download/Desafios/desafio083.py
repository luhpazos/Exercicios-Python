p = []
n = str(input('Digite uma expressão:'))
a = (' '.join(n).split())
p.append(a)
if a.count('(') == a.count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

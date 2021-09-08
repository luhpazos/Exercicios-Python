#ANTES DE USAR UM METODO COLOCAR ASPAS DUPLAS NO OUTRO
t = ('aprender', 'programar', 'linguagem', 'python',
     'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
     'mercado', 'programador', 'futuro')
#LETRAS NA ORDEM DE AEIOU
for t in t:
    a = t.count('a')
    e = t.count('e')
    i = t.count('i')
    o = t.count('o')
    u = t.count('u')
    print(f'\nNa palavra {t.upper()} temos: ', end='')
    if a > 0:
        print(f'{"a "*a}', end='')
    if e > 0:
        print(f'{"e "*e}', end='')
    if i > 0:
        print(f'{"i "*i}', end='')
    if o > 0:
        print(f'{"o "*o}', end='')
    if u > 0:
        print(f'{"u "*u}', end='')

#LETRAS NA ORDEM EM QUE APARECEM NA PALAVRA
for t in t:
    print(f'\nNa palavra {t.upper()} temos: ', end='')
    for p in t:
        if p.lower() in 'aeiou':
            print(p, end=' ')

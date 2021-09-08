#NOME, IDADE E SEXO DE 4 PESSOAS
so = 0
ida = 0
noh = ''
co = 0
for c in range(1, 5):
    print('-----{}° PESSOA-----'.format(c))
    n = str(input('Nome:')).strip().capitalize()
    i = int(input('Idade:'))
    s = str(input('Sexo [M/F]:')).strip().upper()
    so = so + i
    m = so / 4
    if c == 1 and s == 'M':
        ida = i
        noh = n
    else:
        if i > ida and s == 'M':
            ida = i
            noh = n
    if i < 20 and s == 'F':
        co = co + 1

print('A média de idade do grupo é de {} anos!'.format(m))
print('O homem mais velho tem {} anos e se chama {}.'.format(ida, noh))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(co))

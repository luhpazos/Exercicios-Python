def area(lar, comp):
    a = lar * comp
    print(f'A área de um terreno {lar} x {comp} é de {a}m².')


# programa principal
print('CONTROLE DE TERRENOS')
print('-' * 20)
l = float(input('LARGURA(m):'))
c = float(input('COMPRIMENTO(m):'))
area(l, c)

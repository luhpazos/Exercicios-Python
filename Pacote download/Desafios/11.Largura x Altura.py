l = float(input('Qual a largura da sua parede?'))
a = float(input('Qual a altura da sua parede?'))
ar = l * a
t = ar/2
print('Sua parede possui uma área de {:.3f}m² e será necessário {:.2f} litros de tinta para pintá-la!'.format(ar, t))

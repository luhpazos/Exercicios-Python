s = str(input('informe seu sexo: [M/F]')).strip().upper()[0]
while s not in 'MF':
    print('Opção inválida. Tente novamente')
    s = str(input('Qual o seu sexo? [M/F]')).strip().upper()[0]
print('Sexo {} registrado com sucesso. Obrigado!'.format(s))


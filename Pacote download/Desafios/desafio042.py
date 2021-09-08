print('vamos formar um triângulo? Me informe 3 valores quaisquer e eu te digo se com essas 3 retas é possível ouu não obtermos um triângulo!')
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
n3 = int(input('Digite o terceiro valor:'))

if (n1 - n2 < n3 < n1 + n2) and (n1 - n3 < n2 < n1 + n3) and (n2 - n3 < n1 < n2 + n3):
    print('Esse triângulo existe!')
    if n1 == n2 == n3:
        print('Esse triângulo é EQUILÁTERO!')
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print('Esse triângulo é ISÓCELES!')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('Esse triângulo é ESCALENO!')
else:
    print('Esse triângulo não existe!')
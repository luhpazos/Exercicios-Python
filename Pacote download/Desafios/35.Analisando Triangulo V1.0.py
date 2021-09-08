print('vamos formar um triângulo? Me informe 3 valores quaisquer e eu te digo se com essas 3 retas é possível ouu não obtermos um triângulo!')
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
n3 = int(input('Digite o terceiro valor:'))
t = n1 - n2 < n3 < n1 + n2
q = n1 - n3 < n2 < n1 + n3
r = n2 - n3 < n1 < n2 + n3
if n1 - n2 < n3 < n1 + n2:
    if n1 - n3 < n2 < n1 + n3:
        if n2 - n3 < n1 < n2 + n3:
            print('Esse triangulo exite!')
else:
    print('Esse triângulo não existe!')

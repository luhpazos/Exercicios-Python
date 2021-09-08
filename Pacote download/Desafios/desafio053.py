n = str(input('Digite uma frase qualquer:')).strip().upper()
a = n.replace(" ", "")
b = a[::-1]
if a == b :
    print('Essa frase é um paligrafo!')
    print(b)
else:
    print('Essa palavra não é um paligrafo!')

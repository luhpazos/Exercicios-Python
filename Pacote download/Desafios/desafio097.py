def escreva(msg):
    c = len(msg) + 4
    print('-' * c)
    print(f'  {msg}')
    print('-' * c)


# programa principal
for s in range(0, 3):
    escreva(str(input('Digite alguma frase ou palavra:')).strip().capitalize())

def leiaint(numero):
    global n
    while not numero.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido!\033[m')
        n = input('Digite um número:')
        leiaint(numero=n)
        break


# Programa
n = input('Digite um número:')
leiaint(n)
print(f'Você acabou de digitar o número {n}.')

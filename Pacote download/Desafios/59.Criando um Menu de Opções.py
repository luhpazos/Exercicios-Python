from time import sleep
n1 = int(input('Digite o 1º valor:'))
n2 = int(input('Digite o 2º valor:'))
m = 0
while m != 5:
    print('\033[36m=-\033[m'*20)
    m = int(input('''O que você deseja fazer?
\033[31m[1]\033[m SOMAR
\033[31m[2]\033[m MULTIPLICAR
\033[31m[3]\033[m MAIOR
\033[31m[4]\033[m NOVOS NÚMEROS
\033[31m[5]\033[m SAIR DO PROGRAMA
>>>Responda de acordo com o número listado:'''))
    print('\033[36m=-\033[m'*20)
    if m == 1:
        s = n1 + n2
        print('A soma entre {} + {} vale {}'.format(n1, n2, s))
    if m == 2:
        x = n1 * n2
        print('A multiplicação entre {} x {} vale {}'.format(n1, n2, x))
    if m == 3:
        if n1 > n2:
            print('O maior valor digitado foi {}'.format(n1))
        if n2 > n1:
            print('O maior valor digitado foi {}'.format(n2))
    if m == 4:
        print('Informe os números novamente.')
        n1 = int(input('Digite o 1º valor:'))
        n2 = int(input('Digite o 2º valor:'))
    if m != 1 and m != 2 and m != 3 and m != 4 and m != 5:
        print('Opção inválida! Tente novamente!')
print('FINALIZANDO...')
sleep(1)
print('\033[97mPrograma finalizado com sucesso!')

def fatorial(n, show=False):
    """
    -> Cálcula o fatorial de um número.
    :param n: Valor a ser calculado
    :param show: (opcional) mostra ou não o processo de cálculo
    :return: O valor fatorial de n
    """
    f = 1
    while n != 0:
        f *= n  # cálculo do fatorial
        n -= 1  # diminuição dos valores ate chegar em 0
        if show:
            print(f'{n + 1}', end=' ', )
            if n < 1:
                print('=', end=' ')
            else:
                print('x', end=' ')
    return f


# Programa
"""num = int(input('Digite um número para descobrir seu fatorial:'))
p = str(input('Você deseja ver o processo de cálculo? [S/N]')).strip().upper()[0]
if p == 'S':
    resp = fatorial(num, show=True)
else:
    resp = fatorial(num, show=False)
print(resp)"""

# Programa mais simples teste
"""resp = fatorial(7, True)
print(resp)"""

# Programa 3
num = int(input('Digite um número para descobrir seu fatorial:'))
sh = bool(input('Você deseja ver o processo de cálculo? [True/False]'))
resp = fatorial(num, sh)
print(resp)

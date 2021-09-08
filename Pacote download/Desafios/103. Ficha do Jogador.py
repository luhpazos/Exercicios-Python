def ficha(nome=None, gols=None):
    if nome == '':
        nome = '<desconhecido>'
    if not gols.isnumeric():
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa
n = str(input('Nome do jogador:')).strip().capitalize()
g = str(input('Número de gols:'))
ficha(n, g)

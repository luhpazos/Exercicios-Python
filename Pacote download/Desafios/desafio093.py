dados = dict()
g = []
dados['nome'] = str(input('Nome do Jogador:')).strip().capitalize()
p = int(input(f'Quantas partidas {dados["nome"]} jogou?'))
for c in range(0, p):
    q = int(input(f'Quantos gols {dados["nome"]} fez na {c + 1}º partida?'))
    g.append(q)
dados['gols'] = g
dados['total'] = sum(g)
print('=-'*20)
print(dados)
print('=-'*20)
for k, v in dados.items():
    print(f'{k}: {v}')
print('=-'*20)
print(f'O jogagor {dados["nome"]} jogou {p} partidas.')
for c, b in enumerate(g):
    print(f'=> Na partida {c + 1}, fez {b} gols.')
print(f'Foi um total de {dados["total"]} gols!')

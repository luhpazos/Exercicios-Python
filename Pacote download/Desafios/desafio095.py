jog = dict()
dados = []
g = []
gt = []
part = []
co = 0
while True:
    jog['nome'] = str(input('Nome do Jogador:')).strip().capitalize()
    p = int(input(f'Quantas partidas {jog["nome"]} jogou?'))
    part.append(p)
    for c in range(0, p):
        q = int(input(f'Quantos gols {jog["nome"]} fez na {c + 1}º partida?'))
        co += q
        g.append(q)
    jog['gols'] = g[:]
    jog['total'] = co
    dados.append(jog.copy())
    jog.clear()
    gt.append(g[:])
    g.clear()
    co = 0
    d = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    while d not in 'SN':
        d = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if d == 'N':
        break
print(dados)
print('=-'*20)
print(f'{"cod":<5} {"nome":<8} {"gols":<20} {"total":<15}')
print('--'*30)
for c in range(0, len(dados)):
    print(f'{c:<5} {dados[c]["nome"]:<8}', f'{str(gt[c]):<20}', f'{dados[c]["total"]:<15}')
print('--'*30)
while True:
    f = int(input('Mostrar dados de qual jogador?'))
    print('--'*20)
    for c in range(0, len(dados)):
        if f == c:
            print(f'Levantamento do jogador {dados[c]["nome"].upper()}:')
            for t in range(0, part[c]):
                print(f'No jogo {t + 1} fez {dados[c]["gols"][t]} gols.')
            print('--'*20)
    if not f <= len(dados) - 1 and f != 999:
        print(f'ERRO! Não existe jogador com o código {f}! Tente novamente.')
        print('--'*20)
    if f == 999:
        break
print('**VOLTE SEMPRE!**')

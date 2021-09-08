dados = dict()
dados['nome'] = str(input('Nome:')).strip().capitalize()
dados['media'] = float(input(f'Média de {dados["nome"]}:'))
if dados['media'] >= 7:
    dados['situaçao'] = 'Aprovado'
elif dados['media'] <= 5:
    dados['situaçao'] = 'Reprovado'
else:
    dados['situaçao'] = 'Recuperação'
for k, v in dados.items():
    print(f"{k.capitalize()} é igual a {v}")
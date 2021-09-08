import datetime
dados = dict()
dados['Nome'] = str(input('Nome:')).strip().capitalize()
dn = int(input('Ano de Nascimento:'))
i = datetime.date.today().year - dn
dados['Idade'] = i
dados['ctps'] = int(input('Carteira de trabalho (0 se não tem):'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação:'))
    dados['salário'] = float(input('Sálario: R$'))
    ap = dados['contratação'] + 35 - datetime.date.today().year + i
    dados['Aposentadoria'] = ap
    print('=-' * 20)
for k, v in dados.items():
    print(f'{k}: {v}')

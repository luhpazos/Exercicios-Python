def notas(*num, sit=False):
    """
    -> Funçao para avaliar notas e situações de vários alunos
    :param num: uma ou mais notas (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação do(a) aluno/turma
    """
    d = dict()
    d['total'] = q
    d['maior'] = max(t)
    d['menor'] = min(t)
    m = sum(t) / q
    d['média'] = f'{m:.2f}'
    if sit:
        if m >= 7:
            d['situação'] = 'BOA'
        if 7 > m >= 6:
            d['situação'] = 'RAZOÁVEL'
        if m < 6:
            d['situação'] = 'RUIM'
    return d


# PROGRAMA PRINCIPAL
t = list()
q = int(input('Quantas notas deseja digitar?'))
for c in range(0, q):
    n = float(input(f'Digite sua {c + 1} nota:'))
    t.append(n)
s = bool(input('Você deseja ver a sua situação baseada nas notas? ["True" se quer ver]'))
resp = notas(t, sit=s)
print(resp)

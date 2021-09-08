def voto(ano_nasc):
    import datetime
    id = datetime.datetime.now().year - ano_nasc
    print(f'Com {id} anos:', end=' ')
    vt = ''
    if id < 16:
        vt = 'NÃO VOTA.'
    if id >= 18:
        vt = 'VOTO OBRIGATÓRIO.'
    if id >= 65 or 18 > id >= 16:
        vt = 'VOTO OPCIONAL.'
    return vt


resp = voto(int(input('Em que ano você nasceu?')))
print(resp)

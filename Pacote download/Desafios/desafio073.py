t = ('Fortaleza', 'Athletico-PR', 'Atlético-MG', 'Bragantino', 'Palmeiras',
     'Flamengo', 'Atlético-GO', 'Fluminense', 'Bahia', 'Ceará', 'Santos',
     'Corinthians', 'Internacional', 'São Paulo', 'Chapecoense', 'Juventude',
     'Cuiabá', 'Sport Grêmio', 'América-MG')
print(f'Lista de times do Brasileirão: {t}')
print('=='*143)
print(f'Os cincos primeiros são: {t[0:5]}')
print('=='*48)
print(f'Os quatro últimos são: {t[-4:]}')
print('=='*50)
print(f'Os times em ordem alfabética: {sorted(t)}')
print('=='*143)
print(f'a Chapecoense está na {t.index("Chapecoense") + 1}º posição!')
from datetime import date
tmaior = 0
tmenor = 0
for c in range(1, 8):
    n = int(input('Digite o seu ano de nascimento:'))
    a = date.today().year - n
    if a >= 18:
        tmaior = tmaior + 1
    else:
        tmenor = tmenor + 1
print('Ao todo tivemos {} pessoas maiores de idade e\n{} pessoas menores de idade!'.format(tmaior, tmenor))

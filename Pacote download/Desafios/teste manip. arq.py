with open('inscritos.txt', 'r')as f:
    leitura = f.read()

    dados = []
    for x in leitura.split(";"):
        dados.append(x.split("\n"))

    f.close()

print(dados)
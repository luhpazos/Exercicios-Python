from time import sleep
c = ('\033[m',      # 0 - Sem cor
     '\033[36;7m',  # 1 - Verde agua
     '\033[34;7m',  # 2 - Azul
     '\033[7m',     # 3 - Branco
     '\033[31;7m'   # 4 - Vermelho
     '\033[40m')    # 5 - preto


def titulo(msg, cor=0):
    print(c[cor], end='')
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))
    print(c[0], end='')


def ajuda(com):
    titulo(f'Acessando o manual do comando {com}:', 2)
    sleep(1)
    print(c[3], end='')
    help(c)
    print(c[0], end='')


# PROGRAMA PRINCIPAL
co = ''
while True:
    sleep(0.7)
    titulo('SISTEMA DE AJUDA PY.HELP', 1)
    co = str(input('\033[40mFunção ou Biblioteca >')).strip()
    if co.upper() == 'FIM':
        break
    else:
        ajuda(co)
titulo('ATÉ LOGO!', 4)

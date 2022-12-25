# Exercício Python 106:
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.

c = ( ('\033[m'),  # 0 = Sem com
     \033[0;30;41[m,  # 1 = Branco
     )

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(f'{c[cor]}', end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')


#programa principal
comando = ''
while True:
    titulo('sistema de ajuda PyHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO')

# Exercício Python 098:
# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep

#funçoes
def linha():
    print('-='*30)

def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    linha()
    print(f'Contagem de {a} atá {b}, de {c} em {c}')
    sleep(2.5)

    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += c
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='')
            cont -= c
            sleep(0.5)
        print('FIM!')


def regressão():
    linha()
    print('Contagem do 10 ao 0, de 2 em 2')
    for i in range(10, -1, -2):
        print(f'{i} ', end='')
        sleep(0.5)
    print('FIM!')
    linha()

def contPersonalizado():
    linha()
    print('Contagem Personalizada')
    a = int(input('Escolha o inicio: '))
    b = int(input('Escolha o fim: '))
    c = int(input('Escolha o passo (1em1, 2em2, ...): '))
    print(f'Contagem de {a} até {b}, de {c} em {c}')
    linha()
    for i in range(a, b, c):
        print(f'{i} ', end='')
        sleep(0.5)
    print('FIM!')
    linha()

#principal
contador(1, 10, 1)
contador(10, 0, 2)
a = int(input('Escolha o inicio: '))
b = int(input('Escolha o fim: '))
c = int(input('Escolha o passo (1em1, 2em2, ...): '))
contador(a, b, c)

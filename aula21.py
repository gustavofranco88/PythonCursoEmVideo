# print(input.__doc__) #interactive help

from random import randint
from time import sleep


def sorteia(a):
    """
        --> Recebe uma lista e adiciona nomeros aleatórios à ela.

        :param a:recebe uma lista, pode ser lista vazia
        :return: retorna a lista sorteada no parametro 'a'
    """
    print(f'Sorteando 5 valores da lista = ', end='')
    for i in range(0, 5):
        n = randint(0, 20)
        a.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO')
    return a


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

def funcao():
    global n
    n = 4
    print(f'N dentro vale {n}')


w = somar()
q = somar(1, 3, 6)
e = somar(2)
r = somar(2, 3)
print(w, q, e, r)
n=2
funcao()
print(f'N fora vale {n}')


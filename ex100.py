# Exercício Python 100:
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
numeros = []


def sorteia(a):
    print(f'Sorteando 5 valores da lista = ', end='')
    for i in range(0, 5):
        n = randint(0, 20)
        a.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO')
    return a


def somaPar(l):
    soma = 0
    for i in l:
        if i % 2 == 0:
            soma += i
    print(f' Somando os valores pares de {l}, temos {soma}')
    return soma


# preencher lista


sorteia(numeros)


pares = somaPar(numeros)


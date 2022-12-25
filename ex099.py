# Exercício Python 099:
# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def qlMaior(a):
    maior = 0
    for i in a:
        if i > maior:
            maior = i
    print(f'O maior valor informado foi {maior}')

def maiorNum(* num):
    numeros = []
    maior = 0

    for i in num:
        numeros.append(i)

    if len(numeros) == 0:
        print('Nenhum valor passsado')
    else:
        for n in num:
            if n > maior:
                maior = n
        print(f'O maior valor informado foi {maior}')

list = []
while True:
    num = int(input('Digite um valor: '))
    list.append(num)
    op = str(input('Deseja continuar? (s/n) '))
    if op in 'nN':
        break

qlMaior(list)
maiorNum(1, 4, 65, 78, 3)
maiorNum(2, 4, 1, 3, -3)
maiorNum()


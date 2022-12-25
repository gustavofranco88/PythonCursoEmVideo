# Exercício Python 102:
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(a, show=False):
    '''
    CAlculo fatorial de um numero
    :param a: numero a ser calculado
    :param show: Se verdadeiro, mostra o calculo
    :return: resultado do calculo
    '''
    f = 1
    for i in range(a, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


valor = fatorial(5, True)
print(valor)

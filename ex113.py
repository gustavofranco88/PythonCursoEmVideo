# Exercício Python 113:
# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(texto):
    print('-'*20)
    while True:
        try:
            num = int(input(texto))
        except (TypeError, ValueError):
            print('\033[0;31mErro, voce não digitou um numero inteiro\033[m')
            continue
        except KeyboardInterrupt:
            print('Interrompido pelo usuario')
            break
        else:
            return num


def leiaFloat(msg):
    print('-' * 20)
    while True:
        try:
            num = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mErro, voce não digitou um numero decimal\033[m')
            continue
        except KeyboardInterrupt:
            print('Interrompido pelo usuario')
            break
        else:
            return num


# programa principal
n = leiaInt('Digite um numero inteiro ')
n_decimal = leiaFloat('Degite um numero decimal ')
print(f'Voce acabou de digitar o numero inteiro: {n}')
print(f'Voce acabou de digitar o numero decimal: {n_decimal}')
